import os
import time
import socket
import random
import requests


def gen_fake_ip():
    """For generating Fake IP Address for Malicious Connection"""
    ip = []
    for _ in range(4):
        ip.append(str(random.randint(1, 255)))
    return ".".join(ip)


def gen_fake_port(ports: list = [4444, 31337, 9999, 1337]):
    """For generating Fake Port"""
    return random.choices(ports)[0]


def connect_real_url(url):
    """Create a connection to legit website"""
    try:
        r = requests.get(url, timeout=1.0)
        print(f"Connection is made to {r.url}")
        if r.status_code != 200:
            print(f"Problem with the connection {r.status_code}")
    except Exception as e:
        print("Got this problem while solving: ", e)


def make_safe_conn(safe_web: str):
    """Real website connection for class 0"""
    with open(safe_web, 'r') as file:
        web_list = file.readlines()
    
    web_addr = random.choice(web_list).strip()
    connect_real_url(web_addr)
    time.sleep(random.randint(2, 5))


def make_fake_conn():
    """Fake Connection for class 1"""
    fake_ip = gen_fake_ip()
    fake_port = gen_fake_port()

    print(f"Random Fake IP: {fake_ip} | Random Fake Port: {fake_port}")

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1.0)
        client.connect((fake_ip, fake_port))
    except Exception as e:
        print("Got this Problem: ", e)
    finally:
        client.close()
    return 1


if __name__ == "__main__":
    pid = os.getpid()
    print("The PID of this script is: ", pid)

    time.sleep(5)
    conn_num = 100

    for _ in range(conn_num):
        choice_func = random.choice([0, 1])
        if choice_func == 0:
            make_safe_conn("./data/safe_webaddress.txt")
        else:
            make_fake_conn()