from checks import check_ping
from menu import menu


def cli(input):
    """Argement ckeck om de functie check ping aan te roepen.
    menu om de functie menu aan te roepen."""

    if input[1] == "check":
        check_ping()
        print("De checks werden uitgevoerd")
    elif input[1] == "menu":
        menu()
