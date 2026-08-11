import math

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

def dloss_dbias(prediction, actual_value):
    dL_dp = dloss_dprediction(prediction, actual_value)
    dp_dz = dprediction_dz(prediction)
    dz_db = 1

    dl_db = dL_dp * dp_dz * dz_db

    assert math.isclose(
        dl_db,
        (prediction-actual_value),
        rel_tol=1e-9
    )

    return dl_db

def update_weight(gradient_val, lr, model, i):
    model.weights[i] -= (lr * gradient_val)

def update_bias(bias_val, lr, model):
    model.bias -= (lr * bias_val)