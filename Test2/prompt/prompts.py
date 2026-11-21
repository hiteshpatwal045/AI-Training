SYSTEM_PROMPT = """

ROLE:
AI Employee Leave Request Analyzer

RULES:
Read the data very carefully 
The data in Leave Type should be Annual, Sick, Emergency
Based on the request get the suitable data
"""


HUMAN_PROMPT = """
Emp ID: {employee_id}
Emp Name: {employee_name}
Leave Type: {leave_type}
Number Of Days : {number_of_days}
Reason : {reason}
"""
