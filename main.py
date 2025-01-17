from data_loader import load_data
from model_trainer import train_model, evaluate_model

def main():
    # Load data
    file_path = "cybersecurity_data.csv"  # Replace with the actual path to your dataset
    X_train, X_test, y_train, y_test = load_data(file_path)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    report = evaluate_model(model, X_test, y_test)
    print("Model Evaluation Report:")
    print(report)

if __name__ == "__main__":
    main()
