import json


def filter_users_by_name(name):
    """ Take a <name> as str and return user-data(dict) with the user-name -> <name> """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """ Take a <age> as int and return user-data(dict) with the user-age -> <age> """
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_by_age = [user for user in users if user['age'] == age]

    for user in filtered_by_age:
        print(user)


def filter_users_by_email(email):
    """
    Take a <email> as str and return user-data(dict) with the user-mail -> <email>
    filters via ending of the addresses: '.net', '.com', ...
    """
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_by_email = [user for user in users if user['email'].strip().endswith(email)]

    for user in filtered_by_email:
        print(user)


if __name__ == "__main__":
    """
    Ask the user what he wants to filter by and return user-data(dict) that the user wants to see.
    name -> string (case-insensitive, exact name)
    age -> int (a positive number)
    email -> string (.com, .net, ...)
    """
    filter_option = input("What would you like to filter by? (name/age/email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter by: ").strip())
            if age_to_search < 1:
                raise ValueError
            filter_users_by_age(age_to_search)
        except ValueError:
            print("\nno valid age to search for\n")
    elif filter_option == "email":
        email_to_search = input("Enter a mail to filter by (.com/.net/...): ")
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
