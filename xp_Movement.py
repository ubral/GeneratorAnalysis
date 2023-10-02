# Import necessary libraries
import pandas as pd  # Import pandas library and alias it as 'pd'
import numpy as np   # Import numpy library and alias it as 'np'

# Read data from a CSV file into a DataFrame
df = pd.read_csv("../FullData.csv", index_col=0)

# Shift the 'value' column by 1 to create a 'previous_value' column
df['TG1_previous_value'] = df['TG1 - ČINNÝ VÝKON'].shift(1)
df['TG2_previous_value'] = df['TG2 - ČINNÝ VÝKON'].shift(1)
df['TG3_previous_value'] = df['TG3 - ČINNÝ VÝKON'].shift(1)

# Create new columns to track movement ('up', 'down', 'flat', 'off')
df['TG1_movement'] = 'flat'  # Initialize with 'flat'
df['TG2_movement'] = 'flat'  # Initialize with 'flat'
df['TG3_movement'] = 'flat'  # Initialize with 'flat'

# Define movement conditions for TG1
df.loc[df['TG1 - ČINNÝ VÝKON'] > df['TG1_previous_value'], 'TG1_movement'] = 'up'
df.loc[df['TG1 - ČINNÝ VÝKON'] < df['TG1_previous_value'], 'TG1_movement'] = 'down'
flat_condition = np.abs(np.abs(df['TG1 - ČINNÝ VÝKON']) - np.abs(df['TG1_previous_value'])) < np.abs(df['TG1_previous_value']) * 0.05
df.loc[flat_condition, 'TG1_movement'] = 'flat'
df.loc[df['TG1 - ČINNÝ VÝKON'] < 0.5, 'TG1_movement'] = 'off'

# Define movement conditions for TG2
df.loc[df['TG2 - ČINNÝ VÝKON'] > df['TG2_previous_value'], 'TG2_movement'] = 'up'
df.loc[df['TG2 - ČINNÝ VÝKON'] < df['TG2_previous_value'], 'TG2_movement'] = 'down'
flat_condition = np.abs(np.abs(df['TG2 - ČINNÝ VÝKON']) - np.abs(df['TG2_previous_value'])) < np.abs(df['TG2_previous_value']) * 0.05
df.loc[flat_condition, 'TG2_movement'] = 'flat'
df.loc[df['TG2 - ČINNÝ VÝKON'] < 0.5, 'TG2_movement'] = 'off'

# Define movement conditions for TG3
df.loc[df['TG3 - ČINNÝ VÝKON'] > df['TG3_previous_value'], 'TG3_movement'] = 'up'
df.loc[df['TG3 - ČINNÝ VÝKON'] < df['TG3_previous_value'], 'TG3_movement'] = 'down'
flat_condition = np.abs(np.abs(df['TG3 - ČINNÝ VÝKON']) - np.abs(df['TG3_previous_value'])) < np.abs(df['TG3_previous_value']) * 0.05
df.loc[flat_condition, 'TG3_movement'] = 'flat'
df.loc[df['TG3 - ČINNÝ VÝKON'] < 0.5, 'TG3_movement'] = 'off'

# Write the DataFrame to a CSV file
df.to_csv("FullDataPohyby.csv")
