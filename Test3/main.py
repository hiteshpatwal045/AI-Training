from fastapi import FastAPI

from model.models import (
    VisitorRequest,
    VisitorResponse
)
# from service.services import analyze_data
from service.services import analyze_data1

app = FastAPI(
    title="Office Visitor Management System",
    version="1.1"
)


@app.get("/")
def home():
    return {
        "message": "Office Visitor Management System"
    }


@app.post("/api/v2", response_model=VisitorResponse)
def analyzingData2(req: VisitorRequest):
    result = analyze_data1(req)
    return result


# @app.post("/api/v1", response_model=VisitorResponse)
# def analyzingData(req: VisitorRequest):
#     result = analyze_data(req)
#     return result

@app.post("/api/v3", response_model=VisitorResponse)
def analyzingData2(req: VisitorRequest):
    result = analyze_data1({
        "visitor_id": req.visitor_id,
        "visitor_name": req.visitor_name,
        "purpose": req.purpose,
        "employee_name": req.employee_name,
        "visit_time": req.visit_time
    })

    return VisitorResponse(
        visitor_id = result.visitor_id,
        visitor_name = result.visitor_name,
        status = result.status,
        message = result.message,
        visiting_hours = result.visiting_hours,
    )
