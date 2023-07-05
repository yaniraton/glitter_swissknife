# this file will contain all the functions that has
# a connection with the glitter and will be used as an api in the swissknife.py file
import hashlib
import socket
import requests
from datetime import datetime

APP_SERVER_IP = "54.187.16.171"
APP_SERVER_PORT = 1336
APP_LOGIN_STRING = '100#{gli&&er}{"user_name":"_name_","password":"_pass_","enable_push_notifications":true}##'
APP_CHECKSUM_STRING = '110#{gli&&er}_sum_##'
APP_FETCH_STRING = '310#{gli&&er}_userid_##'
APP_LOAD_STRING = '440#{gli&&er}_userid_##'
APP_LIKE_GLIT_STRING = '710#{gli&&er}{"glit_id":_glit_id_,"user_id":_user_id_,' \
                       '"user_screen_name":"_user_screen_name_","id":-1}##'
APP_DISLIKE_STRING = '720#{gli&&er}_ID_##'
COMMENT_GLIT_STRING = '650#{gli&&er}{"glit_id":_glit_id_,"user_id":_user_id_,"user_screen_name":"_user_screen_name_",' \
                      '"id":-1,"content":"_content_","date":"_date_"}##'
TIME_SEND_EXAMPLE = '2020-01-01T00:00:00Z'
NONEXISTENT_ID = '1000000000'
POST_GLIT_STRING = '550#{gli&&er}{"feed_owner_id":_feed_owner_id_,"publisher_id":_publisher_id_,' \
                   '"publisher_screen_name":"_publisher_screen_name_","publisher_avatar":"_publisher_avatar_",' \
                   '"background_color":"_background_color_","date":"_date_","content":"_content_",' \
                   '"font_color":"_font_color_","id":-1}##'
SEARCH_STRING = '300#{gli&&er}{"search_type":"_search_type_","search_entry":"_search_entry_"}##'
APP_FEED_LOAD_STRING = '500#{gli&&er}{"feed_owner_id":_feed_owner_id_,"end_date":"_end_date_",' \
                       '"glit_count":_glit_count_}##'
APP_LOGOUT_STRING = '200#{gli&&er}_user_id_##'
APP_CHANGE_USER_INFO = '350#{gli&&er}{"screen_name":"_screen_name_","avatar":"_avatar_",' \
                       '"description":"_description_","privacy":"_privacy_","id":_id_,"user_name":"_user_name_",' \
                       '"password":"_password_","gender":"_gender_","mail":"_mail_"}##'
APP_GLANCE_REQUEST_STRING = '410#{gli&&er}[_user_sending_,_user_to_send_]##'
APP_REFUSE_GLANCE_REQUEST_STRING = '430#{gli&&er}[_user_sending_,_user_to_send_]##'
WEB_CREATE_PASSWORD_RECOVERY_URL = 'http://cyber.glitter.org.il/password-recovery-code-request/'
WEB_GET_PASSWORD_RECOVERY_CODE = 'http://cyber.glitter.org.il/password-recovery-code-verification/'
APP_GET_USER_SEARCH_HISTORY = '320#{gli&&er}_user_id_##'
NUM_OF_LIKES = 3
SUCCESS = True
FAILURE = False
XSS_EXAMPLE = "<img src='https://www.shutterstock.com/image-vector/hi-sticker-social-media-content" \
              "-260nw-1138004576.jpg'>"


def get_current_time_post_format():
    """
    get the current time in the format that the server expects
    :return: the current time in the format that the server expects
    """
    current_time = datetime.utcnow().isoformat() + 'Z'
    return current_time


def get_current_date():
    """
    get the current date in the dd/mm format
    :return: the current date in the dd/mm format
    """
    current_date = datetime.now().strftime("%d/%m")
    return current_date


def get_current_time():
    """
    get the current time in the mm:hh format
    :return: the current time in the mm:hh format
    """
    current_time = datetime.now().strftime("%H:%M")
    return current_time


