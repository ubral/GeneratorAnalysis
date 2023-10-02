import pandas as pd
import numpy as np
import os


columns = ['TG1 - VIBRACE VLT', 'TG2 - VIBRACE VLT', 'TG3 - VIBRACE VLT']

folder_path = '../CB_Data'
file_list = os.listdir(folder_path)

# Prepare an empty DataFrame to store the results
df = pd.DataFrame()

# Add the specified columns to the DataFrame
columns_df = [
    'dataset',
    'column',
    'mean',
    'median',
    'std',
    'sigma1',
    'sigma2',
    'sigma3',
    'sigma4',
    'sigma5',
    'sigma6',
    'TG1',
    'TG2',
    'TG3',
    'CountSigma3',
    'CountSigma6'
]

result = pd.DataFrame(columns=columns_df)

# Loop through the list of files in file_list
for file in file_list:
    # Check if the file has a '.csv' extension
    if file.endswith('.csv'):
        # Create the full file path by joining the folder_path and the file name
        file_path = os.path.join(folder_path, file)

        # Read the CSV file into a pandas DataFrame with the first column as the index
        df = pd.read_csv(file_path, index_col=0)

        # Loop through the columns of the DataFrame and enumerate them with their index
        for idx, column_name in enumerate(df.columns):
            print(f"Column Name: '{column_name}', Index: {idx}")

        # Loop through the columns in the 'columns' list
        for column in columns:
            # Check if the column exists in the DataFrame
            if column in df.columns:
                # Calculate various statistics for the column
                mean = df[column].mean()
                median = df[column].median()
                std = df[column].std()
                sigma1 = mean + std
                sigma2 = mean + 2 * std
                sigma3 = mean + 3 * std
                sigma4 = mean + 4 * std
                sigma5 = mean + 5 * std
                sigma6 = mean + 6 * std

                # Calculate specific statistics for columns with predefined names
                TG1 = df["TG1 - ČINNÝ VÝKON"].mean()
                TG2 = df["TG2 - ČINNÝ VÝKON"].mean()
                TG3 = df["TG3 - ČINNÝ VÝKON"].mean()

            column_to_analyze = df[column]
            # Use a condition to filter values greater than 5
            CountSigma3 = np.sum((column_to_analyze > sigma3) & (column_to_analyze < sigma6))
            CountSigma6 = np.sum(column_to_analyze > sigma6)
            print(CountSigma6, ' ', CountSigma3)
            # Append the results to the results DataFrame
            result.loc[len(result)] = [
                file,
                column,
                mean,
                median,
                std,
                sigma1,
                sigma2,
                sigma3,
                sigma4,
                sigma5,
                sigma6,
                TG1,
                TG2,
                TG3,
                CountSigma3,
                CountSigma6]

# Save the result to report.csv
# decimal_separator = ','

# Convert the DataFrame to CSV
result.to_csv('report.csv', index=False)
