# this file will contain all the functions that has
# a connection with the glitter and will be used as an api in the swissknife.py file
import socket
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
APP_CHANGE_USER_INFO = '350#{gli&&er}{"screen_name":"roki roki","avatar":"im2","description":"hi","privacy":"Public",' \
                       '"id":14703,"user_name":"yanir","password":"aton","gender":"Male",' \
                       '"mail":"yaniraton@yaniratom.com"}##'
NUM_OF_LIKES = 3


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


def get_user_data_from_app_authentication(message):
    """
    get the user id and username from the app authentication message
    :param message: the authentication message
    :return: the user id and username
    """
    user_id = message.split('"id":')[1].split(',')[0]
    user_screen_name = message.split('"screen_name":"')[1].split('"')[0]
    avatar = message.split('"avatar":"')[1].split('"')[0]
    return user_id, user_screen_name, avatar


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


def app_login(app_sock, user_name, password):
    """
    login to the server with the app
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
        print("\033[31mlogin to server failed\n \033[0m")
        return

    # send checksum message
    checksum = ascii_checksum(user_name + password)
    msg = APP_CHECKSUM_STRING.replace('_sum_', str(checksum))
    app_sock.sendall(msg.encode())

    # Receive data and save for the user id
    server_msg = app_sock.recv(1024).decode()
    if (server_msg.find("Authentication approved") == -1):
        # print that the authentication failed in red
        print("\033[31mlogin to server failed\n \033[0m")
        print("\033[31mAuthentication code mismatch\n \033[0m")
        return

    # get the user id from the authentication message
    user_id, screen_name, avatar = get_user_data_from_app_authentication(server_msg)

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
    return user_id, screen_name, avatar


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
    is_approved(msg, 'logout successful')


def send_message(app_sock, message):
    app_sock.sendall(message.encode())
    return app_sock.recv(8192).decode()


def is_approved(message, approved_string):
    """
    check if the message is approved and print the result
    :param approved_string: the string to print if the message is approved
    :param message: the message to check
    :return: none
    """
    if message.find('approved') != -1:
        # print that the glit was posted in green
        print('\033[92m' + approved_string + '\033[0m')
    else:
        # print that there is an error in red
        print('\033[91m' + 'error: ' + message + '\033[0m')


def get_post_id_from_response(response):
    """
    get the post id from the response
    :param response: the response to get the post id from
    :return: the post id
    """
    try:
        # get the from the id to the end of the response
        id = response.split('"id":')[1].split(',')[0]

        # return the id without the last 4 characters that are not part of the id and represent the end of the response
        return id[:len(id) - 4]
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


def infinity_likes_app(app_sock, glit_id, user_id, user_screen_name, num_of_likes):
    """
    This is a POC that show that you can get as many likes as you want simply by sending repeated like requests
    :param app_sock: the connection to the app server(socket)
    :param glit_id: the id of the glit to like
    :param user_id: the id of the user that likes the glit
    :param user_screen_name: the username of the user that likes the glit
    :param num_of_likes: the number of times to like the glit
    :return: None
    """
    for i in range(num_of_likes):
        like_glit_app(app_sock, glit_id, user_id, user_screen_name)


def like_nonexistent_glit_app(app_sock, user_id, user_screen_name):
    """
    This is a POC that show that you can like a glit that does not exist,
    and it will not throw an error but create a new glit with empty content and pink color
    :param app_sock: the connection to the app server(socket)
    :param user_id: the id of the user that likes the glit
    :param user_screen_name: the username of the user that likes the glit
    :return: None
    """
    like_glit_app(app_sock, 100000, user_id, user_screen_name)


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


def dislike_not_your_gilt_app(app_sock, glit_id):
    """
    this is a POC for disliking a glit that you didn't dislike before
    :param app_sock: the connection to the server(socket)
    :param glit_id: the id of the glit to dislike
    :return: None
    """
    dislike_glit_app(app_sock, glit_id)


def dislike_private_glit_app(app_sock, glit_id):
    """
    this is a POC for disliking a private glit
    :param app_sock: the connection to the server(socket)
    :param glit_id: the id of the glit to dislike
    :return: None
    """
    dislike_glit_app(app_sock, glit_id)


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


def change_comment_time_app(app_sock, glit_id, user_id, user_screen_name):
    """
    This is a POC for commenting a glit with a time that is not the current time
    :param app_sock: the socket object
    :param glit_id: the id of the glit that we want to comment
    :param user_id: the id of the user that wants to comment
    :param user_screen_name: the screen name of the user that wants to comment
    :return: None
    """
    comment_glit_app(app_sock, glit_id, user_id, user_screen_name, ('now its' + get_current_time_regular_format()),
                     TIME_SEND_EXAMPLE)


def comment_nonexistent_glit_id_app(app_sock, user_id, user_screen_name, content):
    """
    this is a POC for commenting to a gilt with an id that does not exist,
    it won't throw an error but instead create a new glit with the content of the comment and pink background color
    :param app_sock: the socket object
    :param user_id: the id of the user that wants to comment
    :param user_screen_name: the screen name of the user that wants to comment
    :param content: the content of the comment
    :return: None
    """
    comment_glit_app(app_sock, NONEXISTENT_ID, user_id, user_screen_name, content, get_current_time_post_format())


def comment_to_private_glit(app_sock, glit_id, user_id, user_screen_name, content):
    """
    this is a POC for commenting to a private glit
    :param app_sock: the socket object
    :param glit_id: the id of the glit that we want to comment
    :param user_id: the id of the user that wants to comment
    :param user_screen_name: the screen name of the user that wants to comment
    :param content: the content of the comment
    :return: None
    """
    comment_glit_app(app_sock, glit_id, user_id, user_screen_name, content, get_current_time_post_format())


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


def change_post_time_app(app_sock, feed_owner_id, publisher_id, publisher_screen_name, publisher_avatar,
                         background_color,
                         content, font_color):
    """
    This is a POC for posting a glit with a time that is not the current time
    :param app_sock: the connection to the server(socket)
    :param feed_owner_id: the id of the user that owns the feed
    :param publisher_id: the id of the user that post the glit
    :param publisher_screen_name: the username of the user that post the glit
    :param publisher_avatar: the avatar of the user that post the glit
    :param background_color: the background color of the glit
    :param content: the content of the glit
    :param font_color: the font color of the glit
    :return: None
    """
    post_glit_app(app_sock, feed_owner_id, publisher_id, publisher_screen_name, publisher_avatar, '', TIME_SEND_EXAMPLE,
                  ('now its ' + get_current_time_regular_format()), 'black')


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


def simplify_search_respond(search_result):
    """
    simplify the search respond
    :param search_result: the search result
    :return: a dictionary with the data
    """
    if search_result is None:
        return None

    # get the search result only
    search_result = search_result[search_result.find('['):search_result.find(']') + 1]

    if (search_result == '[]'):
        return None

    # split the search result to users
    users = search_result.split('},')

    # remove the { and } from the users
    for i in range(len(users)):
        users[i] = users[i].replace('{', '').replace('}', '').replace('[', '').replace(']', '')

        # split the users to data
        users[i] = users[i].split(',"')
        for j in range(len(users[i])):
            # split the data to key and value
            users[i][j] = users[i][j].split(':')
            users[i][j][0] = users[i][j][0].replace('"', '')
            users[i][j][1] = users[i][j][1].replace('"', '')

        # create a dictionary from the data
        users[i] = dict(users[i])

    # return the users
    return users


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


def simplify_load_data(search_result):
    """
    Simplify the search response
    :param search_result: the search result
    :return: a list of dictionaries with the data
    """
    # Get the search result only
    search_result = search_result[search_result.find('['):search_result.find(']') + 1]

    # Split the search result into glits
    glits = search_result.split('},')

    glits_dict = []

    # Remove the { and } from the glits
    for i in range(len(glits)):
        glits[i] = glits[i].replace('{', '').replace('}', '').replace('[', '').replace(']', '')

        # Split the glits into data
        glits[i] = glits[i].split(',"')
        glit_data = {}

        for j in range(len(glits[i])):
            # Split the data into key and value
            key_value = glits[i][j].split(':')
            key = key_value[0].replace('"', '')
            value = key_value[1].replace('"', '')

            # Add key-value pair to glit_data dictionary
            glit_data[key] = value

        # Append glit_data dictionary to glits_dict list
        glits_dict.append(glit_data)

    # Return the list of glits
    return glits_dict