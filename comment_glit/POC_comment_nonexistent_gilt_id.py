import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_comment
else:
    from . import base_comment

nonexistent_glit_id = "100000000"


def comment_nonexistent_glit_id():
    """
    this is a POC for commenting to a gilt with an id that does not exist,
    it won't throw an error but instead create a new glit with the content of the comment and pink background color
    :return: None
    """
    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id, username and avatar
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # comment to the glit
    base_comment.comment_glit(socket, nonexistent_glit_id, user_id, screen_name, 'comment!!!', base_connection.get_current_time_post_format())

    socket.close()


if __name__ == '__main__':
    comment_nonexistent_glit_id()
    