def get_current_time_regular_format():
    """
    get the current time in the regular format that the server show to the user
    :return: the current time in the regular format that the server show to the user
    """
    current_time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
    return current_time


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


def create_a_string_with_ascii_sum(ascii_sum):
    """
    creates a string with the given ascii sum
    :param ascii_sum: the ascii sum to create a string with
    :return: the string with the given ascii sum
    """
    result = ""
    # add 48 to the ascii sum until it is less than 48
    while ascii_sum > 48:
        result += chr(48)
        ascii_sum -= 48
    # if the ascii sum is less than 48 so it can be up to 47 so if we add 47+48=95 and 95 is the range of 48 - 122
    # the range of numbers and letters in the ascii table
    result = result[:-1] + chr(48 + ascii_sum)
    return result


def get_user_data_from_app_authentication(message):
    """
    get the user id and username from the app authentication message
    :param message: the authentication message
    :return: the user id, username , avatar, user description, user privacy, user gender and the user mail
    """
    user_id = message.split('"id":')[1].split(',')[0]
    user_screen_name = message.split('"screen_name":"')[1].split('"')[0]
    avatar = message.split('"avatar":"')[1].split('"')[0]
    description = message.split('"description":"')[1].split('"')[0]
    privacy = message.split('"privacy":"')[1].split('"')[0]
    gender = message.split('"gender":"')[1].split('"')[0]
    mail = message.split('"mail":"')[1].split('"')[0]
    return user_id, user_screen_name, avatar, description, privacy, gender, mail


def initialize_app_connection():
    """
    initialize the connection to the app server
    :return: the connection to the server(socket)
    """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to the app server
    app_server_address = (APP_SERVER_IP, APP_SERVER_PORT)
    sock.connect(app_server_address)
    return sock


def create_app_login_string(user_name, password):
    """
    create the login string
    :param user_name: the username to log in with
    :param password: the password to log in with
    :return: the login string
    """
    msg = APP_LOGIN_STRING.replace('_name_', user_name)
    msg = msg.replace('_pass_', password)
    return msg


def app_login(app_sock, user_name, password, print_error=True):
    """
    login to the server with the app
    :param print_error: if there was a problem with the login, print the error only if this parameter is true
    :param app_sock: the connection to the app server(socket)
    :param user_name: the username to log in with
    :param password: the password to log in with
    :return: None
    """

    # send login message
    app_sock.sendall(create_app_login_string(user_name, password).encode())

    # Receive data
    server_msg = app_sock.recv(1024).decode()
    if (server_msg.find("Login received") == -1):
        if print_error:
            print("\033[31mlogin to server failed\n \033[0m")
        return server_msg

    # send checksum message
    checksum = ascii_checksum(user_name + password)
    msg = APP_CHECKSUM_STRING.replace('_sum_', str(checksum))
    app_sock.sendall(msg.encode())

    # Receive data and save for the user id
    server_msg = app_sock.recv(1024).decode()
    if (server_msg.find("Authentication approved") == -1):
        if print_error:
            # print that the authentication failed in red
            print("\033[31mlogin to server failed\n \033[0m")
            print("\033[31mAuthentication code mismatch\n \033[0m")
        return

    # get the user id from the authentication message
    user_id, screen_name, avatar, description, privacy, gender, mail = get_user_data_from_app_authentication(server_msg)

    # add the user id to the fetch and load messages
    msg = APP_FETCH_STRING.replace('_userid_', user_id)
    app_sock.sendall(msg.encode())

    # Receive data
    app_sock.recv(1024).decode()

    # send checksum message
    msg = APP_LOAD_STRING.replace('_userid_', user_id)
    app_sock.sendall(msg.encode())

    # Receive data
    app_sock.recv(1024).decode()

    # print that we logged in successfully in green
    print("\033[32mlogin to server successful\n \033[0m")

    # print user id and screen name in cyan
    print("\033[36muser id: " + user_id + "\nuser screen name: " + screen_name + "\n\033[0m")
    return user_id, screen_name, avatar, description, privacy, gender, mail


