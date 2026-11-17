from langchain_core.messages import AIMessage
from agent.ai_agent import create_hospital_agent
from model.response_model import HospitalAskResponse
from model.request_model import HospitalAskRequest

# obj of agent
agent = create_hospital_agent()


def process_hospital_query(request: HospitalAskRequest) -> HospitalAskResponse:

    question = f"""
    message : {request.message}
    user_role: {request.user_role}
    """

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    tools_used = []

    for message in result["messages"]:
        if isinstance(message, AIMessage):
            for tool_call in message.tool_calls:
                tools_used.append(tool_call["name"])
                print("Tool Called: ", tool_call["name"])
                print("Arguments: ", tool_call["args"])

    answer = result["messages"][-1].content

    return HospitalAskResponse(
        status="success",
        response=str(answer),
        tools_used=tools_used,
        data={}
    )
