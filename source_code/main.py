from source_code.model.model import Model
from source_code.training.train import train_model, evaluate_model
from source_code.data_processing.process_data import preprocess_data
from source_code.utils.utils import split_dataset

EPOCHS = 100
CSV_PATH = "data/data.csv"

if __name__ == "__main__":
    
    model = Model(num_weights=2)

    features, labels = preprocess_data(CSV_PATH)
    trainset, train_label, testset, test_label = split_dataset(features, labels)

    for epoch in range(EPOCHS):
        train_loss, model = train_model(trainset, train_label, model)
        accuracy, test_loss = evaluate_model(testset, test_label, model)

        print(f"Epoch: {epoch+1} | Train Loss: {train_loss:.4f} | Validation Loss: {test_loss:.4f} | Accuracy: {accuracy:.2f}")