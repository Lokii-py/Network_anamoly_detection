import math
import logging

from source_code.data_processing.process_data import preprocess_data
from source_code.model.model import Model
from source_code.training.back_propagation import update_weight, update_bias, dloss_dweight, dloss_dbias

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s'
)

def loss(p, y):
    penalty = - ((y * math.log(p))+ ((1-y)*(math.log(1-p))))
    return penalty

def train_model(csv_path: str, model, lr=0.1):
    X, y = preprocess_data(csv_path)

    for x, y in zip(X, y):
        prediction = model.forward(x)
        loss_value = loss(prediction, y)

        logging.debug(f"Actual Class: {y} | Prediction: {prediction:.4f} | Loss: {loss_value:.4f}")

        for idx, feature in enumerate(x):
            logging.debug(f"Model Weights_{idx} Before : {model.weights[idx]}")
            weight_val = dloss_dweight(prediction, y, feature)

            logging.debug(f"new weight computed gradient: {weight_val}")

            update_weight(weight_val, lr, model, idx)
            logging.debug(f"Model Weights_{idx} After : {model.weights[idx]}")

        logging.debug(f"Model Bias Before: {model.bias}")
        bias_val = dloss_dbias(prediction, y)
        update_bias(bias_val, lr, model)
        logging.debug(f"Model Bias After: {model.bias}")

        break



## Testing

model = Model(num_weights=2)
train_model("data/data.csv", model)
