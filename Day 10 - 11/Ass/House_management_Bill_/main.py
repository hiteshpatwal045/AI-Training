from fastapi import FastAPI

from model.maintenance_model import QuestionRequest, AnswerResponse
from workflow.maintenance_workflow import workflow_graph

app = FastAPI(title="House Maintenance Bill Assistant")


@app.post("/api/v1/ask", response_model=AnswerResponse)
def ask(data: QuestionRequest):
    result = workflow_graph.invoke({"question": data.question})

    return AnswerResponse(
        question=data.question,
        answer=result["answer"],
    )