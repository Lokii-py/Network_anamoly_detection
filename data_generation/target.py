import os
import time
import random
import requests


def make_conn(url):
    try:
        r = requests.get(url, timeout=1.0)
        print(f"Connection is made to {r.url}")
        if r.status_code != 200:
            print(f"Problem with the connection {r.status_code}")
    except Exception as e:
        print("Got this problem while solving: ", e)


def main(safe_web: str):
    with open(safe_web, 'r') as file:
        web_list = file.readlines()

    for _ in range(100):
        web_addr = random.choice(web_list).strip()
        make_conn(web_addr)
        time.sleep(random.randint(2, 5))


if __name__ == "__main__":
    pid = os.getpid()
    print("The PID of this script is: ", pid)
    time.sleep(10)
    main("./data/safe_webaddress.txt")
