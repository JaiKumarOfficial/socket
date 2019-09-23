'''
BASIC SOCKET LOGIC :
    1. CREATE SOCKET
        2. BIND IP AND PORT WITH SOCKET
            3. LISTEN FOR SOCKET REQ
                4. ACCEPT SOCKET REQ
                    5. CLOSE SOCKET
'''

import socket, sys


# creating socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as error:
        print("create_socket error : " + str(error))


# binding and listening
def bind_socket():
    try:
        print("Binding port : " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as error:
        print("bind_socket error : " + str(error) + "\n" + "Retrying....")
        bind_socket()


# accepting req
def accept_socket():
    try:
        con, address = s.accept()
        print("connection established | ip: " + str(address[0]) + " | port : " + str(address[1]))
        send_commands(con)
        con.close()
    except socket.error as error:
        print("accept_socket error : " + str(error))


def send_commands(con):
    while True:
        try:
            cmd = input()
            print("command:", cmd)
            if cmd == 'quit':
                print("in if")
                con.close()
                s.close()
                sys.exit()
            elif len(str.encode(cmd)) > 0:
                con.send(str.encode(cmd))
                response = str(con.recv(1024), "utf-8")
                print(response, end="")
        except BaseException as e:
            print(e)



def main():
    create_socket()
    bind_socket()
    accept_socket()


main()