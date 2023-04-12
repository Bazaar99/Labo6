import sys  # om te zien of er een argument word meegegeven
from modi import menu, cli
# from checks import init


def main():
    """ Start de applicatie. Met argument in de grafische interface, zonder argument in de cli """


    if len(sys.argv) > 1:
        cli(sys.argv)
    else:
        menu()


if __name__ == "__main__":
    main()
