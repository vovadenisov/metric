import psutil as psutil
from time import sleep
import socket
import datetime
import time
import requests
from subprocess import call
import os

#perl -e '$| = 1; while() { $d = `uptime`; ($la) = $d =~ /load average: (.*?),/; $c = qq{echo local_local.load_average $la }.time().qq{ | nc localhost 2003}; system($c); print "$c\n"; sleep 1;}'


requests_ = 0
TCP_IP = "95.213.203.218"
TCP_PORT = 2003
#sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
#sock.connect((TCP_IP, TCP_PORT))
while True:
    cpu = psutil.cpu_percent()
    result = requests.get("http://127.0.0.1/nginx_status")
    text_list = result.text.split("\n")
    request_count = int(text_list[2].split(" ")[3])
    rpc = request_count - requests_
    requests_ = request_count
    dt = datetime.datetime.now()
    timestamp = time.mktime(dt.timetuple())
    message = "{0} {1} {2}".format("serverone.cpu", cpu, int(timestamp))
    print "echo {0} | nc {1} {2}".format(message, TCP_IP, TCP_PORT)
    #call(["echo {0} | nc {1} {2}".format(message, TCP_IP, TCP_PORT)])
    #sock.send(message)
    os.system("echo {0} | nc {1} {2}".format(message, TCP_IP, TCP_PORT))
    message = "{0} {1} {2}".format("serverone.rpc", rpc, timestamp)
    os.system("echo {0} | nc {1} {2}".format(message, TCP_IP, TCP_PORT))
    #call(["echo {0} | nc {1} {2}".format(message, TCP_IP, TCP_PORT)])
    #sock.send(message)
    sleep(1)
sock.close()