def logout_app(app_sock, user_id):
    """
    logout from the server
    :param app_sock: the connection to the server(socket)
    :param user_id: the id of the user that wants to log out
    :return: None
    """
    logout_string = APP_LOGOUT_STRING.replace('_user_id_', str(user_id))
    msg = send_message(app_sock, logout_string)

    # print the result of the logout
    if is_approved(msg, 'logout successful'):
        app_sock.close()


def send_message(app_sock, message):
    """
    send a message to the server and return the response
    :param app_sock: the connection to the server(socket)
    :param message: the message to send
    :return:
    """
    app_sock.sendall(message.encode())
    return app_sock.recv(8192).decode()


def is_approved(message, approved_string, print_approved=True):
    """
    check if the message is approved and print the result
    :param approved_string: the string to print if the message is approved
    :param message: the message to check
    :return: none
    """
    if message.find('approved') != -1:
        # print that the glit was posted in green
        if print_approved:
            print('\033[92m' + approved_string + '\033[0m')
        return True
    else:
        # print that there is an error in red
        if print_approved:
            print('\033[91m' + 'error: ' + message + '\033[0m')
        return False


def get_value_from_response(response, value):
    """
    get a value from a response
    :param response: the response to get the value from
    :param value: the value to get
    """
    try:
        # get the value from the response
        value = response.split('"' + value + '":')[1].split(',')

        # remove the " from the value if there is
        if value[0][0] == '"':
            value[0] = value[0][1:-1]

        # remove the end of the message if the value is the last one
        if len(value) == 1:
            value[0] = value[0][:-4]

        # return the value
        return value[0]
    except Exception as e:
        return None


def like_glit_app(app_sock, glit_id, user_id, user_screen_name):
    """
    like a glit
    :param app_sock: the connection to the app server(socket)
    :param glit_id: the id of the glit to like
    :param user_id: the id of the user that likes the glit
    :param user_screen_name: the username of the user that likes the glit
    :return: None
    """
    like_glit_string = APP_LIKE_GLIT_STRING.replace('_glit_id_', str(glit_id))
    like_glit_string = like_glit_string.replace('_user_id_', str(user_id))
    like_glit_string = like_glit_string.replace('_user_screen_name_', user_screen_name)
    msg = send_message(app_sock, like_glit_string)

    # print the result of the like
    is_approved(msg, 'glit liked')
    return msg


def dislike_glit_app(app_sock, glit_id):
    """
    dislike a glit
    :param app_sock: the connection to the server(socket)
    :param glit_id: the id of the glit to dislike
    :return: None
    """
    dislike_glit_string = APP_DISLIKE_STRING.replace('_ID_', str(glit_id))
    msg = send_message(app_sock, dislike_glit_string)

    # print the result of the dislike
    is_approved(msg, 'glit disliked')


def comment_glit_app(app_sock, glit_id, user_id, user_screen_name, content, date):
    """
    This function sends a comment glit request to the server
    :param app_sock: the socket object
    :param glit_id: the id of the glit that we want to comment
    :param user_id: the id of the user that wants to comment
    :param user_screen_name: the screen name of the user that wants to comment
    :param content: the content of the comment
    :param date: the date of the comment
    :return: None
    """
    comment_glit_string = COMMENT_GLIT_STRING.replace('_glit_id_', glit_id).replace('_user_id_', user_id).replace(
        '_user_screen_name_', user_screen_name).replace('_content_', content).replace('_date_', date)
    msg = send_message(app_sock, comment_glit_string)

    # print the result of the comment
    is_approved(msg, 'commented on glit')


