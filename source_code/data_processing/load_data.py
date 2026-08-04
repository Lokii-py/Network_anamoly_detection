from source_code.utils.utils import load_data

def preprocess_csv():
    data = load_data("data/data.csv")

    remote_ports = data["remote_port"]
    statuses = data["status"]
    labels = data["label"]

    # Prep
    encoded_statuses = statuses.map({"SYN_SENT" : 0, "ESTABLISHED": 1, "CLOSE_WAIT": 2})

preprocess_csv()