import pandas as pd
import psutil


def extract_network_info():
    """returns back port and other network info for creating the dataset"""
    net_info = psutil.net_connections(kind="tcp")
    return net_info


def main(time):
    """the entry point to the code"""
    data_dict = {
        "family": [],
        "type": [],
        "local_ip": [],
        "local_port": [],
        "remote_ip": [],
        "remote_port": [],
        "status": []
    }
    print(f"running until {time} times")
    for _ in range(time):
        data = extract_network_info()
        for item in data:
            data_dict["family"].append(item.family)
            data_dict["type"].append(item.type)

            local_ip = getattr(item.laddr, "ip", "None")
            data_dict["local_ip"].append(local_ip if local_ip != "::" else "None")
            data_dict["local_port"].append(getattr(item.laddr, "port", "None"))

            remote_ip = getattr(item.raddr, "ip", "None")
            data_dict["remote_ip"].append(remote_ip if remote_ip != "::" else "None")
            data_dict["remote_port"].append(getattr(item.raddr, "port", "None"))

            data_dict["status"].append(item.status)

    data_csv = pd.DataFrame(data_dict)
    data_csv.to_csv("./data.csv", index=False)


if __name__ == "__main__":
    main(10)