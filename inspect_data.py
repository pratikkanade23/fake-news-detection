import pandas as pd

fake_data = pd.read_csv("data/Fake.csv")
true_data = pd.read_csv("data/True.csv")

print("Fake news articles:", len(fake_data))
print("Real news articles:", len(true_data))

print("\nColumns in Fake.csv:")
print(fake_data.columns)

print("\nColumns in True.csv:")
print(true_data.columns)
print("\nMissing values in Fake.csv:")
print(fake_data.isnull().sum())

print("\nMissing values in True.csv:")
print(true_data.isnull().sum())