from typing import List
from pydantic import BaseModel


class YouTubeContentRequest(BaseModel):
    topic: str
    target_audience: str
    video_duration: int
    language: str
    content_style: str


class SEOContent(BaseModel):
    video_title: str
    video_description: str
    seo_keywords: List[str]
    hashtags: List[str]
    thumbnail_text: List[str]


class QualityReview(BaseModel):
    quality_score: int
    feedback: str