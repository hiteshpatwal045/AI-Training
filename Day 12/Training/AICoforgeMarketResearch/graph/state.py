from typing import TypedDict, Optional

from model.market_model import (
    ResearchResult,
    WriterResult,
    AnalysisResult
)


class MarketState(TypedDict, total=False):

    company: str
    industry: str
    country: str
    year: int
    question: str

    research_result: Optional[ResearchResult]
    analysis_result: Optional[AnalysisResult]
    writer_result: Optional[WriterResult]

    completed_agents: list[str]

    next_agent: str
