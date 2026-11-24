from data.dataset1 import (
    orders_df,
    products_df,
    customers_df,
    employees_df,
    order_items_df
)


#  CREATION

# 1. Print all five tables.
print(orders_df)
print(products_df)
print(customers_df)
print(employees_df)
print(order_items_df)


# 2.  Create a Series from [10,20,30,40] with index ['a','b','c','d'].


# 3.  Create a Series from a dict and access values by label.


# 4.  Create a Series from a scalar with an index of length 5.


# 5.  Create a DataFrame from a dict of lists (3 columns, 4 rows).


# 6.  Create a DataFrame from a list of dicts.


# 7.  Create a DataFrame from a list of lists with column names.


# 8.  Create a DataFrame from a 2D NumPy array with custom index and columns.


# 9.  Create an empty DataFrame, then add 2 columns.


# 10.  Create a DataFrame from a dict of Series with different indexes; observe alignment.


# 11.  Create a DatetimeIndex with pd.date_range (10 days).


# 12.  Use pd.period_range and pd.timedelta_range.


# 13.  Use np.random.seed(42) + randint to make a (5,3) DataFrame.


# 14.  Build a Series with np.arange and np.linspace; check dtype.


# 15.  Copy customers with .copy(), modify the copy, confirm the original is unchanged.


# 16.  Show the difference between df2 = df and df2 = df.copy().


# 17.  Create a Series with dtype='category'; inspect .cat.categories.


# 18.  Use pd.DataFrame.from_dict(..., orient='index').


# 19.  Use pd.DataFrame.from_records.


# 20.  Print type() of a DataFrame, a column, and a row from loc
