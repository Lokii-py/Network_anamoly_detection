import pandas as pd


def load_data(csv_path: str, view_head=False):
    try:
        data = pd.read_csv(csv_path)
        if data is not None:
            if view_head:
                print(f"\n{'='* 100}\n")
                print(data.head(5))
                print(f"\n{'='* 100}\n")
                print(data.tail(5), "\n")
            return data
        else:
            print("Nothing in csv file")
            return None
    except:
        raise FileNotFoundError("Faulty CSV path")


def clip_probablity(num):
    eps = 1e-9
    num = max(min(num, 1-eps), eps)
    return num