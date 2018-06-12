
def confirm(message, default="Y"):
    message += " [Y/n]" if default == "Y" else " [y/N]"
    while True:
        result = input(message)
        if result == "":
            return True if default == "Y" else False
        elif result.lower() == "y":
            return True
        elif result.lower() == "n":
            return False
        else:
            print("Input not valid")
