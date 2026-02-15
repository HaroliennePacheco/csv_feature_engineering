import pandas as pd

def time_based_feature_extraction(df):
    # Convert Date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Extract Year, Month, and Day
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    # Extract Day Name (Monday, Tuesday, etc.)
    df['Day_Name'] = df['Date'].dt.day_name()

    return df

if __name__ == "__main__":
    df = pd.read_csv("input/data.csv")
    df = time_based_feature_extraction(df)

    df.to_csv("output/time_based_feature_extraction.csv", index=False)
    print("time_based_feature_extraction done")
