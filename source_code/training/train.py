import logging

from source_code.training.loss import loss
from source_code.training.optimizer import update_weight, update_bias
from source_code.utils.utils import Accuracy
from source_code.training.back_propagation import compute_weight_gradient, compute_bias_gradient

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

def train_model(trainset, train_label, model, lr=0.1):
    full_loss = 0.0
    full_acc = 0.0

    for x, y in zip(trainset, train_label):
        prediction = model.forward(x)
        loss_value = loss(prediction, y)
        # acc = Accuracy(prediction, y)
        
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

        full_loss += loss_value
        # full_acc += acc

    # full_loss /= len(train_label)
    full_loss /= len(train_label)

    return full_loss, model


def evaluate_model(test_feature, test_labels, model):
    full_pass_loss = 0.0
    full_pass_acc = 0.0

    for x, y in zip(test_feature, test_labels):
        predictions = model.forward(x) 
        acc = Accuracy(predictions, y)
        loss_value = loss(predictions, y)

        full_pass_acc += acc
        full_pass_loss += loss_value

    full_pass_acc /= len(test_labels)
    full_pass_loss /= len(test_labels)

    return full_pass_acc, full_pass_loss

