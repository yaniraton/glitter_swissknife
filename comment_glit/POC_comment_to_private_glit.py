import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_comment
else:
    from . import base_comment

def comment_to_private_glit():
    """
    this is a POC for commenting to a private glit
    :return: None
    """
    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id, username and avatar
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # glit id to comment(should be a valid glit id)
    glit_id = input("Enter a glit id: ")

    # comment to the glit
    base_comment.comment_glit(socket, glit_id, user_id, screen_name, 'comment!!!', base_connection.get_current_time_post_format())

    socket.close()


if __name__ == '__main__':
    comment_to_private_glit()
