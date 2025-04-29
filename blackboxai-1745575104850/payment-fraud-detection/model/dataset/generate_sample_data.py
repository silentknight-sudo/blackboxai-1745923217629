import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate 100 samples
n_samples = 100

# Generate Time feature (seconds from start of day)
start_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
times = np.sort(np.random.randint(0, 86400, n_samples))  # seconds in a day

# Generate Amount (transaction amounts between $1 and $5000)
amounts = np.random.uniform(1, 5000, n_samples)

# Generate V1-V28 (normally distributed features)
v_features = np.random.normal(0, 1, (n_samples, 28))

# Generate Class (fraud = 1, non-fraud = 0)
# Make 5% of transactions fraudulent
n_fraud = int(n_samples * 0.05)
classes = np.zeros(n_samples)
fraud_indices = np.random.choice(n_samples, n_fraud, replace=False)
classes[fraud_indices] = 1

# Create DataFrame
data = pd.DataFrame()
data['Time'] = times
data['Amount'] = amounts
for i in range(28):
    data[f'V{i+1}'] = v_features[:, i]
data['Class'] = classes

# Save to CSV
data.to_csv('creditcard.csv', index=False)
print("Sample dataset generated successfully!")
