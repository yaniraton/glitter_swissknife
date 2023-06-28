import base_connection
from imports import *


def print_main_menu():
    """
    This function prints the menu
    :return: None
    """
    print("Please choose one of the following options:")
    print("1. comment a glit prove of concepts")
    print("2. like a glit prove of concepts")
    print("3. dislike a glit prove of concepts")
    print("4. post a glit prove of concepts")
    print("5. search a glit prove of concepts")
    print("6. exit")


def welcome_and_get_login_info():
    """
    This function prints the welcome message and get the login info from the user
    :return: None
    """
    print("Welcome to the prove of concept for glit")
    print("Before we start, please enter your username and password")
    base_connection.username = input("Username: ")
    base_connection.password = input("Password: ")


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
    user_choice = input("Your choice: ")
    return user_choice


def print_dislike_menu():
    """
    This function prints the dislike menu
    :return: the user choice
    """
    print("Please choose one of the following options:")
    print("1. dislike a glit of a private user")
    print("2. dislike a glit that is not yours")
    print("3. exit")
    user_choice = input("Your choice: ")
    return user_choice


def print_like_menu():
    """
    This function prints the like menu
    :return: the user choice
    """
    print("Please choose one of the following options:")
    print("1. give yourself a like infinite likes(the default is 3 change the constant NUM_OF_LIKES)")
    print("2. like a nonexistent glit")
    print("3. exit")
    user_choice = input("Your choice: ")
    return user_choice


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
    user_choice = input("Your choice: ")
    return user_choice


def print_search_menu():
    """
    This function prints the search menu
    :return: the user choice
    """
    print("Please choose one of the following options:")
    print("1. get ID's and emails of search results")
    print("2. get info of the first 5 ID's of")
    print("3. exit")
    user_choice = input("Your choice: ")
    return user_choice


def print_right_menu(user_choice):
    """
    This function prints the right menu according to the user choice
    :param user_choice: the user choice
    :return: None
    """
    # for each option in the menu, print the right menu and do the user choice action
    if user_choice == "1":
        user_choice = print_comment_menu()
        action_comment(user_choice)
    elif user_choice == "2":
        user_choice = print_like_menu()
        action_like(user_choice)
    elif user_choice == "3":
        user_choice = print_dislike_menu()
        action_dislike(user_choice)
    elif user_choice == "4":
        user_choice = print_post_menu()
        action_post(user_choice)
    elif user_choice == "5":
        user_choice = print_search_menu()
        action_search(user_choice)
    else:
        print("Invalid choice")


def action_comment(user_choice):
    """
    This function does the action about commenting according to the user choice
    :param user_choice: the user choice
    :return: None
    """

    # do the action that the user chose
    if user_choice == "1":
        change_comment_time()
    elif user_choice == "2":
        comment_nonexistent_glit_id()
    elif user_choice == "3":
        comment_to_private_glit()
    elif user_choice == "4":
        print("exiting...")
    else:
        print("Invalid choice")


def action_dislike(user_choice):
    """
    This function does the action about disliking according to the user choice
    :param user_choice: the user choice
    :return: None
    """
    # do the action that the user chose
    if user_choice == "1":
        dislike_not_your_gilt()
    elif user_choice == "2":
        dislike_private_user()
    elif user_choice == "3":
        print("exiting...")
    else:
        print("Invalid choice")


def action_like(user_choice):
    """
    This function does the action about liking according to the user choice
    :param user_choice: the user choice
    :return: None
    """
    # do the action that the user chose
    if user_choice == "1":
        infinity_likes()
    elif user_choice == "2":
        like_nonexistent_glit()
    else:
        print("Invalid choice")


def action_post(user_choice):
    """
    This function does the action about posting according to the user choice
    :param user_choice: the user choice
    :return: None
    """
    # do the action that the user chose
    if user_choice == "1":
        change_post_time()
    elif user_choice == "2":
        post_glit_with_another_photo()
    elif user_choice == "3":
        post_glit_with_nonexistent_background_color()
    elif user_choice == "4":
        post_glit_with_nonexistent_text_color()
    elif user_choice == "5":
        post_with_XSS()
    elif user_choice == "6":
        print("exiting...")
    else:
        print("Invalid choice")


def action_search(user_choice):
    """
    This function does the action about searching according to the user choice
    :param user_choice: the user choice
    :return: None
    """
    # do the action that the user chose
    if user_choice == "1":
        get_IDs_from_search()
    elif user_choice == "2":
        search_five_first_id()
    elif user_choice == "3":
        print("exiting...")
    else:
        print("Invalid choice")


def main():
    """
    This function prints the main menu and does the user choice action
    :return: None
    """
    welcome_and_get_login_info()
    print_main_menu()
    user_choice = input("Your choice: ")
    print_right_menu(user_choice)


if __name__ == '__main__':
    main()
