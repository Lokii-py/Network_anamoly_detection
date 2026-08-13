from source_code.model.model import Model
from source_code.training.training import train_model


if __name__ == "__main__":

    model = Model(num_weights=2)
    train_model("data/data.csv", model)