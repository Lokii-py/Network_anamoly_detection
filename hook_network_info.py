import os
import time
import psutil

import pandas as pd


def extract_network_info():
    """returns back port and other network info for creating the dataset"""
    net_info = psutil.net_connections(kind="tcp")
    return net_info


def main(datapoints: int, target_pid: int):
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

    deduplication_set = set()
    print(f"[info] Running this script until {datapoints} datapoints")

    while datapoints > len(deduplication_set):
        data = extract_network_info()
        for item in data:
            if item.pid == target_pid:
                local_ip = getattr(item.laddr, "ip", "None")
                local_port = getattr(item.laddr, "port", "None")

                remote_ip = getattr(item.raddr, "ip", "None")
                remote_port = getattr(item.raddr, "port", "None")

                net = f"{local_ip}-{local_port}:{remote_ip}-{remote_port}"

                if net not in deduplication_set:

                    data_dict["family"].append(item.family)
                    data_dict["type"].append(item.type)

                    data_dict["local_ip"].append(local_ip if local_ip != "::" else "None")
                    data_dict["local_port"].append(local_port)

                    data_dict["remote_ip"].append(remote_ip if remote_ip != "::" else "None")
                    data_dict["remote_port"].append(remote_port)

                    data_dict["status"].append(item.status)
                    deduplication_set.add(net)


        time.sleep(1.0)

    data_csv = pd.DataFrame(data_dict)
    data_path = "./data.csv"
    data_csv.to_csv(data_path, index=False)

    print(f"[Into] There is {len(deduplication_set)} unique connections")
    print(f"[Info] The generated Data is at: {data_path}")


if __name__ == "__main__":
    pid = os.getpid()
    print(f"[info] The PID of this script is {pid}")
    main(datapoints=10, target_pid=pid)