import numpy as np

def array_fundamentals(df):
  """N01-N10: array basics."""

  # N01. Convert Quantity into a NumPy array and show the first 10 values.
  qty = df["Quantity"].to_numpy()
  print("N01", qty[:10])

  # N02. Convert Net_Revenue_INR into a NumPy array and show the first 5 values.
  rev = df["Net_Revenue_INR"].to_numpy()
  print("N02", rev[:5])

  # N03. Show the dimensions, shape, size and data type of both arrays.
  print("N03 qty:", qty.ndim, qty.shape, qty.size, qty.dtype)
  print("N03 rev:", rev.ndim, rev.shape, rev.size, rev.dtype)

  # N04. Find the unique discount percentages.
  print("N04", np.unique(df["Discount_Pct"].to_numpy()))

  # N05. Create day numbers from 1 to 30.
  print("N05", np.arange(1, 31))

  # N06. Create 10 evenly spaced discount rates from 0 to 30.
  rates = np.linspace(0, 30, 10)
  print("N06", rates)

  # N07. Reshape the first 120 quantities into a 12 x 10 matrix.
  matrix = qty[:120].reshape(12, 10)
  print("N07", matrix.shape)

  # N08. Flatten the matrix back into one dimension.
  print("N08", matrix.flatten().shape)

  # N09. Join the first 50 and next 50 revenue values.
  joined = np.concatenate((rev[:50], rev[50:100]))
  print("N09", joined.shape)

  # N10. Count the orders with revenue above 1000.
  print("N10", np.sum(rev > 1000))


def statistics_operations(df):
  """N11-N20: statistics."""
  rev = df["Net_Revenue_INR"].to_numpy()
  qty = df["Quantity"].to_numpy()
  price = df["Unit_Selling_Price_INR"].to_numpy()
  discount = df["Discount_Pct"].to_numpy()

  # N11. Total revenue.
  print("N11", np.sum(rev))

  # N12. Mean order revenue.
  print("N12", np.mean(rev))

  # N13. Median order revenue.
  print("N13", np.median(rev))

  # N14. Standard deviation of revenue.
  print("N14", np.std(rev))

  # N15. Variance of revenue.
  print("N15", np.var(rev))

  # N16. Minimum and maximum revenue.
  print("N16", np.min(rev), np.max(rev))

  # N17. Percentiles 25, 50, 75 and 90 of revenue.
  print("N17", np.percentile(rev, [25, 50, 75, 90]))

  # N18. Average selling price weighted by quantity.
  print("N18", np.sum(price * qty) / np.sum(qty))

  # N19. Correlation between discount and quantity.
  print("N19", np.corrcoef(discount, qty)[0, 1])

  # N20. Distinct quantity values and the number of orders for each.
  values, counts = np.unique(qty, return_counts=True)
  print("N20", values)
  print("N20", counts)


def conditional_simulation(df):
  """N21-N30: conditions and simulation."""
  rev = df["Net_Revenue_INR"].to_numpy()
  profit = df["Profit_INR"].to_numpy()

  # N21. Label each order Profitable or Loss-making and count each label.
  label = np.where(profit >= 0, "Profitable", "Loss-making")
  print("N21", np.unique(label, return_counts=True))

  # N22. Group revenue into Low, Medium and High (33rd and 66th percentiles) and count each.
  low = np.percentile(rev, 33)
  high = np.percentile(rev, 66)
  category = np.where(rev <= low, "Low", np.where(rev <= high, "Medium", "High"))
  print("N22", np.unique(category, return_counts=True))

  # N23. Cap the discount rates at 20.
  rates = np.linspace(0, 30, 10)
  print("N23", np.clip(rates, 0, 20))

  # N24. Round the profit margins to 2 decimals (first 5).
  margin = df["Profit_Margin_Pct"].to_numpy()
  print("N24", np.round(margin, 2)[:5])

  # N25. Find the ten largest revenues.
  print("N25", np.sort(rev)[::-1][:10])

  # N26. Find the positions of the ten largest profits and the profits themselves.
  top10 = np.argsort(profit)[::-1][:10]
  print("N26", top10)
  print("N26", profit[top10])

  # N27. Check whether revenue has any missing (NaN) values.
  print("N27", np.isnan(rev).any())

  # N28. Total revenue now and after a 5% uplift.
  print("N28", np.sum(rev), np.sum(rev * 1.05))

  # N29. Simulate 1000 growth scenarios (mean 5%, spread 10%) and show revenue percentiles.
  np.random.seed(42)
  growth = np.random.normal(0.05, 0.10, 1000)
  scenario_revenue = np.sum(rev) * (1 + growth)
  print("N29", np.percentile(scenario_revenue, [5, 25, 50, 75, 95]))

  # N30. Break-even quantity for Dairy Milk Silk with a fixed cost of 50,000.
  silk = df[df["Product_Name"] == "Dairy Milk Silk"]
  profit_per_unit = silk["Unit_Selling_Price_INR"].mean() - silk["Unit_Cost_INR"].mean()
  print("N30", np.ceil(50000 / profit_per_unit))


def run_numpy_analysis(df):
  """Runs all NumPy sections (N01-N30)."""
  array_fundamentals(df)
  statistics_operations(df)
  conditional_simulation(df)