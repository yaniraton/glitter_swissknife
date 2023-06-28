import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_search
else:
    from . import base_search


def get_IDs_from_search():
    """
    This is a POC for searching and getting user ids and their emails
    :return: None
    """
    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id and username
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    search_prompt = input("Enter a search: ")

    # search for users
    search = base_search.search_gliters(socket, 'SIMPLE', search_prompt)

    # print the results
    search = base_search.simplify_search_respond(search)
    for user in search:
        print(user['screen_name'] + ' ' + user['id'] + ' ' + user['mail'])

    socket.close()


if __name__ == '__main__':
    get_IDs_from_search()

