import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_post
else:
    from . import base_post


def post_glit_with_nonexistent_background_color():
    """
    This is a POC for posting a glit with background color that does not exist
    :return: None
    """

    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id, username and avatar
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # ask the user for the text background he wants
    bg_color = input("Enter a color in HEX or just in text for background color: ")
    base_post.post_glit(socket, user_id, user_id, screen_name, avatar, bg_color, base_connection.get_current_time_post_format(), 'new color!!!', 'White')

    socket.close()


if __name__ == '__main__':
    post_glit_with_nonexistent_background_color()