def post_glit_app(app_sock, feed_owner_id, publisher_id, publisher_screen_name, publisher_avatar, background_color,
                  date,
                  content, font_color):
    """
    post a glit
    :param app_sock: the connection to the server(socket)
    :param feed_owner_id: the id of the user that owns the feed
    :param publisher_id: the id of the user that post the glit
    :param publisher_screen_name: the username of the user that post the glit
    :param publisher_avatar: the avatar of the user that post the glit
    :param background_color: the background color of the glit
    :param date: the date of the glit
    :param content: the content of the glit
    :param font_color: the font color of the glit
    :return: None
    """
    # replace the placeholders in the string with the actual values
    post_glit_string = POST_GLIT_STRING.replace('_feed_owner_id_', str(feed_owner_id))
    post_glit_string = post_glit_string.replace('_publisher_id_', str(publisher_id))
    post_glit_string = post_glit_string.replace('_publisher_screen_name_', publisher_screen_name)
    post_glit_string = post_glit_string.replace('_publisher_avatar_', publisher_avatar)
    post_glit_string = post_glit_string.replace('_background_color_', background_color)
    post_glit_string = post_glit_string.replace('_date_', date)
    post_glit_string = post_glit_string.replace('_content_', content)
    post_glit_string = post_glit_string.replace('_font_color_', font_color)

    # send the message to the server
    msg = send_message(app_sock, post_glit_string)

    # print the result of the post
    is_approved(msg, 'glit posted')
    return msg


def search_gliters_app(app_sock, search_type, search_entry):
    """
    This function sends a search request to the server
    :param app_sock: the connection to the server(socket)
    :param search_type: the type of the search
    :param search_entry: the entry of the search
    :return: None
    """
    search_string = SEARCH_STRING.replace('_search_type_', search_type).replace('_search_entry_', search_entry)
    msg = send_message(app_sock, search_string)

    if msg.find('Entities search result') != -1:
        # print that the search was successful in green
        print('\033[92m' + 'search successful' + '\033[0m')
        return msg
    else:
        # print that there is an error in red
        print('\033[91m' + 'error: ' + msg + '\033[0m')
        return None


def simplify_data(data):
    """
    simplify given data
    :param data: the search result
    :return: a dictionary with the data
    """
    if data is None:
        return None

    # get only the data from the respond
    only_data = data[data.find('['):data.find(']') + 1]

    if (only_data == '[]'):
        return None

    # convert the string to a list of dictionaries that contain the data
    simplified_data = eval(only_data)

    # return the data
    return simplified_data


def load_data_app(app_sock, feed_owner_id, glit_count):
    """
    load glits data from the server
    :param app_sock: the connection to the server(socket)
    :param feed_owner_id: the id of the user that owns the feed
    :param glit_count: the number of glits to load
    :return: None
    """
    print("loading data...")
    load_string = APP_FEED_LOAD_STRING.replace('_feed_owner_id_', str(feed_owner_id))
    load_string = load_string.replace('_glit_count_', str(glit_count))
    load_string = load_string.replace('_end_date_', get_current_time_post_format())
    msg = send_message(app_sock, load_string)

    # print the result of the load
    is_approved(msg, 'data loaded')

    return msg


def change_user_info_app(app_sock, user_screen_name, avatar, description, privacy, user_id,
                         user_name, password, gender, mail, print_error=True):
    """
    This function sends a change user info request to the server
    :param print_error: print the result of the change(succesful or not)
    :param app_sock: the connection to the server(socket)
    :param user_screen_name: the screen name of the user
    :param avatar: the avatar of the user
    :param description: the description of the user
    :param privacy: the privacy of the user(Public, Private)
    :param user_id: the id of the user
    :param user_name: the username of the user
    :param password: the password of the user
    :param gender: the gender of the user (male, female, leave blank)
    :param mail: the mail of the user
    :return: None
    """
    change_user_info_string = APP_CHANGE_USER_INFO.replace('_screen_name_', user_screen_name)
    change_user_info_string = change_user_info_string.replace('_avatar_', avatar)
    change_user_info_string = change_user_info_string.replace('_description_', description)
    change_user_info_string = change_user_info_string.replace('_privacy_', privacy)
    change_user_info_string = change_user_info_string.replace('_id_', str(user_id))
    change_user_info_string = change_user_info_string.replace('_user_name_', user_name)
    change_user_info_string = change_user_info_string.replace('_password_', password)
    change_user_info_string = change_user_info_string.replace('_gender_', gender)
    change_user_info_string = change_user_info_string.replace('_mail_', mail)
    msg = send_message(app_sock, change_user_info_string)

    return msg, is_approved(msg, 'user info changed', print_error)


