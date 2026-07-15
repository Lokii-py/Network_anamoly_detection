import pandas as pd
import psutil


def extract_network_info():
    """returns back port and other network info for creating the dataset"""
    net_info = psutil.net_connections(kind="tcp")
    return net_info


def main(time):
    """the entry point to the code"""
    data_dict = {
        "fd" : [],
        "family": [],
        "type": [],
        "laddr": [],
        "raddr": [],
        "status": []
    }
    print(f"running until {time} times")
    for _ in range(time):
        data = extract_network_info()
        # print(data)
        # break
        for item in data:
            data_dict["fd"].append(item.fd)
            data_dict["family"].append(item.family)
            data_dict["type"].append(item.type)
            data_dict["laddr"].append(item.laddr)
            data_dict["raddr"].append(item.raddr)
            data_dict["status"].append(item.status)

    data_csv = pd.DataFrame(data_dict)
    data_csv.to_csv("./data.csv", index=False)


if __name__ == "__main__":
    main(10)