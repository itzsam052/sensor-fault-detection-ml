import pandas as pd

df = pd.read_csv("data/sensor_data.csv")

# Create features
df["rolling_mean"] = df["signal"].rolling(window=5).mean()
df["rolling_std"] = df["signal"].rolling(window=5).std()
df["rolling_mean_long"] = df["signal"].rolling(window=20).mean()
df["diff"] = df["signal"].diff()
# Handle missing values
df.fillna(0, inplace=True)

# Save new dataset
df.to_csv("data/processed_data.csv", index=False)

print("Feature engineering completed!")