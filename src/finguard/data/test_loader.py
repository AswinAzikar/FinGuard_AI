from finguard.data.loader import load_data

df = load_data("data/raw/creditcard.csv")
print( f"Data loaded successfully. Shape: {df.shape}")


print(df.head())


