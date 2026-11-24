from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from prompt.prompts import (
    HUMAN_PROMPT,
    SYSTEM_PROMPT
)
from config.settings import (
    AZURE_API_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)
from model.models import (
    VisitorRequest,
    VisitorResponse,
    VisitorAnalysis
)


llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_API_ENDPOINT,
)

structure_llm = llm.with_structured_output(
    VisitorAnalysis
)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", HUMAN_PROMPT)
])


chain = prompt | structure_llm


# def analyze_data1(req: VisitorRequest) -> VisitorResponse:
#     result = chain.invoke({
#         "visitor_id": req.visitor_id,
#         "visitor_name": req.visitor_name,
#         "purpose": req.purpose,
#         "employee_name": req.employee_name,
#         "visit_time": req.visit_time
#     })

#     analysis = VisitorAnalysis(
#         visitor_id=req.visitor_id,
#         is_office_open=result["is_office_open"],
#         visitor_category=result.analysis.visitor_category,
#         approval_status=result.analysis.approval_status,
#         reason=result.analysis.reason
#     )

#     return {
#         "visitor_id":  result["visitor_id"],
#         "visitor_name": result["visitor_name"],
#         "status": result["status"],
#         "message": result["message"],
#         "visiting_hours": result["visiting_hours"]
#     }


def analyze_data1(req: VisitorRequest):
    result = chain.invoke({
        "visitor_id": req.visitor_id,
        "visitor_name": req.visitor_name,
        "purpose": req.purpose,
        "employee_name": req.employee_name,
        "visit_time": req.visit_time
    })
    return result
