import pandas as pd

def time_based_feature_extraction(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['Day_Name'] = df['Date'].dt.day_name()

    return df

if __name__ == "__main__":
    df = pd.read_csv("input/data.csv")
    df = time_based_feature_extraction(df)

    df.to_csv("output/time_based_feature_extraction.csv", index=False)
    print("time_based_feature_extraction done")
