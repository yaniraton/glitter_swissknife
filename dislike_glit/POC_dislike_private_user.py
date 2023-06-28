import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_dislike
else:
    from . import base_dislike


def dislike_private_user():
    """
    this is a POC for disliking a glit that is not yours
    :return: None
    """
    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id, username and avatar
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # get a glit id to dislike(should be a valid glit id)
    gild_id = input("Enter a glit like id of a private user: ")

    # dislike a glit of a private user
    base_dislike.dislike_glit(socket, gild_id)

    socket.close()


if __name__ == '__main__':
    dislike_private_user()
