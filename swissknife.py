import glitter

username = ""
password = ""
user_id = ""
screen_name = ""
avatar = ""
app_sock = None
web_sock = None


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
    search_result = glitter.simplify_search_respond(search_result)
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
    else:
        temp_user_id = user_id

    # get the user posts
    load = glitter.load_data_app(app_sock, temp_user_id, 5)

    print(load)
    # simplify the response and print the posts
    glits = glitter.simplify_load_data(load)

    print()
    for i in range(len(glits)):
        print(str(i) + ". \"" + glits[i]['content'] + "\" (" + glits[i]['date'][0:10] + ")")

    # get the user choice and return the post id
    return glits[int(input("Enter the number of the glit you choose: "))]['id']


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
    print("6. exit")


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
    elif (user_choice_kind == "5"):
        print_search_menu()
    elif (user_choice_kind == "6"):
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
    temp_user_id, temp_screen_name, temp_avatar = glitter.app_login(temp_sock, temp_username, temp_password)
    return temp_sock, temp_user_id, temp_screen_name, temp_avatar


def comment_glit_prove_of_concepts(user_choice):
    """
    this function run the comment prove of concepts
    :return: None
    """
    if (user_choice == "1"):
        # This is a POC for commenting a glit with a time that is not the current time
        glitter.comment_glit_app(app_sock, get_post_id(), user_id, screen_name,
                                 ('now its ' + glitter.get_current_time_regular_format()), glitter.TIME_SEND_EXAMPLE)
    elif (user_choice == "2"):
        # this is a POC for commenting to a gilt with an id that does not exist, it won't throw an error but instead
        # create a new glit with the content of the comment and pink background color in the feed of the user that
        # commented last
        glitter.comment_glit_app(app_sock, glitter.NONEXISTENT_ID, user_id, screen_name,
                                 'this is a comment to a nonexistent glit', glitter.get_current_time_post_format())
    elif (user_choice == "3"):
        # this is a POC for commenting to a private glit
        glitter.comment_glit_app(app_sock, get_post_id(), user_id, screen_name,
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
        msg = glitter.post_glit_app(temp_sock, temp_user_id, temp_user_id, temp_screen_name, temp_avatar, "white",
                              glitter.get_current_time_post_format(), "this is a private glit", "black")
        print("now let's like the private glit")
        temp_glit_id = glitter.get_post_id_from_response(msg)
        print("the glit id is: " + str(temp_glit_id))
        glitter.like_glit_app(temp_sock, temp_glit_id, temp_user_id, temp_screen_name)
        print("now let's log out from the temp user")
        glitter.logout_app(temp_sock, temp_user_id)
        temp_sock.close()
        print("now let's dislike the private glit from the main user")
        glitter.dislike_glit_app(app_sock, temp_glit_id)

    elif (user_choice == "2"):
        # This is a POC that show that you can dislike a glit that is not yours
        glitter.dislike_glit_app(app_sock, get_post_id(), user_id, screen_name)
    elif (user_choice == "3"):
        return


def main():
    # define the global variables
    global app_sock, web_sock, user_id, screen_name, avatar

    welcome_and_get_login_info()
    app_sock = glitter.initialize_app_connection()
    try:
        user_id, screen_name, avatar = glitter.app_login(app_sock, username, password)
    except Exception as e:
        return

    user_choice_kind = ""
    while (user_choice_kind != "6"):
        print_main_menu()
        user_choice_kind = input("Your choice: ")
        print_right_menu(user_choice_kind)
    glitter.logout_app(app_sock, user_id)


if __name__ == '__main__':
    main()
