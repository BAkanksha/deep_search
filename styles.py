EXAMPLES = [
    "Most popular AI Agent frameworks in 2026",
    "Most commercially successful Agentic AI implementations in 2026",
    "Celebrities who don't like cheese",
]

HEADER_HTML = """
<header class="dr-masthead">
    <div class="dr-topline">
        <span id="dr-date">Est. MMXXVI</span>
        <span class="dr-topline-mid">Vol. II &middot; No. 2</span>
        <span>Price: One Query</span>
    </div>
    <div class="dr-rule dr-rule-double"></div>
    <div class="dr-ornament-row">
        <span class="dr-flourish">&#10086;</span>
        <h1 class="dr-title">The Deep Research</h1>
        <span class="dr-flourish dr-flourish-flip">&#10086;</span>
    </div>
    <p class="dr-tagline">An Inquiry into All Things &mdash; Gathered, Weighed &amp; Reported from the Wide Web</p>
    <div class="dr-rule"></div>
</header>
"""

FOOTER_HTML = """
<div class="dr-footer">
    <div class="dr-fleuron">&#10087; &nbsp; &#10087; &nbsp; &#10087;</div>
    <p>Printed by a Council of Agents &middot; Planner, Searcher, Scribe &amp; Courier</p>
</div>
"""

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Cinzel:wght@500;700&display=swap');

.gradio-container {
    --dr-paper: #f4ecd8;
    --dr-paper-deep: #e9dcbc;
    --dr-surface: #fbf6e9;
    --dr-ink: #2b2118;
    --dr-muted: #7a6a55;
    --dr-rule: #2b2118;
    --dr-rule-soft: #cdbb94;
    --dr-gold: #a8842c;
    --dr-burgundy: #7b1e22;
    --dr-shadow: rgba(43, 33, 24, 0.18);

    --dr-serif: "EB Garamond", Garamond, "Times New Roman", serif;
    --dr-display: "Playfair Display", Didot, Georgia, serif;
    --dr-caps: "Cinzel", "Trajan Pro", Georgia, serif;

    max-width: 980px !important;
    margin: 0 auto !important;
    padding: 2.5rem 2.25rem 3rem !important;
    color: var(--dr-ink) !important;
    font-family: var(--dr-serif) !important;
    font-size: 18px;
    background:
        radial-gradient(ellipse at 20% 0%, rgba(255, 255, 255, 0.55), transparent 55%),
        radial-gradient(ellipse at 100% 100%, rgba(168, 132, 44, 0.10), transparent 50%),
        var(--dr-paper) !important;
    border-left: 1px solid var(--dr-rule-soft);
    border-right: 1px solid var(--dr-rule-soft);
    box-shadow: 0 0 60px var(--dr-shadow);
}

.gradio-container.dark,
.dark .gradio-container,
body.dark .gradio-container,
html.dark .gradio-container {
    --dr-paper: #1a1612;
    --dr-paper-deep: #241e17;
    --dr-surface: #221c16;
    --dr-ink: #ece2c8;
    --dr-muted: #a89878;
    --dr-rule: #d9c99f;
    --dr-rule-soft: #4a3f30;
    --dr-gold: #d1ad55;
    --dr-burgundy: #d0756c;
    --dr-shadow: rgba(0, 0, 0, 0.6);
}

