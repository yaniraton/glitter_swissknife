import base_connection
DISLIKE_STRING = '720#{gli&&er}_ID_##'


def dislike_glit(sock, glit_id):
    """
    dislike a glit
    :param sock: the connection to the server(socket)
    :param glit_id: the id of the glit to dislike
    :return: None
    """
    dislike_glit_string = DISLIKE_STRING.replace('_ID_', str(glit_id))
    msg = base_connection.send_message(sock, dislike_glit_string)


    if msg.find('approved') != -1:
        # print that the glit was posted in green
        print('\033[92m' + 'glit disliked' + '\033[0m')
    else:
        # print that there is an error in red
        print('\033[91m' + 'error: ' + msg + '\033[0m')
