import time
import psutil
import argparse
import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok= True)
CSV_FILE = DATA_DIR / "data.csv"


def main(target_pid: int):
    """the entry point to the code"""

    data_dict = {
        "family": [],
        "type": [],
        "local_ip": [],
        "local_port": [],
        "remote_ip": [],
        "remote_port": [],
        "status": [],
        "label": []
    }

    deduplication_set = set()

    while psutil.pid_exists(target_pid):
        process = psutil.Process(target_pid)
        target_conn = process.net_connections(kind="tcp")
        for conn in target_conn:
            local_ip = getattr(conn.laddr, "ip", "None")
            local_port = getattr(conn.laddr, "port", "None")

            remote_ip = getattr(conn.raddr, "ip", "None")
            remote_port = getattr(conn.raddr, "port", "None")

            net = f"{local_ip}-{local_port}:{remote_ip}-{remote_port}"

            if net not in deduplication_set:

                data_dict["family"].append(conn.family)
                data_dict["type"].append(conn.type)

                data_dict["local_ip"].append(local_ip if local_ip != "::" else "None")
                data_dict["local_port"].append(local_port)

                data_dict["remote_ip"].append(remote_ip if remote_ip != "::" else "None")
                data_dict["remote_port"].append(remote_port)

                data_dict["status"].append(conn.status)
                deduplication_set.add(net)

                data_dict["label"].append(1 if remote_port in [4444, 31337, 9999, 1337] else 0)

        time.sleep(0.1)

    data_csv = pd.DataFrame(data_dict)
    data_csv.to_csv(CSV_FILE, index=False)

    print(f"There is {len(deduplication_set)} unique connections")
    print(f"The generated Data is at: {CSV_FILE}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the PID for Automation")
    parser.add_argument("--pid", type=int, required=True, help="The PID of the scripts/system you wnat to monitor")
    args = parser.parse_args()
    main(target_pid=args.pid)