body, .dark body, body.dark { background: #d8c9a6 !important; }
.dark body, body.dark { background: #0d0b09 !important; }

/* ================= ANIMATIONS ================= */
@keyframes dr-fade-down {
    from { opacity: 0; transform: translateY(-14px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes dr-fade-up {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes dr-draw {
    from { transform: scaleX(0); }
    to   { transform: scaleX(1); }
}
@keyframes dr-ink-in {
    0%   { opacity: 0; letter-spacing: 0.25em; filter: blur(6px); }
    100% { opacity: 1; letter-spacing: -0.01em; filter: blur(0); }
}
@keyframes dr-sway {
    0%, 100% { transform: rotate(-6deg) translateY(0); }
    50%      { transform: rotate(6deg) translateY(-3px); }
}
@keyframes dr-quill {
    0%   { content: ""; }
    25%  { content: "."; }
    50%  { content: ".."; }
    75%  { content: "..."; }
}
@keyframes dr-shimmer {
    from { background-position: -200% 0; }
    to   { background-position: 200% 0; }
}
@keyframes dr-pulse-border {
    0%, 100% { box-shadow: 0 0 0 0 rgba(168, 132, 44, 0.0); }
    50%      { box-shadow: 0 0 0 6px rgba(168, 132, 44, 0.18); }
}

/* ================= MASTHEAD ================= */
.dr-masthead {
    text-align: center;
    margin-bottom: 2.25rem;
    animation: dr-fade-down 0.9s ease-out both;
}

.dr-topline {
    display: flex;
    justify-content: space-between;
    font-family: var(--dr-caps);
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--dr-muted);
    padding-bottom: 0.5rem;
}

.dr-rule {
    height: 1px;
    background: var(--dr-rule);
    transform-origin: center;
    animation: dr-draw 1.1s cubic-bezier(.6, .05, .25, 1) 0.2s both;
}

.dr-rule-double {
    height: 5px;
    background: transparent;
    border-top: 3px solid var(--dr-rule);
    border-bottom: 1px solid var(--dr-rule);
}

.dr-ornament-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.25rem;
    padding: 1.1rem 0 0.4rem;
}

.dr-title {
    font-family: var(--dr-display) !important;
    font-weight: 900 !important;
    font-size: clamp(2.2rem, 6.5vw, 4.4rem) !important;
    line-height: 1 !important;
    margin: 0 !important;
    color: var(--dr-ink) !important;
    animation: dr-ink-in 1.4s ease-out 0.3s both;
}

.dr-flourish {
    font-size: clamp(1.4rem, 3vw, 2.2rem);
    color: var(--dr-gold);
    display: inline-block;
    animation: dr-sway 5s ease-in-out infinite;
}
.dr-flourish-flip { transform: scaleX(-1); animation-delay: -2.5s; }

.dr-tagline {
    font-family: var(--dr-serif);
    font-style: italic;
    font-size: 1.02rem;
    color: var(--dr-muted);
    margin: 0.35rem 0 0.9rem !important;
    animation: dr-fade-up 1s ease-out 0.8s both;
}

/* ================= QUERY ROW ================= */
.dr-query-row {
    gap: 0 !important;
    align-items: stretch !important;
    animation: dr-fade-up 0.9s ease-out 1s both;
}

#dr-query, #dr-query > div, #dr-query .wrap, #dr-query .form, #dr-query .block {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    border-radius: 0 !important;
}

#dr-query textarea, #dr-query input {
    background: var(--dr-surface) !important;
    color: var(--dr-ink) !important;
    border: 1px solid var(--dr-rule) !important;
    outline: 1px solid var(--dr-rule-soft) !important;
    outline-offset: 3px !important;
    border-radius: 0 !important;
    padding: 1.05rem 1.25rem !important;
    font-size: 1.15rem !important;
    font-family: var(--dr-serif) !important;
    box-shadow: inset 0 1px 6px var(--dr-shadow) !important;
    line-height: 1.45 !important;
    resize: none !important;
    min-height: 58px !important;
    transition: outline-color 0.3s, box-shadow 0.3s !important;
}

#dr-query textarea:focus, #dr-query input:focus {
    outline-color: var(--dr-gold) !important;
    animation: dr-pulse-border 2.2s ease-in-out infinite;
}

#dr-query textarea::placeholder, #dr-query input::placeholder {
    color: var(--dr-muted) !important;
    font-style: italic;
    opacity: 1 !important;
}

#dr-run {
    position: relative;
    overflow: hidden;
    background: linear-gradient(to right, var(--dr-burgundy) 50%, var(--dr-ink) 50%) !important;
    background-size: 200% 100% !important;
    background-position: right bottom !important;
    color: var(--dr-paper) !important;
    border: 1px solid var(--dr-rule) !important;
    border-radius: 0 !important;
    font-family: var(--dr-caps) !important;
    font-weight: 700 !important;
    letter-spacing: 0.2em !important;
    font-size: 0.85rem !important;
    text-transform: uppercase !important;
    box-shadow: none !important;
    margin-left: 10px !important;
    min-width: 170px !important;
    padding: 1rem 1.5rem !important;
    transition: background-position 0.5s ease, transform 0.1s, letter-spacing 0.4s !important;
}

