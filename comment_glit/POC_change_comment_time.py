import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_comment
else:
    from . import base_comment


TIME_SEND = '2020-01-01T00:00:00Z'


def change_comment_time():
    """
    This is a POC for commenting a glit with a time that is not the current time
    :return: None
    """
    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id, username and avatar
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # get a glit id to comment(should be a valid glit id)
    gild_id = input("Enter a glit id: ")

    # comment a glit with different time
    base_comment.comment_glit(socket, gild_id, user_id, screen_name, ('now its' + base_connection.get_current_time_regular_format()), TIME_SEND)

    socket.close()


if __name__ == '__main__':
    change_comment_time()
