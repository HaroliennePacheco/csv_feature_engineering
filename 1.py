import pandas as pd

def derive_computed_columns(df):
    df['Total'] = df['Price'] * df['Quantity']
    return df

if __name__ == "__main__":
    df = pd.read_csv("input/data.csv")
    df = derive_computed_columns(df)
    df.to_csv("output/derive_computed_columns.csv", index=False)
    print("derive_computed_columns done")
