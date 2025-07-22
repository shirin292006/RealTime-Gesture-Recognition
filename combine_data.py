import pandas as pd
import os

# Path to the gesture_data folder
data_folder = 'gesture_data'

# Output file path
combined_file = os.path.join(data_folder, 'combined_data.csv')

# List all .csv files in the folder
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv') and f.startswith('data_')]

# List to hold all DataFrames
all_data = []

# Combine each CSV with a new 'label' column
for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    
    # Extract label from filename, e.g., "call_me" from "data_call_me.csv"
    label = file.replace('data_', '').replace('.csv', '')
    df['label'] = label
    
    all_data.append(df)

# Concatenate all dataframes
combined_df = pd.concat(all_data, ignore_index=True)

# Save to new CSV
combined_df.to_csv(combined_file, index=False)

print(f"✅ Combined data saved to: {combined_file}")
