from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(X_train, y_train):
    """
    Train a machine learning model using RandomForestClassifier.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model using test data.
    """
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    return report
