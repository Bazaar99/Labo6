import sys
from modi import menu, cli


def main():
    """ Start de applicatie. Zonder argument in menu. Gebruik argument check om te pingen"""

    if len(sys.argv) > 1:
        cli(sys.argv)
    else:
        menu()


if __name__ == "__main__":
    main()
