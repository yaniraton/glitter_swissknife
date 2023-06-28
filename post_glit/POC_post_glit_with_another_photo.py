import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_post
else:
    from . import base_post


def post_glit_with_another_photo():
    """
    This is a POC for posting a glit with another picture that is not your current profile picture
    :return: None
    """
    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id, username and avatar
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # post a glit
    base_post.post_glit(socket, user_id, user_id, screen_name, 'im5', 'white', base_connection.get_current_time_post_format(), 'new picture!!!', 'black')

    socket.close()


if __name__ == '__main__':
    post_glit_with_another_photo()
