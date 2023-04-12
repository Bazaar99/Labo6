from checks import check_ping
from menu import menu

def cli(input):
    if input[1] == "check":
        check_ping()
        print("De checks werden uitgevoerd")
    elif input[1] == "menu":
        menu()