#dr-run:hover {
    background-position: left bottom !important;
    letter-spacing: 0.28em !important;
}

#dr-run:active { transform: translateY(2px) !important; }

/* ================= EXAMPLES ================= */
.dr-examples-label {
    font-family: var(--dr-caps);
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    color: var(--dr-burgundy);
    text-transform: uppercase;
    margin: 2.2rem 0 0.9rem 0;
    display: flex;
    align-items: center;
    gap: 1rem;
    animation: dr-fade-up 0.8s ease-out 1.2s both;
}

.dr-examples-label::before,
.dr-examples-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: var(--dr-rule-soft);
}

#dr-examples, #dr-examples > div, #dr-examples .wrap, #dr-examples .block {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}

#dr-examples label, #dr-examples .label-wrap, #dr-examples > div > .label-wrap {
    display: none !important;
}

#dr-examples table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    width: 100% !important;
    background: transparent !important;
    border: none !important;
}

#dr-examples thead { display: none !important; }
#dr-examples tbody { background: transparent !important; }

#dr-examples tr {
    background: transparent !important;
    display: flex !important;
    flex-wrap: wrap !important;
    justify-content: center !important;
    gap: 10px !important;
    border: none !important;
}

#dr-examples td, #dr-examples button {
    background: var(--dr-surface) !important;
    border: 1px solid var(--dr-rule-soft) !important;
    padding: 0.65rem 1.1rem !important;
    cursor: pointer !important;
    font-family: var(--dr-serif) !important;
    font-style: italic !important;
    font-size: 1rem !important;
    color: var(--dr-ink) !important;
    border-radius: 0 !important;
    margin: 0 !important;
    box-shadow: 2px 2px 0 var(--dr-rule-soft) !important;
    transition: transform 0.25s ease, box-shadow 0.25s ease, color 0.25s, border-color 0.25s !important;
    animation: dr-fade-up 0.7s ease-out both;
}

#dr-examples td:nth-child(1), #dr-examples button:nth-of-type(1) { animation-delay: 1.35s; }
#dr-examples td:nth-child(2), #dr-examples button:nth-of-type(2) { animation-delay: 1.5s; }
#dr-examples td:nth-child(3), #dr-examples button:nth-of-type(3) { animation-delay: 1.65s; }

#dr-examples td:hover, #dr-examples button:hover {
    color: var(--dr-burgundy) !important;
    border-color: var(--dr-gold) !important;
    transform: translate(-2px, -3px) rotate(-0.5deg);
    box-shadow: 5px 6px 0 var(--dr-gold) !important;
}

/* ================= REPORT ================= */
#dr-report {
    margin-top: 2.5rem !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--dr-ink) !important;
    min-height: 40px;
    font-family: var(--dr-serif) !important;
}

#dr-report > div, #dr-report .prose {
    background: transparent !important;
    color: var(--dr-ink) !important;
    font-family: var(--dr-serif) !important;
    font-size: 1.12rem !important;
}

#dr-report .prose > *, #dr-report .md > * {
    animation: dr-fade-up 0.7s ease-out both;
}

/* A lone paragraph = a streamed status line: show it as a "press is running" notice */
#dr-report p:only-child {
    text-align: center;
    font-style: italic;
    color: var(--dr-muted);
    padding: 1.2rem 1rem;
    border-top: 1px solid var(--dr-rule-soft);
    border-bottom: 1px solid var(--dr-rule-soft);
    background: linear-gradient(90deg, transparent 0%, rgba(168, 132, 44, 0.16) 50%, transparent 100%);
    background-size: 200% 100%;
    animation: dr-fade-up 0.5s ease-out both, dr-shimmer 2.4s linear infinite;
}
#dr-report p:only-child::before { content: "\\2712\\00a0\\00a0"; color: var(--dr-gold); font-style: normal; }
#dr-report p:only-child::after { content: ""; animation: dr-quill 1.4s steps(1) infinite; }

#dr-report h1 {
    font-family: var(--dr-display) !important;
    font-size: 2.3rem !important;
    font-weight: 900 !important;
    text-align: center;
    color: var(--dr-ink) !important;
    line-height: 1.12 !important;
    padding: 0 0 0.9rem !important;
    margin: 0.5rem 0 1.4rem !important;
    border-bottom: 3px double var(--dr-rule);
}

