import pandas as pd
import numpy as np

# =========================
# CUSTOMERS DATAFRAME
# =========================

customers_df = pd.DataFrame({
    'customer_id': [f'C{i}' for i in range(101, 126)],
    'name': [
        'Aarav Sharma', 'Priya Patel', 'Rohan Mehta', 'Sneha Iyer', 'Vikram Singh',
        'Ananya Reddy', 'Karan Malhotra', 'Neha Gupta', 'Arjun Nair', 'Pooja Desai',
        'Rahul Verma', 'Isha Kapoor', 'Siddharth Joshi', 'Meera Menon', 'Aditya Rao',
        'Kavya Pillai', 'Manish Yadav', 'Divya Bhatt', 'Harsh Agarwal', 'Tanvi Kulkarni',
        'Nikhil Chopra', 'Riya Banerjee', 'Sahil Khan', 'Simran Kaur', 'Varun Jain'
    ],
    'city': [
        'Pune', 'Mumbai', 'Delhi', 'Bengaluru', 'Hyderabad', 'Chennai', 'Kolkata',
        'Pune', 'Mumbai', ' delhi', 'Bengaluru', 'Hyderabad', 'Chennai', 'Pune',
        'MUMBAI', 'Delhi', 'Ahmedabad', 'Kolkata', 'Pune', 'Bengaluru', 'Delhi',
        'Hyderabad', 'Mumbai', 'Chennai', 'Pune'
    ],
    'age': [
        28, 34, 45, 29, np.nan, 31, 52, 26, 38, 41, 33, np.nan, 47,
        30, 36, 24, 55, 39, 27, 43, 35, np.nan, 32, 29, 48
    ],
    'gender': ['M', 'F'] * 12 + ['M'],
    'signup_date': [
        '2022-01-15', '2022-02-20', '2022-03-05', '2022-03-18', '2022-04-22',
        '2022-05-30', '2022-06-11', '2022-07-07', '2022-08-19', '2022-09-25',
        '2022-10-03', '2022-11-14', '2022-12-01', '2023-01-09', '2023-02-17',
        '2023-03-23', '2023-04-12', '2023-05-28', '2023-06-15', '2023-07-21',
        '2023-08-30', '2023-09-18', '2023-10-27', '2023-11-11', '2023-12-05'
    ],
    'membership': [
        'Gold', 'Silver', 'Basic', 'Gold', 'Silver', 'Basic', 'Gold', 'Basic', 'Silver',
        'Gold', 'Basic', 'Silver', np.nan, 'Gold', 'Basic', 'Silver', 'Gold', 'Basic',
        'Silver', 'Gold', 'Basic', 'Silver', 'Gold', 'Basic', 'Silver'
    ]
})

# =========================
# PRODUCTS DATAFRAME
# =========================

products_df = pd.DataFrame({
    'product_id': [f'P{i:02d}' for i in range(1, 23)],
    'product_name': [
        'Laptop', 'Smartphone', 'Headphones', 'Smartwatch', 'Tablet', 'Keyboard',
        'Mouse', 'Monitor', 'Office Chair', 'Desk Lamp', 'Backpack', 'Water Bottle',
        'Notebook', 'Pen Set', 'Running Shoes', 'T-Shirt', 'Jeans', 'Jacket',
        'Coffee Maker', 'Blender', 'Yoga Mat', 'Dumbbell Set'
    ],
    'category': (
        ['Electronics'] * 8 +
        ['Furniture'] * 2 +
        ['Accessories'] * 2 +
        ['Stationery'] * 2 +
        ['Clothing'] * 4 +
        ['Appliances'] * 2 +
        ['Fitness'] * 2
    ),
    'price': [
        65000, 30000, 3500, 8000, 25000, 1500, 700, 12000,
        9000, 1200, 2200, 500, 150, 300, 4000, 600, 2500,
        5500, 6500, 3800, 1000, 4500
    ],
    'stock': [
        15, 40, 100, 60, 25, 80, 150, 30, 20, 70, 90, 200,
        300, 250, 55, 120, 65, 35, 28, 45, 85, 40
    ],
    'rating': [
        4.5, 4.3, 4.1, np.nan, 4.0, 3.9, 4.2, 4.4, 4.0,
        3.8, 4.1, 4.6, 4.2, np.nan, 4.3, 3.7, 4.0, 4.2,
        4.1, 3.9, 4.5, 4.4
    ]
})

# =========================
# EMPLOYEES DATAFRAME
# =========================

