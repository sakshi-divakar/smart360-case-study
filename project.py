import pandas as pd

# Read consumer data from a CSV file
consumer_data_file = '/content/give in sheet format - give in sheet format.csv'
df_consumer = pd.read_csv(consumer_data_file)

# Map the consumer data to the SMART360 Consumer Table Fields
df_smart360 = df_consumer.rename(columns={
    'Consumer ID': 'Consumer ID',
    'Name': 'First Name',
    'Address': 'Address Line 1',
    'Contact Number': 'Phone Number',
    'Email Address': 'Email Address'
})

df_smart36 = df_consumer[['Consumer ID', 'Name', 'Address', 'Contact Number', 'Email Address']].copy()

df_smart360['Consumer ID'] = df_smart36['Consumer ID']
df_smart360['First Name'] = df_smart36['Name'].str.split(' ').str[-2]
# Extracting Last Name, City, State, and Zip Code from the Address column
df_smart360['Last Name'] = df_smart36['Name'].str.split(' ').str[-1]
df_smart360['City'] = df_smart36['Address'].str.split(' ').str[-2]
df_smart360['State'] = df_smart36['Address'].str.split(' ').str[-1]
df_smart360['Zip Code'] = df_smart36['Address'].str.split().str[-3]
df_smart360['Phone Number'] = df_smart36['Contact Number']
df_smart360['Email Address'] = df_smart36['Email Address']

# Display the mapped data
print(df_smart360)