#dr-report h1::after {
    content: "\\2766";
    display: block;
    font-size: 1.2rem;
    color: var(--dr-gold);
    margin-top: 0.6rem;
}

#dr-report h2 {
    font-family: var(--dr-display) !important;
    font-size: 1.55rem !important;
    font-style: italic;
    color: var(--dr-burgundy) !important;
    font-weight: 700 !important;
    margin-top: 2.2rem !important;
    padding-bottom: 0.3rem;
    border-bottom: 1px solid var(--dr-rule-soft);
}

#dr-report h3 {
    font-family: var(--dr-caps) !important;
    font-size: 1rem !important;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--dr-ink) !important;
    margin-top: 1.6rem !important;
}

#dr-report p { line-height: 1.75; text-align: justify; hyphens: auto; }

/* Drop cap on the opening paragraph of the report */
#dr-report h1 + p::first-letter {
    font-family: var(--dr-display);
    float: left;
    font-size: 4.2em;
    line-height: 0.82;
    padding: 0.06em 0.12em 0 0;
    color: var(--dr-burgundy);
    font-weight: 900;
}

#dr-report a {
    color: var(--dr-burgundy) !important;
    text-decoration: none;
    background-image: linear-gradient(var(--dr-gold), var(--dr-gold));
    background-size: 0% 1px;
    background-position: 0 100%;
    background-repeat: no-repeat;
    border-bottom: 1px dotted var(--dr-burgundy);
    transition: background-size 0.35s ease;
}
#dr-report a:hover { background-size: 100% 1px; border-bottom-color: transparent; }

#dr-report code {
    background: var(--dr-paper-deep);
    border: 1px solid var(--dr-rule-soft);
    padding: 0.1rem 0.4rem;
    font-size: 0.88em;
    border-radius: 0;
}

#dr-report pre {
    background: var(--dr-surface);
    border: 1px solid var(--dr-rule-soft);
    border-radius: 0;
    padding: 1rem 1.25rem;
}

#dr-report blockquote {
    border-left: 3px solid var(--dr-gold) !important;
    background: var(--dr-surface);
    font-style: italic;
    padding: 1rem 1.5rem;
    margin: 1.4rem 0;
    color: var(--dr-ink);
}

#dr-report hr {
    border: none !important;
    text-align: center;
    margin: 2rem 0;
}
#dr-report hr::after { content: "\\2042"; color: var(--dr-gold); font-size: 1.3rem; }

#dr-report ul, #dr-report ol { padding-left: 1.6rem; }
#dr-report li { margin: 0.35rem 0; line-height: 1.65; }
#dr-report li::marker { color: var(--dr-gold); }

#dr-report table {
    border-collapse: collapse;
    border-top: 2px solid var(--dr-rule);
    border-bottom: 2px solid var(--dr-rule);
    margin: 1.5rem 0;
}

#dr-report th, #dr-report td {
    border-bottom: 1px solid var(--dr-rule-soft);
    padding: 0.55rem 0.9rem;
    text-align: left;
}

#dr-report th {
    font-family: var(--dr-caps);
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--dr-burgundy);
}

#dr-report tr { transition: background 0.2s; }
#dr-report tbody tr:hover { background: var(--dr-paper-deep); }

/* ================= FOOTER ================= */
.dr-footer {
    text-align: center;
    margin-top: 3rem;
    padding-top: 1rem;
    border-top: 3px double var(--dr-rule);
    color: var(--dr-muted);
    animation: dr-fade-up 1s ease-out 1.8s both;
}
.dr-fleuron { color: var(--dr-gold); letter-spacing: 0.3em; font-size: 1.1rem; }
.dr-footer p {
    font-family: var(--dr-caps);
    font-size: 0.68rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    margin: 0.5rem 0 0 !important;
}

footer { display: none !important; }

/* ================= RESPONSIVE ================= */
/* Never let anything push the page wider than the screen */
html, body { overflow-x: hidden; }
.gradio-container, .gradio-container * { box-sizing: border-box; }
.gradio-container { width: 100% !important; }

