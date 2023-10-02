# Import necessary libraries
import pandas as pd  # Import pandas library and alias it as 'pd'
import time          # Import the 'time' module (not used in this script)

# Read data from a CSV file into a DataFrame
df = pd.read_csv("../FullDataPohyby.csv", index_col=0)

# Enumerate column names and print them with their indices
for idx, column_name in enumerate(df.columns):
    print(f"Column Name: '{column_name}', Index: {idx}")

# Initialize variables
count = 1
timestamp = 0
pwr = 0
cpwr = 0

# Create new columns in the DataFrame using 'shift' method
df['next_timestamp'] = df['datetime'].shift(-1)
df['TG_next_power'] = df['TG1 - ČINNÝ VÝKON'].shift(-1)
df['TG1_next_value'] = df['TG1_movement'].shift(-1)

# Initialize an empty list for storing results
Cntr = []

# Iterate through rows of the DataFrame
for index, row in df.iterrows():
    TG1_pohyb = row['TG1_movement']
    PTG1_pohyb = row['TG1_next_value']

    # Check if the current 'TG1_movement' value matches the next one
    if TG1_pohyb == PTG1_pohyb:
        if timestamp == 0:
            timestamp = row['datetime']
            pwr = row['TG1 - ČINNÝ VÝKON']
            frow = index

        count += 1
    else:
        if timestamp != 0:
            timestamp2 = row['datetime']
            cpwr = row['TG1 - ČINNÝ VÝKON']
            lrow = index
            print(f'frow {frow} nad lrow {lrow}')
            selected_rows = df.loc[frow:lrow]
            PWR_mean = selected_rows["TG1 - ČINNÝ VÝKON"].mean()
            VIB_mean = selected_rows["TG1 - VIBRACE VLT"].mean()
            PWR_max = selected_rows["TG1 - ČINNÝ VÝKON"].max()
            PWR_min = selected_rows["TG1 - ČINNÝ VÝKON"].min()

            # Append a dictionary with calculated statistics to 'Cntr' list
            Cntr.append({"Timestamp": timestamp, "LTimestamp": timestamp2, "Count": count, "Pohyb": TG1_pohyb, "Počáteční výkon": pwr, "Konečný výkon": cpwr, "Průměr Výkonu": PWR_mean, "Průměr vibrací VLT": VIB_mean, "MAX Výkon": PWR_max, "MIN Výkon": PWR_min})
            count = 1
            timestamp = 0
            selected_values = []
        else:
            timestamp = row['datetime']
            pwr = row['TG1 - ČINNÝ VÝKON']

            # Append a dictionary with 'NA' values when 'timestamp' is 0
            Cntr.append({"Timestamp": timestamp, "LTimestamp": timestamp, "Count": count, "Pohyb": TG1_pohyb, "Počáteční výkon": pwr, "Konečný výkon": pwr, "Průměr Výkonu": "NA", "Průměr vibrací VLT": "NA"})
            timestamp = 0
            count = 1

# Create a new DataFrame from the list of dictionaries
output_df = pd.DataFrame(Cntr)

# Write the new DataFrame to a CSV file without including the index column
output_df.to_csv("FinalResults_TG1.csv", index=False)
