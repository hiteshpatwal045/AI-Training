# HSBC Banking Analytics 

# Business Scenario 
# You are a Data Analyst supporting a fictional HSBC Retail Banking Analytics team. The team needs insights into customer balances, deposits, withdrawals, credit scores, account activity and branch performance. Build a reproducible Python analysis using NumPy and Pandas to answer the questions below. All customer records are synthetic and are intended solely for training. 
# Learning Objectives 
# Manipulate numerical banking data with NumPy arrays, vectorization and statistical functions. 
# Load, inspect, clean, filter, sort, group and reshape data using Pandas. 
# Interpret banking KPIs and produce a concise branch-wise business summary. 

#1. Convert Account_Balance into a NumPy array. 
print("===============================1===============================")
import pandas as pd
import numpy as np

df = pd.read_csv("HSBC_Synthetic_Banking_Customers.csv")
print(df["Account_Balance"])

account_balance = np.array(df["Account_Balance"])
monthly_deposit = np.array(df["Monthly_Deposit"])
credit_score = np.array(df["Credit_Score"])
monthly_Withdrawal = np.array(df["Monthly_Withdrawal"])
customer_name = np.array(df["Customer_Name"])
monthly_income = np.array(df["Monthly_Income"])
customer_id = pd.DataFrame(df["Customer_ID"])

print(account_balance)

# 2. Inspect array ndim, shape, size and dtype. 
print("===============================2===============================")
print("Dimensions : ", account_balance.ndim)
print("Shape : ", account_balance.shape)
print("Size : ", account_balance.size)
print("Datatype : ", account_balance.dtype)


# 3. Calculate minimum and maximum balances.
print("===============================3===============================") 
print("Minimum balance : ", account_balance.min())
print("Maximum balance : ", account_balance.max())

# 4. Calculate sum, mean, median and standard deviation of balances. 
print("===============================4===============================")
print("Sum : ", account_balance.sum())
print("Mean :", account_balance.mean())
print("Median :", np.median(account_balance))
print("Standard Deviation : ", account_balance.std())

# 5. Find the 25th, 50th and 75th balance percentiles. 
print("===============================5===============================")
print(np.percentile(account_balance, [25, 50, 75]))

# 6. Filter balances above INR 500,000.
print("===============================6===============================") 
print("Balances > 5lakh : ", account_balance[account_balance > 500000])

# 7. Identify credit scores below 650 using boolean masking. 
print("===============================7===============================")
mask = credit_score < 650
print("Credit Score < 650 : ", df[mask])

# 8. Sort balances ascending and descending. 
print("===============================8===============================")
print("Sorted Account Balance in asc : ")
print(np.sort(account_balance))
print("Sorted Account Balance in desc: ")
print(np.sort(account_balance)[::-1])

# 9. Compute total monthly deposits and total monthly withdrawals. 
print("===============================9===============================")
print("Total monthly Deposits : ", monthly_deposit.sum())
print("Total monthly Withdrawal : ", monthly_Withdrawal.sum())

# 10. Use vectorization to calculate hypothetical balances after a 5% increase. 
print("===============================10===============================")
print("after 5% increase : ", account_balance * 1.05)

# 11. Use np.where to classify balances as High (> INR 500,000) or Low. 
print("===============================11===============================")
print(np.where(account_balance > 500000, "High" , "Low"))

# 12. Use np.select to categorize balances into Low (< INR 100,000), Medium (INR 100,000–500,000) and High (> INR 500,000). 
print("===============================12===============================")
conditions = [
    account_balance < 100000,
    (account_balance >= 100000) & (account_balance <= 500000),
    account_balance > 500000
]
choices = ["Low", "Medium", "High"]
balance_categories = np.select(conditions,choices,default="Unknown")

print(balance_categories)

# 13. Compute deposit-to-income ratio; handle zero income safely. 
print("===============================13===============================")
ratio = np.where(monthly_income > 0,monthly_deposit / monthly_income,0)

print(ratio)

# 14. Identify records where monthly withdrawals exceed monthly deposits. 
print("===============================14===============================")
print(df[monthly_Withdrawal > monthly_deposit])

# 15. Use np.unique to summarize credit-score frequencies. 
print("===============================15===============================")
print(df["Credit_Score"].nunique())

# 16. Use np.argsort to locate the five largest balances. 
print("===============================16===============================")

