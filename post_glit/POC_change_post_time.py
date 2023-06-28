import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_post
else:
    from . import base_post


TIME_SEND = '2019-05-05T12:00:00Z'


def change_post_time():
    """
    This is a POC for posting a glit with a time that is not the current time
    :return: None
    """
    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id, username and avatar
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # post a glit
    base_post.post_glit(socket, user_id, user_id, screen_name, avatar, '', TIME_SEND, ('now its ' + base_connection.get_current_time_regular_format()), 'black')

    socket.close()


if __name__ == '__main__':
    change_post_time()
