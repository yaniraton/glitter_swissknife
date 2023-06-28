import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_like
else:
    from . import base_like

nonexistent_glit_id = 100000000


def like_nonexistent_glit():
    """
    This is a POC that show that you can like a glit that does not exist,
    and it will not throw an error but create a new glit with empty content and pink color
    :return: None
    """
    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id and username
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    base_like.like_glit(socket, nonexistent_glit_id, user_id, screen_name)

    socket.close()


if __name__ == '__main__':
    like_nonexistent_glit()
