import pandas as pd

def bin_numeric_ranges(df):
    # Bin Age into categories
    df['Age_Group'] = pd.cut(
        df['Age'],
        bins=[0, 18, 60, 100],
        labels=['Teen', 'Adult', 'Senior']
    )

    # Bin Price into categories
    df['Price_Range'] = pd.cut(
        df['Price'],
        bins=[0, 50, 150, 300],
        labels=['Low', 'Medium', 'High']
    )

    return df

if __name__ == "__main__":
    df = pd.read_csv("input/data.csv")
    df = bin_numeric_ranges(df)

    df.to_csv("output/bin_numeric_ranges.csv", index=False)
    print("bin_numeric_ranges done")
