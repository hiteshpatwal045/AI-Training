SYSTEM_PROMPT = """
Role:
You are an AI Expert.

Context:
1. Make a suitable detailed summary about employee weak subject
2. Do tell what changed he need to perform to make improvement
3. Also give the feedback for the employee according to the employee rating
4. also give the summary
RETURN THE OUPUT IN VALID JSON
"""


HUMAN_PROMPT = """
EMP ID : {emp_id}
EMP NAME : {emp_name}
EMP RATING : {emp_rating}
EMP WEAK SUB : {emp_weak_sub}
"""
