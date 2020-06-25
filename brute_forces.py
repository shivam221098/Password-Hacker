import socket
import sys
import itertools as it
import string
 
guessing_letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
args = sys.argv
my_socket = socket.socket()
my_socket.connect((args[1], int(args[2])))
 
 
def password_guess():
    global guessing_letters
    length = 1
    flag = 0
    response = ""
    while response != "Connection success!":
        for guess in it.product(guessing_letters, repeat=length):
            guess = "".join(guess)
            my_socket.send(guess.encode())
            response = my_socket.recv(1024)
            if response.decode() == "Connection success!":
                print(guess)
                flag = 1
                break
        if flag == 1:
            exit(0)
        length += 1
 
 
password_guess()
my_socket.close()
