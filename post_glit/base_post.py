import base_connection

POST_GLIT_STRING = '550#{gli&&er}{"feed_owner_id":_feed_owner_id_,"publisher_id":_publisher_id_,' \
                   '"publisher_screen_name":"_publisher_screen_name_","publisher_avatar":"_publisher_avatar_",' \
                   '"background_color":"_background_color_","date":"_date_","content":"_content_",' \
                   '"font_color":"_font_color_","id":-1}##'


def post_glit(sock, feed_owner_id, publisher_id, publisher_screen_name, publisher_avatar, background_color, date,
              content, font_color):
    """
    post a glit
    :param sock: the connection to the server(socket)
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
    msg = base_connection.send_message(sock, post_glit_string)

    # check if the glit was posted
    if msg.find('approved') != -1:
        # print that the glit was posted in green
        print('\033[92m' + 'glit posted' + '\033[0m')
    else:
        # print that there is an error in red
        print('\033[91m' + 'error: ' + msg + '\033[0m')
