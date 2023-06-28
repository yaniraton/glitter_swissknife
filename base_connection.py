import socket
from datetime import datetime


SERVER_IP = "54.187.16.171"
SERVER_PORT = 1336
login_sting = '100#{gli&&er}{"user_name":"_name_","password":"_pass_","enable_push_notifications":true}##'
checksum_string = '110#{gli&&er}sum##'
fetch_string = '310#{gli&&er}userid##'
load_string = '440#{gli&&er}userid##'

# global variables
username = 'yanir'
password = 'aton'


def get_user_data_from_authentication(message):
    """
    get the user id and username  from the authentication message
    :param message: the authentication message
    :return: the user id and username
    """
    user_id = message.split('"id":')[1].split(',')[0]
    user_screen_name = message.split('"screen_name":"')[1].split('"')[0]
    avatar = message.split('"avatar":"')[1].split('"')[0]
    return user_id, user_screen_name, avatar


def ascii_checksum(string):
    """
    calculates the checksum of a string
    :param string: the string to calculate the checksum of
    :return: the checksum of the string
    """
    checksum = 0
    for i in string:
        checksum += ord(i)
    return checksum


def initialize_connection():
    """
    initialize the connection to the server
    :return: the connection to the server(socket)
    """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to server
    server_address = (SERVER_IP, SERVER_PORT)
    sock.connect(server_address)
    return sock


def login_string(user_name, password):
    """
    create the login string
    :param user_name: the username to login with
    :param password: the password to login with
    :return: the login string
    """
    msg = login_sting.replace('_name_', user_name)
    msg = msg.replace('_pass_', password)
    return msg


def login(sock, user_name, password):
    """
    login to the server
    :param sock: the connection to the server(socket)
    :param user_name: the username to log in with
    :param password: the password to log in with
    :return: None
    """

    # send login message
    sock.sendall(login_string(user_name, password).encode())

    # Receive data
    sock.recv(1024).decode()

    # send checksum message
    checksum = ascii_checksum(user_name + password)
    msg = checksum_string.replace('sum', str(checksum))
    sock.sendall(msg.encode())

    # Receive data and save for the user id
    server_msg = sock.recv(1024).decode()

    # get the user id from the authentication message
    user_id, screen_name, avatar = get_user_data_from_authentication(server_msg)

    # add the user id to the fetch and load messages
    msg = fetch_string.replace('userid', user_id)
    sock.sendall(msg.encode())

    # Receive data
    sock.recv(1024).decode()

    # send checksum message
    msg = load_string.replace('userid', user_id)
    sock.sendall(msg.encode())

    # Receive data
    sock.recv(1024).decode()

    # print that we logged in successfully in green
    print("\033[32mlogin to server successful\n \033[0m")

    # print user id and screen name in cyan
    print("\033[36muser id: " + user_id + "\nuser screen name: " + screen_name + "\n\033[0m\n")
    return user_id, screen_name, avatar


def get_current_time_post_format():
    """
    get the current time in the format that the server expects
    :return: the current time in the format that the server expects
    """
    current_time = datetime.utcnow().isoformat() + 'Z'
    return current_time


def get_current_time_regular_format():
    """
    get the current time in the regular format that the server show to the user
    :return: the current time in the regular format that the server show to the user
    """
    current_time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
    return current_time


def send_message(sock, message):
    sock.sendall(message.encode())
    return sock.recv(1024).decode()
