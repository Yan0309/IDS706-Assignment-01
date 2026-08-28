def welcome_message(name):
    return f"{name}, welcome to the Data Engineering course."


if __name__ == "__main__":
    # Get the user's name and print the welcome message
    name = input("Enter your name: ")
    print(welcome_message(name))