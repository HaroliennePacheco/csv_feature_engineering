import pandas as pd

def flag_anomalies_column(df):
    # Basic anomaly rules
    df['Anomaly'] = 0

    df.loc[df['Price'] <= 0, 'Anomaly'] = 1
    df.loc[df['Quantity'] <= 0, 'Anomaly'] = 1
    df.loc[(df['Age'] < 0) | (df['Age'] > 100), 'Anomaly'] = 1

    # Statistical anomaly detection for Price (outlier detection)
    mean_price = df['Price'].mean()
    std_price = df['Price'].std()

    threshold = mean_price + (2 * std_price)
    df.loc[df['Price'] > threshold, 'Anomaly'] = 1

    return df

if __name__ == "__main__":
    df = pd.read_csv("input/data.csv")
    df = flag_anomalies_column(df)

    df.to_csv("output/flag_anomalies_column.csv", index=False)
    print("flag_anomalies_column done")
