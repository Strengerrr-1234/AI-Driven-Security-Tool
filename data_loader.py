import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Load and preprocess the data from a CSV file.
    """
    data = pd.read_csv(file_path)
    X = data.drop(columns=['threat_level'])  # Drop the target column
    y = data['threat_level']  # Use 'threat_level' as the target column
    
    # Encode target labels (malicious=1, benign=0)
    y = y.map({'benign': 0, 'malicious': 1})
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Standardize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test
