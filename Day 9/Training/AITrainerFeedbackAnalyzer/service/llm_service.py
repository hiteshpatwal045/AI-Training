from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import json

from config.settings import (
    AZURE_API_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)
from model.trainer_feedback_model import (
    TrainerFeedbackRequest,
    TrainerFeedbackResponse
)
from prompt.trainer_feedback_prompt import (
    HUMAN_PROMPT,
    SYSTEM_PROMPT
)

# Create the LLM
llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_API_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION
)


structured_llm = llm.with_structured_output(
    TrainerFeedbackResponse
)

# Prompt Making
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("user", HUMAN_PROMPT)
    ]
)

# Create the Langchain
chain = prompt | structured_llm

# create the function


def analyze_feedback(request: TrainerFeedbackRequest) -> TrainerFeedbackResponse:

    result = chain.invoke({
        "trainer_name": request.trainer_name,
        "training_topic": request.training_topic,
        "learner_name": request.learner_name,
        "rating": request.rating,
        "feedback": request.feedback
    })

    return result
