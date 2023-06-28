import base_connection

# to run the file on its own and on the main project
if __name__ == '__main__':
    import base_search
else:
    from . import base_search

def search_five_first_id():
    """
    This is a POC for searching for nothing and getting user ids and emails of the first 5 users
    :return: None
    """
    # create connection
    socket = base_connection.initialize_connection()

    # login and get user id and username
    user_id, screen_name, avatar = base_connection.login(socket, base_connection.username, base_connection.password)

    # search for users
    search = base_search.search_gliters(socket, 'SIMPLE', "")

    # print the results
    search = base_search.simplify_search_respond(search)
    for user in search:
        print(user['screen_name'] + ' ' + user['id'] + ' ' + user['mail'])

    socket.close()


if __name__ == '__main__':
    search_five_first_id()