# 17. Perform min-max normalization of balances; handle constant arrays safely. 
print("===============================17===============================")
if account_balance.max() != account_balance.min():
    normalized_balances = (account_balance - account_balance.min()) / (
        account_balance.max() - account_balance.min()
    )
else:
    normalized_balances = 0

print(normalized_balances)

# 18. Compute z-scores for balances; handle zero standard deviation safely. 
print("===============================18===============================")

# 19. Build a 2D array with balance, deposit and withdrawal columns and inspect axis-wise totals. 
print("===============================19===============================")
# array2d = np.array([
#     account_balance,
#     monthly_deposit,
#     monthly_Withdrawal
# ])
# print(array2d.shape)


# 20. Calculate Pearson correlation between income and account balance. 
print("===============================20===============================")

# 21. Read the supplied CSV using pd.read_csv. 
print("===============================21===============================")
df = pd.read_csv("HSBC_Synthetic_Banking_Customers.csv")
print(df)

# 22. Display first and last ten rows. 
print("===============================22===============================")
print(df.head(10))
print(df.tail(10))

# 23. Inspect shape, columns, dtypes and info(). 
print("===============================23===============================")
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

# 24. Generate numerical descriptive statistics using describe(). 
print("===============================24===============================")
print(df.describe())

# 25. Check missing values and duplicate Customer_ID values.
print("===============================25===============================")
print("Missing: ", df["Customer_ID"].isnull().sum()) 
print("Missing: ", df["Customer_ID"].duplicated().sum()) 
print("Missing: ", customer_id.isnull().sum())
print("Missing: ", customer_id.duplicated().sum())

# 26. Select customer name, city, balance and credit score columns.
print("===============================26===============================")
multiple_col = df[
    [
        "Customer_Name",
        "City",
        "Account_Balance",
        "Credit_Score"
    ]
]
print(multiple_col)

# 27. Filter customers aged 25 through 40 inclusive. 
print("===============================27===============================")
filtered_age = df[(df["Age"] >= 25) & (df["Age"] <= 40)]
print(filtered_age)

# 28. Find active Savings accounts. 
print("===============================28===============================")
active_savings = df[(df["Account_Type"] == "Savings") & (df["Account_Status"] == "Active")]
print(active_savings)

# 29. Sort by balance and monthly income, descending.
print("===============================29===============================") 
print("Sort by balance and monthly income, desc :")
print( 
      df.sort_values(
          by=["Account_Balance","Monthly_Income"],
          ascending=False
        )
    )

# 30. Create Net_Monthly_Flow = Monthly_Deposit - Monthly_Withdrawal. 
print("===============================30===============================")
df["Net_Monthly_Flow"] = df["Monthly_Deposit"] - df["Monthly_Withdrawal"]
print(df[["Customer_Name", "Net_Monthly_Flow"]])

# 31. Group by City and calculate total Account_Balance. 
print("===============================31===============================")
city_balances = df.groupby("City")["Account_Balance"].sum()
print(city_balances)

# 32. Group by Account_Type and calculate average Monthly_Income. 
print("===============================32===============================")
type_income = df.groupby("Account_Type")["Monthly_Income"].mean()
print(type_income)

# 33. Compute branch-wise deposit and withdrawal totals. 
print("===============================33===============================")
branch_totals = df.groupby("Branch")[["Monthly_Deposit", "Monthly_Withdrawal"]].sum()
print(branch_totals)

# 34. Use agg to report minimum, maximum, mean and median balances by branch. 
print("===============================34===============================")
branch_balance_stats = df.groupby("Branch")["Account_Balance"].agg(["min", "max", "mean", "median"])
print(branch_balance_stats)

# 35. Create a pivot table of total balance by City and Account_Type. 
print("===============================35===============================")

# 36. Use pd.cut to create age groups: 18–25, 26–40, 41–60 and 61+. 
print("===============================36===============================")

# 37. Use groupby().transform() to calculate each customer’s balance minus branch average. 
print("===============================37===============================")

# 38. Create a separate Branch_Details DataFrame with Branch and Region; merge it on Branch and validate the join. 
print("===============================38===============================")

# 39. Find the top three customers by balance within each City. 
print("===============================39===============================")
top3_customers = (
    df.sort_values("Account_Balance", ascending=False)
      .groupby("City")
      .head(3)
)

print(top3_customers[["Customer_Name", "City", "Account_Balance"]])

# 40. Create a branch summary with total balance, mean credit score, counts by account status and total net monthly flow.
print("===============================40===============================")
