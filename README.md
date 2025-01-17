# AI-driven Security tool
Your **AI-driven cybersecurity tool** is a Python-based program designed to detect threats using machine learning. The key features of this project are:

## Key Features

1. ### Machine Learning Model:
    * Uses the `RandomForestClassifier` from **scikit-learn** for classification.
    * Detects whether network traffic is **benign** or **malicious** based on features such as IP reputation, packet size, time-to-live, and more.
2. ### Modular Programming:
    * The project is divided into multiple modules for better organization and maintainability:
         * `data_loader.py`: Responsible for loading and preprocessing the dataset.
         * `model_trainer.py`: Handles training and evaluation of the machine learning model.
         * `main.py`: The entry point that ties everything together.
3. ### Dataset:
    A synthetic dataset (`cybersecurity_data.csv`) with features like IP reputation, packet size, and flags. The target column, **threat_level**, is labeled as either "benign" or "malicious."
4. ### Steps in the Program:
    * **Load Data**: Reads and preprocesses the dataset (splits into train and test sets, standardizes features).
    * **Train Model**: Builds and trains a RandomForest model using the training data.
    * **Evaluate Model**: Tests the model on unseen data and generates a classification report.
5. ### Output:
    A detailed report showing precision, recall, F1-score, and accuracy for the model.


## How the Tool Works

1. ### Input:
    * A CSV file containing network metrics (`cybersecurity_data.csv`).
    * Each row represents a network event with features and a label (`benign` or `malicious`).
      
2. ### Processing: 
  * The `data_loader.py` module reads and preprocesses the input data, encoding labels and splitting it into training and testing datasets.
  * The `model_trainer.py` module trains a RandomForestClassifier on the training data.
  * The `main.py` module evaluates the trained model on the testing data and prints the results.
  
3. ### Output:
  * A summary report of the model’s performance on detecting malicious threats.


## Project Workflow

**Step 1**: Prepare the dataset (`cybersecurity_data.csv`).

**Step 2**: Execute the `main.py` script:
```
python main.py
```
**Step 3**: Review the output, which includes metrics like accuracy, precision, and recall.


## Use Cases
* **Threat Detection**: Identify suspicious network activity or patterns.
* **Network Monitoring**: Provide insights into potential vulnerabilities.
* **Cybersecurity Research**: Serve as a foundation for building more sophisticated threat-detection systems.

This tool is a great starting point for understanding how to apply machine learning to cybersecurity tasks. 
