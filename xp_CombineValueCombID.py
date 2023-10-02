# Import the pandas library and alias it as pd
import pandas as pd

# Read the CSV file "Fulldata_NewCombID.csv" and set the first column as the index
df = pd.read_csv("Fulldata_NewCombID.csv", index_col=0)

# Loop through the columns in the DataFrame and print their names and indices
for idx, column_name in enumerate(df.columns):
    print(f"Column Name: '{column_name}', Index: {idx}")

# Select a range of columns from index 40 to 50 (inclusive)
selected_columns = df.columns[40:51]

# Apply the 'join' function to concatenate selected columns as strings with '-' separator
# and create a new 'Komb_con' column with the concatenated values
df['Komb_con'] = df[selected_columns].astype(str).agg('-'.join, axis=1)

# Loop through the columns in the DataFrame again and print their names and indices
for idx, column_name in enumerate(df.columns):
    print(f"Column Name: '{column_name}', Index: {idx}")

# Save the modified DataFrame to a new CSV file named "FullData_CombID.csv"
df.to_csv("FullData_CombID.csv")