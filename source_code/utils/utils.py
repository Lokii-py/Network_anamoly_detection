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


def split_dataset(features: list, labels: list, train_percent: int= 80):
    """
    Splitting Data into train and test set
    TODO: Need to do stratification when splitting fairly
    """
    total_datapoints = len(features)
    assert total_datapoints == len(labels), "Total Datapoints should be equal to total number of labels"
    split_pt = int((train_percent / 100) * total_datapoints)

    trainset = features[:split_pt]
    train_label = labels[:split_pt]

    testset = features[split_pt:]
    test_label = labels[split_pt:]

    return trainset, train_label, testset, test_label

def clip_probablity(num):
    eps = 1e-9
    num = max(min(num, 1-eps), eps)
    return num


def Accuracy(prediction, ground_truth):
    #Convert the raw_prediction to class
    predicted_cls = round(prediction)
    return 1 if predicted_cls == ground_truth else 0