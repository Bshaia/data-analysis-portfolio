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
