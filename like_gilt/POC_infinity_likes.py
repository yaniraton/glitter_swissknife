import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_like
else:
    from . import base_like


NUM_OF_LIKES = 3


def infinity_likes():
    """
    This is a POC that show that you can get as many likes as you want simply by sending repeated like requests
    :return: None
    """
    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id and username
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # gilt id to like(should be a valid glit id and have access to it)
    glit_id = input("Enter a glit id: ")

    # repeat the like process NUM_OF_LIKES times
    for i in range(NUM_OF_LIKES):
        base_like.like_glit(socket, glit_id, user_id, screen_name)

    socket.close()


if __name__ == '__main__':
    infinity_likes()
