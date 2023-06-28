import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_post
else:
    from . import base_post


def post_glit_with_nonexistent_text_color():
    """
    This is a POC for posting a glit with text color that does not exist
    :return: None
    """

    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id, username and avatar
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # ask the user for the text color he wants
    msg_color = input("Enter a color in HEX or just in text for text color: ")
    base_post.post_glit(socket, user_id, user_id, screen_name, avatar, 'White', base_connection.get_current_time_post_format(), 'new color!!!', msg_color)

    socket.close()


if __name__ == '__main__':
    post_glit_with_nonexistent_text_color()
