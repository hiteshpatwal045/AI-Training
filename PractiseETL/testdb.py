import pandas as pd

# Managers DataFrame
manager_data = [
    ['M001', 'Amit Sharma', 'IT', 'Pune', 180000],
    ['M002', 'Priya Nair', 'HR', 'Bengaluru', 88500],
    ['M003', 'Rahul Mehta', 'Finance', 'Kolkata', 210000],
    ['M004', 'Neha Kapoor', 'Sales', 'Mumbai', 95500],
    ['M005', 'Vikram Singh', 'Operations', 'Hyderabad', 99000],
    ['M006', 'Anjali Rao', 'IT', 'Jaipur', 102500],
    ['M007', 'Karan Shah', 'HR', 'Delhi', 106000],
    ['M008', 'Sneha Iyer', 'Finance', 'Chennai', 109500],
    ['M009', 'Rohit Verma', 'Sales', 'Pune', 113000],
    ['M010', 'Pooja Gupta', 'Operations', 'Bengaluru', 116500],
    ['M011', 'Arjun Patel', 'IT', 'Kolkata', 120000],
    ['M012', 'Meera Joshi', 'HR', 'Mumbai', 123500],
    ['M013', 'Nikhil Das', 'Finance', 'Hyderabad', 127000],
    ['M014', 'Ritu Malhotra', 'Sales', 'Jaipur', 130500],
    ['M015', 'Sanjay Kulkarni', 'Operations', 'Delhi', 134000],
    ['M016', 'Kavita Menon', 'IT', 'Chennai', 137500],
    ['M017', 'Dev Bansal', 'HR', 'Pune', 141000],
    ['M018', 'Isha Sethi', 'Finance', 'Bengaluru', 144500],
    ['M019', 'Manish Yadav', 'Sales', 'Kolkata', 148000],
    ['M020', 'Tanya Bose', 'Operations', 'Mumbai', 151500]
]

manager_df = pd.DataFrame(
    manager_data,
    columns=[
        'manager_id',
        'manager_name',
        'department',
        'city',
        'salary_inr'
    ]
)


# Employees DataFrame

employee_data = [
    ['E001', 'Aarav Kumar', 'IT', 'Delhi', 'M001', 32000],
    ['E002', 'Diya Shah', 'Finance', 'Jaipur', 'M008', 33750],
    ['E003', 'Aditya Jain', 'Operations', 'Hyderabad', 'M015', 35500],
    ['E004', 'Sara Khan', 'HR', 'Mumbai', 'M002', 37250],
    ['E005', 'Rohan Gupta', 'Sales', 'Kolkata', 'M009', 39000],
    ['E006', 'Ananya Das', 'IT', 'Bengaluru', 'M016', 40750],
    ['E007', 'Kabir Sinha', 'Finance', 'Pune', 'M003', 42500],
    ['E008', 'Ishita Rao', 'Operations', 'Chennai', 'M010', 44250],
    ['E009', 'Varun Nair', 'HR', 'Delhi', 'M017', 46000],
    ['E010', 'Simran Kaur', 'Sales', 'Jaipur', 'M004', 47750],
    ['E011', 'Yash Patel', 'IT', 'Hyderabad', 'M011', 49500],
    ['E012', 'Nisha Verma', 'Finance', 'Mumbai', 'M018', 51250],
    ['E013', 'Harsh Mehta', 'Operations', 'Kolkata', 'M005', 53000],
    ['E014', 'Tara Kapoor', 'HR', 'Bengaluru', 'M012', 54750],
    ['E015', 'Om Prakash', 'Sales', 'Pune', 'M019', 56500],
    ['E016', 'Riya Sen', 'IT', 'Chennai', 'M006', 58250],
    ['E017', 'Akash Singh', 'Finance', 'Delhi', 'M013', 60000],
    ['E018', 'Maya Iyer', 'Operations', 'Jaipur', 'M020', 61750],
    ['E019', 'Sahil Bansal', 'HR', 'Hyderabad', 'M007', 63500],
    ['E020', 'Pallavi Joshi', 'Sales', 'Mumbai', 'M014', 65250],

    # Extra records for advanced practice

    ['E021', 'Rakesh Gupta', 'IT', 'Pune', 'M001', 95000],
    ['E022', 'Pallav Roy', 'IT', 'Mumbai', 'M001', 105000],
    ['E023', 'Deepika Sharma', 'HR', 'Delhi', 'M002', 88000],
    ['E024', 'Sonali Jain', 'HR', 'Pune', 'M002', 94000],
    ['E025', 'Vinit Mehta', 'Finance', 'Jaipur', 'M003', 115000],
    ['E026', 'Mohan Rao', 'Finance', 'Chennai', 'M003', 121000],
    ['E027', 'Nitin Verma', 'Sales', 'Delhi', 'M004', 99000],
    ['E028', 'Kunal Bansal', 'Sales', 'Noida', 'M004', 108000],
    ['E029', 'Priyansh Shah', 'Operations', 'Mumbai', 'M005', 102000],
    ['E030', 'Vaibhav Singh', 'Operations', 'Pune', 'M005', 130000],
    ['E031', 'Ankita Kapoor', 'IT', 'Bengaluru', 'M001', 125000],
    ['E032', 'Sakshi Roy', 'Finance', 'Delhi', 'M003', 135000],
    ['E033', 'Raj Malhotra', 'HR', 'Chennai', 'M007', 118000],
    ['E034', 'Aman Gupta', 'Sales', 'Hyderabad', 'M009', 155000],
    ['E035', 'Nisha Sharma', 'Sales', 'Pune', 'M009', 85000],
    ['E036', 'Kriti Jain', 'Operations', 'Delhi', 'M005', 28000]
]

employee_df = pd.DataFrame(
    employee_data,
    columns=[
        'emp_id',
        'employee_name',
        'department',
        'city',
        'manager_id',
        'salary_inr'
    ]
)
