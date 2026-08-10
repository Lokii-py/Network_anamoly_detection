from source_code.utils.utils import load_data

def preprocess_data(csv_path: str):
    """Take the feature from CSV that is going to model and Normalize them"""
    data = load_data(csv_path)

    remote_ports = data["remote_port"]
    statuses = data["status"]
    labels = data["label"]

    # Normalized the statuses and ports to a range that model can accept
    encoded_statuses = statuses.map({"SYN_SENT" : 0, "ESTABLISHED": 1, "CLOSE_WAIT": 2})
    normalized_ports = round((remote_ports / 65535), 4)

    y = labels.tolist()
    X = []
    for status, port in zip(encoded_statuses, normalized_ports):
        X.append([status, port])

    return X, y