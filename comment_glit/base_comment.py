import base_connection

COMMENT_GLIT_STRING = '650#{gli&&er}{"glit_id":_glit_id_,"user_id":_user_id_,"user_screen_name":"_user_screen_name_",' \
                      '"id":-1,"content":"_content_","date":"_date_"}##'


def comment_glit(socket, glit_id, user_id, user_screen_name, content, date):
    """
    This function sends a comment glit request to the server
    :param socket: the socket object
    :param glit_id: the id of the glit that we want to comment
    :param user_id: the id of the user that wants to comment
    :param user_screen_name: the screen name of the user that wants to comment
    :param content: the content of the comment
    :param date: the date of the comment
    :return: None
    """
    comment_glit_string = COMMENT_GLIT_STRING.replace('_glit_id_', glit_id).replace('_user_id_', user_id).replace(
        '_user_screen_name_', user_screen_name).replace('_content_', content).replace('_date_', date)
    msg = base_connection.send_message(socket, comment_glit_string)
    if msg.find('approved') != -1:
        # print that the glit was posted in green
        print('\033[92m' + 'glit posted' + '\033[0m')
    else:
        # print that there is an error in red
        print('\033[91m' + 'error: ' + msg + '\033[0m')
