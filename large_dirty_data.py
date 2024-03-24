import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate random dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Generate 100,000 observations
start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 12, 31)

data = {
    'User ID': range(1, 100001),
    'Cohort Group': [random_date(start_date, end_date).strftime('%Y-%m') for _ in range(100000)],
    'Date': [random_date(start_date, end_date).strftime('%Y-%m-%d') for _ in range(100000)],
    'Revenue': [f'${random.uniform(10, 1000):.2f}' for _ in range(100000)]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to CSV
df.to_csv('large_dirty_cohort_data.csv', index=False)
