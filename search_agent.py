from agents import Agent, ModelSettings, function_tool
from ddgs import DDGS
from gemini_model import MODEL


@function_tool
def web_search(query: str) -> str:
    """
    Search the web and return the top results.

    Args:
        query: The search term to look up
    """
    try:
        results = DDGS().text(query, max_results=6)
    except Exception as e:
        return f"Search failed: {e}"
    if not results:
        return "No results found."
    return "\n\n".join(f"{r['title']}\n{r['href']}\n{r['body']}" for r in results)


INSTRUCTIONS = """
You are a research assistant. Given a search term, you search the web for that term and
produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 words.
Capture the main points and be succinct. Reply only with the summary.
"""

settings = ModelSettings(tool_choice="required")

search_agent = Agent(name="Search Agent", instructions=INSTRUCTIONS, tools=[web_search], model=MODEL, model_settings=settings)
