import logging

from source_code.training.loss import loss
from source_code.data_processing.process_data import preprocess_data
from source_code.training.optimizer import update_weight, update_bias
from source_code.utils.utils import Accuracy
from source_code.training.back_propagation import compute_weight_gradient, compute_bias_gradient

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

def train_model(csv_path: str, model, epochs=10, lr=0.1):
    features, labels = preprocess_data(csv_path)

    for epoch in range(epochs):
        epoch_loss = 0.0
        epoch_acc = 0

        for x, y in zip(features, labels):
            prediction = model.forward(x)
            loss_value = loss(prediction, y)
            acc = Accuracy(prediction, y)
            
            logging.debug(f"Actual Class: {y} | Prediction: {prediction:.4f} | Loss: {loss_value:.4f}")

            for idx, feature in enumerate(x):
                logging.debug(f"Model Weights_{idx} Before : {model.weights[idx]}")
                weight_val = compute_weight_gradient(prediction, y, feature)

                logging.debug(f"new weight computed gradient: {weight_val}")

                update_weight(weight_val, lr, model, idx)
                logging.debug(f"Model Weights_{idx} After : {model.weights[idx]}")

            logging.debug(f"Model Bias Before: {model.bias}")
            bias_val = compute_bias_gradient(prediction, y)

            update_bias(bias_val, lr, model)
            logging.debug(f"Model Bias After: {model.bias}")

            epoch_loss += loss_value
            epoch_acc += acc

        epoch_loss /= len(features)
        epoch_acc /= len(features)
        logging.info(f"Epoch: {epoch+1} | Avg.loss: {epoch_loss:.4f} | Accuracy: {epoch_acc:.2f}")
