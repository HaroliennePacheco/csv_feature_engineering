import pandas as pd

def encode_categorical_features(df):
    # Encode Gender column: Male = 1, Female = 0
    df['Gender_Encoded'] = df['Gender'].map({
        'Male': 1,
        'Female': 0
    })
    return df
  
if __name__ == "__main__":
    df = pd.read_csv("input/data.csv")
    df = encode_categorical_features(df)

    df.to_csv("output/encode_categorical_features.csv", index=False)
    print("encode_categorical_features done")
