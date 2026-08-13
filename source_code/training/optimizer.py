def update_weight(gradient_val, lr, model, i):
    model.weights[i] -= (lr * gradient_val)

def update_bias(bias_val, lr, model):
    model.bias -= (lr * bias_val)