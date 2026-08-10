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
    print(X)

    for x, y in zip(X, y):
        prediction = model.forward(x)
        loss_value = loss(prediction, y)

        logging.debug(f"Actual Class: {y} | Prediction: {prediction:.4f} | Loss: {loss_value:.4f}")
        break

def dloss_dprediction(prediction, actual_value):
    """If prediction changes a little bit, how much does the loss changes"""
    return (prediction - actual_value) / (prediction*(1-prediction))

def dprediction_dz(prediction):
    """if the raw value of model changes a little big, how much does the prediction changes"""
    return prediction * (1 - prediction)

def dz_dweight(feature):
    return feature

def dloss_dweight(prediction, actual_value, feature):
    """It comes to (prediction - actual_value) * feature"""
    dL_dp = dloss_dprediction(prediction, actual_value)
    dp_dz = dprediction_dz(prediction)
    dz_dw = dz_dweight(feature)

    dl_dw = dL_dp * dp_dz * dz_dw

    assert math.isclose(
        dl_dw,
        (prediction - actual_value) * feature,
        rel_tol=1e-9
    )

    return dl_dw


## Testing

# val = dloss_dweight(0.8, 1, 0.1526)
# print(val)

# model = Model(num_weights=2)
# train_model("data/data.csv", model)
