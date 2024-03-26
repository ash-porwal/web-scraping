import pandas as pd

cols = ["a", "b", "c"]
df = pd.DataFrame(columns=cols)
print(df)
temp_a = ["a", "a1", "a2"]
temp_b = ["b", "b1", "b2"]
temp_c = ["c", "c1", "c2"]

# Creating a new DataFrame for the row to be appended
row_to_append = pd.DataFrame([{
    "a": temp_a,
    "b": temp_b,
    "c": temp_c
}])

# Using concat instead of append
df = pd.concat([df, row_to_append], ignore_index=True) # always set ignore index to True when appending rows
print(df)