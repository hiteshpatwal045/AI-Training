import pandas as pd
from config.database import Base, SessionLocal, engine
from model.employee_model import Employee, Payroll

DEPT = {"it": "IT", "i.t.": "IT", "information technology": "IT",
        "hr": "HR", "h.r.": "HR", "human resources": "HR",
        "finance": "Finance", "fin": "Finance",
        "sales": "Sales", "sales dept": "Sales",
        "operations": "Operations", "operation": "Operations", "ops": "Operations"}
CITY = {"bangalore": "bengaluru", "bombay": "mumbai", "madras": "chennai", "hyd": "hyderabad"}


def run_etl_pipeline(session=None, path="data/employee_payroll.csv"):
  df = pd.read_csv(path)
  df["Department"] = df["Department"].str.strip().str.lower().map(DEPT)
  df["City"] = df["City"].fillna("Unknown").str.strip().str.lower().replace(CITY).str.title()
  df["JoiningDate"] = pd.to_datetime(df["JoiningDate"], format="mixed").dt.date
  df["PayrollMonth"] = pd.to_datetime(df["PayrollMonth"], format="mixed").dt.date
  df = df.dropna(subset=["Department"]).drop_duplicates(["EmployeeID", "PayrollMonth"], keep="last")
  df["Bonus"] = df["Bonus"].fillna(0)
  df["BasicSalary"] = df["BasicSalary"].fillna(df.groupby("Department")["BasicSalary"].transform("median"))
  df["Gross"] = df["BasicSalary"] + df["HRA"] + df["Bonus"]
  df["Net"] = df["Gross"] - df["Deductions"]
  df["Att"] = (df["PresentDays"] / df["WorkingDays"] * 100).round(2)

  emps = df.drop_duplicates("EmployeeID", keep="last")
  own = session is None
  if own:
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
  try:
    session.query(Payroll).delete()
    session.query(Employee).delete()
    session.add_all(Employee(employee_id=r.EmployeeID, employee_name=r.EmployeeName,
                             department=r.Department, city=r.City, joining_date=r.JoiningDate)
                    for r in emps.itertuples())
    session.flush()
    session.add_all(Payroll(employee_id=r.EmployeeID, payroll_month=r.PayrollMonth,
                            basic_salary=r.BasicSalary, hra=r.HRA, bonus=r.Bonus,
                            deductions=r.Deductions, gross_salary=r.Gross, net_salary=r.Net,
                            working_days=r.WorkingDays, present_days=r.PresentDays,
                            attendance_pct=r.Att,
                            performance_rating=None if pd.isna(r.PerformanceRating) else int(r.PerformanceRating))
                    for r in df.itertuples())
    session.commit()
    return {"employees_in_db": len(emps), "payroll_rows_in_db": len(df)}
  except Exception:
    session.rollback()
    raise
  finally:
    if own:
      session.close()