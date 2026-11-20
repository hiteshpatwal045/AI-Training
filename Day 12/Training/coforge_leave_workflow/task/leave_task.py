from crewai import Task
from agent.approval_agent import approval_agent
from agent.hrpolicy_agent import hr_agent
from agent.leave_verification_agent import leave_verifier


def create_task(empId, req_day):

    verify_task = Task(
        description=f"""
        Employee ID: {empId} 
        Requested Days : {req_day}

        Use check_leave_balance to verify the employee.

        Return :
        -Employee ID
        -Empolyee name   
        -Available Leave balance
        -Requested leave days

        If employee does not exist,
        clearly report NOT_FOUND.   
        """,
        expected_output="Verified emp leave Details.",
        agent=leave_verifier
    )
    policty_task = Task(
        description=f"""
        Evaluate the verified leave request.

        Requested Days : {req_day}

        Company policy:
        1. Requested days must be positive.
        2. Requested days must mnot exceed 
            the avilable leave balance.
        3. Unknow empl are not eligible.
        4. Never invent leave balances.

        Return:
        ELIGIBLE or NOT_ELIGIBLE
        with a clear reason.
        """,
        expected_output="leave eligibility and reason",
        agent=hr_agent,
        context=[verify_task]
    )
    approval_task = Task(
        description=f"""
        Review the emp verfication 
        and HR policy analysis.

        Return:
        - Employee name
        - Requested Days
        - leave balance
        - Recommendation: Approve or Reject
        - Reason

        Only recommend APPROVE if 
        verification and policy checks pass.
        
        Do not modify and employee records.
        """,
        expected_output="Final Leave recommendation",
        agent=approval_agent,
        context=[verify_task, policty_task]
    )

    return [verify_task, policty_task, approval_task]
