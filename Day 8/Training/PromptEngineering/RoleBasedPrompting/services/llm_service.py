from openai import OpenAI
import json

from prompts.prompt_role_based import (
    HUMAN_PROMPT,
    SYSTEM_PROMPT
)
from models.model_role_based import (
    PythonAIRequest,
    PythonAIResponse
)

from config.settings import (
    AZURE_API_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT
)

llm = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=f"{AZURE_API_ENDPOINT.rstrip('/')}/openai/v1"
)


def analyze_python_role_based(request: PythonAIRequest) -> PythonAIResponse:

    user_prompt = HUMAN_PROMPT.format(
        learner_name=request.learner_name,
        question=request.question,
        experience_level=request.experience_level
    )

    response = llm.responses.parse(
        model=AZURE_OPENAI_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=user_prompt,
        text_format=PythonAIResponse
    )
    # this also generate answer
    # return response.output_parsed
    ai_responses = response.output_text

    parse_data = json.loads(ai_responses)

    return PythonAIResponse(
        **parse_data
    )
