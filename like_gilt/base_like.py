import base_connection
LIKE_GLIT_STRING = '710#{gli&&er}{"glit_id":_glit_id_,"user_id":_user_id_,"user_screen_name":"_user_screen_name_","id":-1}##'


def like_glit(sock, glit_id, user_id, user_screen_name):
    """
    like a glit
    :param sock: the connection to the server(socket)
    :param glit_id: the id of the glit to like
    :param user_id: the id of the user that likes the glit
    :param user_screen_name: the username of the user that likes the glit
    :return: None
    """
    like_glit_string = LIKE_GLIT_STRING.replace('_glit_id_', str(glit_id))
    like_glit_string = like_glit_string.replace('_user_id_', str(user_id))
    like_glit_string = like_glit_string.replace('_user_screen_name_', user_screen_name)
    msg = base_connection.send_message(sock, like_glit_string)

    if msg.find('approved') != -1:
        # print that the glit was posted in green
        print('\033[92m' + 'glit liked' + '\033[0m')
    else:
        # print that there is an error in red
        print('\033[91m' + 'error: ' + msg + '\033[0m')
