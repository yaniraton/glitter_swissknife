import base_connection
SEARCH_STRING = '300#{gli&&er}{"search_type":"_search_type_","search_entry":"_search_entry_"}##'


def search_gliters(socket, search_type, search_entry):
    """
    This function sends a search request to the server
    :param socket: the socket object
    :param search_type: the type of the search
    :param search_entry: the entry of the search
    :return: None
    """
    search_string = SEARCH_STRING.replace('_search_type_', search_type).replace('_search_entry_', search_entry)
    msg = base_connection.send_message(socket, search_string)
    if msg.find('Entities search result') != -1:
        # print that the search was posted in green
        print('\033[92m' + 'search posted' + '\033[0m')
    else:
        # print that there is an error in red
        print('\033[91m' + 'error: ' + msg + '\033[0m')
    return msg


def simplify_search_respond(search_result):
    """
    simplify the search respond
    search result example: 305#Entities search result{gli&&er}[{"screen_name":"yossi gabay","avatar":"im3","description":"dsad","privacy":"Public","id":19,"mail":"saqdasd@sd.com"},{"screen_name":"yod 3 3","avatar":"im7","description":"123","privacy":"Public","id":21,"mail":"r@r.com"},{"screen_name":"Nehoray Calvin","avatar":"im8","description":"<script>alert(\"haha\");</script>","privacy":"Private","id":23,"mail":"nehorayd2580@gmail.com"},{"screen_name":"mynamenow","avatar":"im1","description":"lets go","privacy":"Public","id":24,"mail":"yonatan88@gmail.com"},{"screen_name":"yarin a","avatar":"im6","description":"mototo","privacy":"Public","id":25,"mail":"yaringefter@gmail.com"}]##
    :param search_result: the search result
    :return: a dictionary with the data
    """
    # get the search result only
    search_result = search_result[search_result.find('['):search_result.find(']') + 1]

    # split the search result to users
    users = search_result.split('},')

    # remove the { and } from the users
    for i in range(len(users)):
        users[i] = users[i].replace('{', '').replace('}', '').replace('[', '').replace(']', '')

        # split the users to data
        users[i] = users[i].split(',')
        for j in range(len(users[i])):
            # split the data to key and value
            users[i][j] = users[i][j].split(':')
            users[i][j][0] = users[i][j][0].replace('"', '')
            users[i][j][1] = users[i][j][1].replace('"', '')

        # create a dictionary from the data
        users[i] = dict(users[i])

    # return the users
    return users


def print_search_respond(search_result):
    """
    print the search respond
    :param search_result: the search result
    :return: None
    """
    users = simplify_search_respond(search_result)
    for user in users:
        print('id: ' + user['id'])
        print('screen name: ' + user['screen_name'])
        print('avatar: ' + user['avatar'])
        print('description: ' + user['description'])
        print('privacy: ' + user['privacy'])
        print('mail: ' + user['mail'])
        print('\n')