from crewai.tools import tool


@tool("Research Tool")
def research_tool(topic: str) -> str:
    """Gives a research checklist for a video topic."""
    return (
        f"For '{topic}' cover: definition, why it matters, key concepts, "
        "real-world example, common mistakes, next steps."
    )


@tool("Keyword Analysis Tool")
def keyword_tool(topic: str) -> str:
    """Gives keyword variations for a video topic."""
    t = topic.lower()
    return ", ".join([t, f"{t} tutorial", f"{t} for beginners",
                      f"what is {t}", f"{t} explained", f"{t} in python"])