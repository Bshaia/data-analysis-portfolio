# generate_data.py
# Author: Brett Shaia
# Description: Generate synthetic data for a nonprofit org - donors and donations

import pandas as pd 
import numpy as np 
from faker import Faker 
import random 

fake = Faker()

# Generate donor data
num_doners = 300

donors = pd.DataFrame({
    "donor_id": range(1, num_doners + 1),
    "name": [fake.name() for _ in range(num_doners)],
    "email": [fake.email() for _ in range(num_doners)],
    "join_date": [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_doners)]
})

print(donors.head())

# Generate donation records
num_donations = 1200
donation_records = []

for _ in range(num_donations):
    donor= donors.sample(1).iloc[0]
    amount = round(random.uniform(10, 1000), 2)
    donation_date = fake.date_between(start_date=donor["join_date"], end_date='today')
    donation_records.append((donor["donor_id"], donation_date, amount))

donations = pd.DataFrame(donation_records, columns=["donor_id", "donation_date", "amount"])
print(donations.head())

# Save to CSV 
donors.to_csv("../data/donors.csv", index=False)
donations.to_csv("../data/donations.csv", index=False)
print("CSV files saved to /data folder.")