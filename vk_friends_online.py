import getpass
import vk


APP_ID = -1


def get_user_login():
    return input("Login: ")


def get_user_password():
    return getpass.getpass()


def get_online_friends(login, password, api_version='5.35'):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        api = vk.API(session, v=api_version)
        friends_online_ids = api.friends.getOnline()
        return api.users.get(user_ids=friends_online_ids)
    except vk.exceptions.VkAuthError:
        return None


def output_friends_to_console(friends_online):
    if friends_online:
        print("Online users: ")
    else:
        print("No users online")

    for user in friends_online:
        print(" {} {}".format(user["first_name"], user["last_name"]))


def main():
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    if friends_online is not None:
        output_friends_to_console(friends_online)
    else:
        print("Invalid login or password")


if __name__ == "__main__":
    main()
