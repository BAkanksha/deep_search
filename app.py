import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager
from styles import CSS, JS, EXAMPLES, HEADER_HTML, FOOTER_HTML

load_dotenv(override=True)


async def run(query: str):
    try:
        async for status_update in ResearchManager().run(query):
            yield status_update
    except Exception as e:
        # Gemini puts the real reason in the response body, not the exception text
        detail = ""
        response = getattr(e, "response", None)
        if response is not None:
            try:
                detail = response.text[:500]
            except Exception:
                pass
        print(f"Research failed: {type(e).__name__}: {e} {detail}", flush=True)
        yield (
            f"**The presses have jammed.** {type(e).__name__}: {e}\n\n"
            + (f"`{detail}`\n\n" if detail else "")
            + "Please try again in a minute."
        )


with gr.Blocks(title="Deep Research") as ui:
    gr.HTML(HEADER_HTML)

    with gr.Row(elem_classes="dr-query-row"):
        query_textbox = gr.Textbox(
            placeholder="Pose your question, dear reader...",
            show_label=False,
            container=False,
            autofocus=True,
            elem_id="dr-query",
            scale=5,
        )
        run_button = gr.Button("Begin Inquiry", variant="primary", elem_id="dr-run", scale=1)

    gr.HTML('<div class="dr-examples-label">Notable Inquiries</div>')
    gr.Examples(examples=EXAMPLES, inputs=query_textbox, elem_id="dr-examples")

    report = gr.Markdown(elem_id="dr-report")

    gr.HTML(FOOTER_HTML)

    run_button.click(run, inputs=query_textbox, outputs=report)
    query_textbox.submit(run, inputs=query_textbox, outputs=report)


if __name__ == "__main__":
    import os

    ui.launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
    )
