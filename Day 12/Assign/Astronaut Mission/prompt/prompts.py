SYSTEM_PROMPT = """
Role: 
you are a astronaut Mission readiness analyzer


Rules:
based on the input generate the output clearly and accurately
and the mission_status only contain values like after analysis
- APPROVED
- TRAINING_REQUIRED
- REJECTED

"""

HUMAN_PROMPT = """
Ast ID : {ast_id}
Ast Name: {ast_name}
Age :  {age}
Traing Housr :  {training_hours}
Medical Clerance :  {medical_clearance}
Previous Mission  {previous_missions}
"""