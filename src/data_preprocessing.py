import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    # Handle missing values
    df.fillna(df.mean(), inplace=True)
    
    # Normalize biomarker levels
    scaler = StandardScaler()
    X = scaler.fit_transform(df.drop('diagnosis', axis=1))
    y = df['diagnosis']  # Binary label (0=healthy, 1=tumor)
    
    return X, y, scaler
