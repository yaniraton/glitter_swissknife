import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_post
else:
    from . import base_post


def post_with_XSS():
    """
    This is a POC for posting a glit with cross site scripting
    :return: None
    """

    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id, username and avatar
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # post a glit
    base_post.post_glit(socket, user_id, user_id, screen_name, avatar, 'white', base_connection.get_current_time_post_format(), "<img src='https://www.shutterstock.com/image-vector/hi-sticker-social-media-content-260nw-1138004576.jpg'>", 'black')

    socket.close()


if __name__ == '__main__':
    post_with_XSS()