employees_df = pd.DataFrame({
    'emp_id': [f'E{i:02d}' for i in range(1, 21)],
    'emp_name': [
        'Amit Kumar', 'Sunita Rao', 'Deepak Shah', 'Pallavi Nair', 'Rajesh Pillai',
        'Anjali Mishra', 'Suresh Reddy', 'Kritika Sen', 'Mohit Arora',
        'Lakshmi Iyer', 'Gaurav Saxena', 'Nisha Thakur', 'Tarun Bose',
        'Preeti Das', 'Vivek Dubey', 'Shweta Pandey', 'Ajay Bhatia',
        'Rekha Menon', 'Yash Goel', 'Komal Seth'
    ],
    'department': [
        'Sales', 'Sales', 'Sales', 'Support', 'Support', 'Marketing', 'Marketing',
        'IT', 'IT', 'HR', 'Sales', 'Sales', 'Support', 'Marketing', 'IT',
        'Sales', 'Support', 'HR', 'IT', 'Sales'
    ],
    'salary': [
        75000, 62000, 58000, 45000, 48000, 70000, 55000, 95000, 82000,
        52000, 60000, 56000, 46000, 64000, 88000, 59000, 47000, 54000,
        91000, 61000
    ],
    'joining_date': [
        '2019-03-15', '2020-06-01', '2021-01-10', '2020-09-14', '2021-07-19',
        '2018-11-05', '2022-02-28', '2017-08-21', '2019-12-02', '2020-04-13',
        '2022-05-16', '2021-10-25', '2023-01-09', '2019-07-30', '2018-03-12',
        '2022-09-05', '2023-03-20', '2021-02-08', '2017-05-17', '2023-06-26'
    ],
    'manager_id': [
        np.nan, 'E01', 'E01', np.nan, 'E04', np.nan, 'E06', np.nan, 'E08',
        np.nan, 'E01', 'E01', 'E04', 'E06', 'E08', 'E01', 'E04', 'E10', 'E08', 'E01'
    ],
    'performance_score': [
        8.5, 7.2, 6.8, 7.9, 6.5, 8.8, 7.0, 9.1, 8.0, 7.5,
        6.9, 7.3, np.nan, 8.2, 8.7, 7.1, 6.6, 7.8, 9.0, 7.4
    ]
})

# =========================
# ORDERS DATAFRAME
# =========================

orders_df = pd.DataFrame({
    'order_id': [f'O{i}' for i in range(1001, 1031)],
    'customer_id': [
        'C101', 'C103', 'C105', 'C102', 'C110', 'C107', 'C115', 'C101',
        'C120', 'C118', 'C104', 'C109', 'C125', 'C113', 'C122', 'C106',
        'C117', 'C103', 'C111', 'C124', 'C108', 'C119', 'C102', 'C116',
        'C123', 'C112', 'C114', 'C121', 'C101', 'C105'
    ],
    'emp_id': ['E01', 'E02', 'E03', 'E11', 'E12', 'E16', 'E20'] * 4 + ['E01', 'E02'],
    'order_date': [
        '2023-01-12', '2023-01-25', '2023-02-08', '2023-02-19', '2023-03-03',
        '2023-03-21', '2023-04-10', '2023-04-28', '2023-05-14', '2023-05-30',
        '2023-06-09', '2023-06-27', '2023-07-15', '2023-07-31', '2023-08-18',
        '2023-09-02', '2023-09-20', '2023-10-08', '2023-10-24', '2023-11-05',
        '2023-11-23', '2023-12-12', '2023-12-29', '2024-01-17', '2024-02-06',
        '2024-02-22', '2024-03-14', '2024-04-01', '2024-04-19', '2024-05-07'
    ],
    'status': [
        'Delivered', 'Delivered', 'Cancelled', 'Delivered', 'Returned',
        'Delivered', 'Delivered', 'Pending', 'Delivered', 'Cancelled',
        'Delivered', 'Delivered', 'Returned', 'Delivered', 'Pending',
        'Delivered', 'Delivered', 'Cancelled', 'Delivered', 'Delivered',
        'Returned', 'Delivered', 'Pending', 'Delivered', 'Delivered',
        'Delivered', 'Cancelled', 'Delivered', 'Pending', 'Delivered'
    ],
    'payment_mode': [
        'UPI', 'Card', 'COD', 'UPI', 'Card', 'NetBanking', 'UPI', 'COD',
        'Card', 'UPI', 'NetBanking', 'Card', 'UPI', 'COD', 'UPI', 'Card',
        'UPI', 'NetBanking', 'Card', 'UPI', 'COD', 'Card', 'UPI',
        'NetBanking', 'Card', 'UPI', 'COD', 'Card', 'UPI', 'Card'
    ]
})

# =========================
# ORDER ITEMS DATAFRAME
# =========================

order_items_df = pd.DataFrame({
    'item_id': range(1, 31),
    'order_id': [
        'O1001', 'O1001', 'O1002', 'O1003', 'O1004', 'O1004', 'O1005', 'O1006',
        'O1007', 'O1008', 'O1008', 'O1009', 'O1010', 'O1011', 'O1012', 'O1012',
        'O1013', 'O1014', 'O1015', 'O1016', 'O1017', 'O1018', 'O1019', 'O1020',
        'O1021', 'O1022', 'O1023', 'O1024', 'O1025', 'O1026'
    ],
    'product_id': [
        'P01', 'P03', 'P02', 'P05', 'P12', 'P13', 'P04', 'P07', 'P15', 'P09',
        'P10', 'P16', 'P11', 'P20', 'P06', 'P08', 'P14', 'P17', 'P19', 'P21',
        'P22', 'P18', 'P03', 'P12', 'P02', 'P07', 'P01', 'P13', 'P16', 'P21'
    ],
    'quantity': [
        1, 2, 1, 1, 3, 5, 1, 2, 1, 1, 2, 4, 1, 1, 1, 1, 10, 2, 1, 2,
        1, 1, 3, 2, 1, 4, 1, 6, 2, 1
    ],
    'discount': [
        0, 5, 10, 0, np.nan, 5, 0, 10, 15, 0, np.nan, 5, 0, 10, 0,
        5, 20, 0, 10, np.nan, 5, 0, 0, 10, 5, 0, 15, 5, np.nan, 0
    ]
})
