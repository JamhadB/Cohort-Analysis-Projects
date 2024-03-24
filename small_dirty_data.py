import pandas as pd
import numpy as np

# Create the dirty dataset
data = {
    'User ID': range(1, 19),
    'Cohort Group': ['2022-01', '2022-01', '2022-01',
                     '2022-02', '2022-02', '2022-02',
                     '2022-03', '2022-03', '2022-03',
                     '2022-04', '2022-04', '2022-04',
                     '2022-05', '2022-05', '2022-05',
                     '2022-06', '2022-06', '2022-06'],
    'Date': ['2022-01-01', '2022-01-03', '2022-01-05',
             '2022-02-01', '2022-02-03', '2022-02-05',
             '2022-03-01', '2022-03-03', '2022-03-05',
             '2022-04-01', '2022-04-03', '2022-04-05',
             '2022-05-01', '2022-05-03', '2022-05-05',
             '2022-06-01', '2022-06-03', '2022-06-05'],
    'Revenue': ['$50.00', '$30.00', '$20.00',
                '$40.00', '$25.00', '$35.00',
                '$60.00', '$45.00', '$55.00',
                '$70.00', '$90.00', '$80.00',
                np.nan, '$75.00', '$85.00',
                '$60.00', '$45.00', '$55.00']
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to CSV
df.to_csv('dirty_cohort_data.csv', index=False)