def create_cookie(date, time, username):
    """
    This function creates a cookie
    :param date: the date of the cookie in the format of dd/mm/yyyy
    :param time: the time of the cookie in the format of hh:mm
    :param username: the username of the user
    :return: the cookie
    """
    date = date.replace('/', '')
    time = time.replace(':', '')
    username_MD5 = hashlib.md5(username.encode()).hexdigest()
    return date + '.' + username_MD5 + '.' + time + '.' + date


def send_glance_request_app(app_sock, user_sending, user_to_send):
    """
    This function sends a glance request to the server
    :param app_sock: the connection to the server(socket)
    :param user_sending: the user that sends the request
    :param user_to_send: the user that the request is sent to
    :return: None
    """
    glance_string = APP_GLANCE_REQUEST_STRING.replace('_user_sending_', str(user_sending))
    glance_string = glance_string.replace('_user_to_send_', str(user_to_send))
    msg = send_message(app_sock, glance_string)

    if msg.find("Glance request is valid") != -1:
        # print that the glance request was sent
        print('\033[92m' + 'glance request sent' + '\033[0m')
        return msg
    else:
        # print that there is an error in red
        print('\033[91m' + 'error: ' + msg + '\033[0m')
        return None


def refuse_glance_request_app(app_sock, user_sending, user_to_send):
    """
    This function refuses a glance request
    :param app_sock: the connection to the server(socket)
    :param user_sending: the user that sends the request
    :param user_to_send: the user that the request is sent to
    :return:
    """
    glance_string = APP_REFUSE_GLANCE_REQUEST_STRING.replace('_user_sending_', str(user_sending))
    glance_string = glance_string.replace('_user_to_send_', str(user_to_send))
    msg = send_message(app_sock, glance_string)

    return msg.find("Glance response is valid") != -1


def request_password_recovery_web(username):
    """
    This function sends a password recovery request to the server
    :param username: the username of the user
    :return: True if the request was sent successfully, False otherwise
    """
    response = requests.post(WEB_CREATE_PASSWORD_RECOVERY_URL, json=username)
    return response.status_code == 204


def generate_key(date, user_id, time):
    """
    This function generates a key for the password recovery
    :param date: the date of the key in the format of dd/mm
    :param user_id: the user id of the user
    :param time: the time of the key in the format of hh:mm
    :return: the key
    """
    date = date.replace('/', '')
    time = time.replace(':', '')
    user_code = ""
    for i in str(user_id):
        user_code += chr(int(i) + 65)

    return date + user_code + time


def get_password_from_recovery_code(username, recovery_code):
    """
    This function gets the password with the recovery code
    :param username: the username of the user
    :param recovery_code: the recovery code of the user
    :return: the password
    """
    request_body = [username, recovery_code]
    response = requests.post(WEB_GET_PASSWORD_RECOVERY_CODE, json=request_body)
    return response.text


def get_user_search_history_app(app_sock, user_id):
    """
    This function gets the user search history
    :param app_sock: the connection to the server(socket)
    :param user_id: the user id of the user
    :return: the search history
    """
    search_history_string = APP_GET_USER_SEARCH_HISTORY.replace('_user_id_', str(user_id))
    msg = send_message(app_sock, search_history_string)
    return msg


def get_user_updates_app(app_sock, user_id):
    """
    This function gets the user updates
    :param app_sock: the connection to the server(socket)
    :param user_id: the user id of the user
    :return: the updates
    """
    updates_string = APP_LOAD_STRING.replace('_userid_', str(user_id))
    msg = send_message(app_sock, updates_string)
    return msg