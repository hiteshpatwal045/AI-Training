from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)


from service.llm_service import create_llm
from model.market_model import AnalysisResult
from graph.state import MarketState


def analyst_agent(state: MarketState):
    print("Market Analyst Agent Started")
    research = state.get("research_result")

    if research is None:
        raise ValueError(
            "Research must be completed before analysis"
        )

    llm = create_llm()

    structured_llm = llm.with_structured_output(
        AnalysisResult
    )

    system_prompt = """
    You are an Enterprise Business Market Analysit. 

    Your responsibilites:
    1. Analyze the supplied market research
    2. Identify company strengths.
    3. Identify potential weaknesses.
    4. Identify market opportunites.
    5. Identity business threats. 
    6. Generate practical recommendations.

    Rules.
    - Base conclusions on the provided research.
    - Do not invent company-specific facts.
    - Mark unsupported assumptions as assumptions.
    - Return structured SWOT analysis.
    """

    user_prompt = f"""
    Company: {state['company']}
    Industry: {state['industry']}
    Country: {state['country']}

    Original Business Question:
    {state['question']}

    Research Findings:
    {research.model_dump_json(indent=2)}

    Perfrom SWOT analysis and generate
    business recommendations.
    """

    result = structured_llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])

    print("Market Analysis Agent Completed")

    return {
        "analysis_result": result,
        "completed_agents": (
            state.get("completed_agents", [])
            + ["Market Analyst Agent"]
        )
    }
