import math
import logging

from source_code.data_processing.process_data import preprocess_data
from source_code.model.model import Model

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s'
)

def loss(p, y):
    penalty = - ((y * math.log(p))+ ((1-y)*(math.log(1-p))))
    return penalty

def train_model(csv_path: str, model):
    X, y = preprocess_data(csv_path)

    for x, y in zip(X, y):
        prediction = model.forward(x)
        loss_value = loss(prediction, y)

        logging.debug(f"Actual Class: {y} | Prediction: {prediction:.4f} | Loss: {loss_value:.4f}")

model = Model(num_weights=2)
train_model("data/data.csv", model)
