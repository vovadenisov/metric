import psutil as psutil
from time import sleep
import socket
import datetime
import time
import requests


requests_ = 0
while True:
    cpu = psutil.cpu_percent()
    result = requests.get("http://127.0.0.1/nginx_status")
    text_list = result.text.split("\n")
    request_count = int(text_list[3].split(" ")[3])
    rpc = request_count - requests_
    requests_ = request_count
    dt = datetime.datetime.now()
    timestamp = time.mktime(dt.timetuple())
    udp_ip = "95.213.251.22"
    udp_port = 2003
    message = "{0} {1} {2}".format("server_1.cpu", cpu, timestamp)
    sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    sock.sendto(message, (udp_ip, udp_port))
    message = "{0} {1} {2}".format("server_1.rpc", rpc, timestamp)
    sock.sendto(message, (udp_ip, udp_port))
    sleep(1)