/* Long example prompts wrap instead of overflowing */
#dr-examples td, #dr-examples button {
    max-width: 100% !important;
    white-space: normal !important;
    overflow-wrap: anywhere;
    text-align: center;
}

/* Wide report content scrolls inside itself, not the page */
#dr-report table { display: block; max-width: 100%; overflow-x: auto; }
#dr-report pre { max-width: 100%; overflow-x: auto; }
#dr-report img { max-width: 100%; height: auto; }
#dr-report a, #dr-report code { overflow-wrap: anywhere; }

/* Tablet */
@media (max-width: 900px) {
    .gradio-container {
        padding: 2rem 1.5rem 2.5rem !important;
        border-left: none;
        border-right: none;
        box-shadow: none;
    }
    #dr-run { min-width: 140px !important; letter-spacing: 0.14em !important; }
    #dr-report h1 { font-size: 2rem !important; }
}

/* Phone */
@media (max-width: 700px) {
    .gradio-container { padding: 1.25rem 1rem 2rem !important; font-size: 16px; }
    .dr-masthead { margin-bottom: 1.5rem; }
    .dr-topline { font-size: 0.62rem; letter-spacing: 0.12em; }
    .dr-topline-mid { display: none; }
    .dr-flourish { display: none; }
    .dr-ornament-row { padding: 0.9rem 0 0.3rem; }
    .dr-tagline { font-size: 0.92rem; }

    .dr-query-row { flex-direction: column !important; flex-wrap: nowrap !important; }
    .dr-query-row > * { width: 100% !important; min-width: 0 !important; flex: none !important; }
    #dr-query textarea, #dr-query input { font-size: 1rem !important; padding: 0.9rem 1rem !important; }
    #dr-run {
        margin: 12px 0 0 !important;
        width: 100% !important;
        min-width: 0 !important;
        padding: 0.9rem 1rem !important;
    }
    #dr-run:hover { letter-spacing: 0.2em !important; }

    .dr-examples-label { margin: 1.6rem 0 0.75rem; letter-spacing: 0.2em; gap: 0.6rem; }
    #dr-examples tr { flex-direction: column !important; gap: 8px !important; }
    #dr-examples td, #dr-examples button { width: 100% !important; font-size: 0.95rem !important; }
    #dr-examples td:hover, #dr-examples button:hover { transform: none; box-shadow: 2px 2px 0 var(--dr-gold) !important; }

    #dr-report { margin-top: 1.75rem !important; }
    #dr-report > div, #dr-report .prose { font-size: 1rem !important; }
    #dr-report h1 { font-size: 1.6rem !important; }
    #dr-report h2 { font-size: 1.25rem !important; margin-top: 1.6rem !important; }
    #dr-report h3 { font-size: 0.9rem !important; }
    #dr-report p { text-align: left; hyphens: manual; }
    #dr-report h1 + p::first-letter { font-size: 3.2em; }
    #dr-report blockquote { padding: 0.75rem 1rem; }
    #dr-report ul, #dr-report ol { padding-left: 1.2rem; }

    .dr-footer { margin-top: 2rem; }
    .dr-footer p { font-size: 0.6rem; letter-spacing: 0.14em; line-height: 1.7; }
}

/* Small phones */
@media (max-width: 380px) {
    .gradio-container { padding: 1rem 0.75rem 1.5rem !important; }
    .dr-topline { justify-content: center; }
    .dr-topline > span:last-child { display: none; }
}

@media (prefers-reduced-motion: reduce) {
    .gradio-container *, .gradio-container *::before, .gradio-container *::after {
        animation: none !important;
        transition: none !important;
    }
}
"""

JS = """
() => {
    // Classic dateline, e.g. "Thursday, November 19, 2026"
    const setDate = () => {
        const el = document.getElementById("dr-date");
        if (!el) return false;
        el.textContent = new Date().toLocaleDateString("en-US", {
            weekday: "long", year: "numeric", month: "long", day: "numeric"
        });
        return true;
    };
    const focus = () => {
        const el = document.querySelector("#dr-query textarea, #dr-query input");
        if (el) { el.focus(); return true; }
        return false;
    };
    let tries = 0;
    const i = setInterval(() => {
        const done = setDate() & focus();
        if (done || ++tries > 30) clearInterval(i);
    }, 100);
}
"""
