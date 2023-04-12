import json


def menu():
    """Menu om het bestand servers.json te bewerken"""


    herhalen = True
    while herhalen == True:
        userinput = input(
            "1)voeg server toe\n2)verwijder server\n3)toon lijst van alle servers\n")
        with open("servers.json", "r") as servers:
            hostnames = json.load(servers)

        if userinput == "1":
            userinput = input("Server hostname of ip adress: ")
            hostnames.append(userinput)
            print("server toegevoegd")
            while True:
                userinput = input(
                    "Geef nog een server op (enter om te stoppen): ")
                if userinput == "":
                    herhalen = False
                    break
                else:
                    hostnames.append(userinput)
                    print("server toegevoegd")
            with open("servers.json", "w") as servers:
                hostnames = json.dump(hostnames, servers)

        elif userinput == "2":
            userinput = input("Server hostname of ip adress: ")
            while True:
                if userinput in hostnames:
                    hostnames.remove(userinput)
                    print(f"server {userinput} verwijderd")
                    userinput = input(
                        "Wilt u nog een server verwijderen? (j/n): ")
                    if userinput == "n":
                        herhalen = False
                        break
                else:
                    print("Server staat niet in de lijst")
                userinput = input("Server hostname of ip adress: ")
            with open("servers.json", "w") as servers:
                hostnames = json.dump(hostnames, servers)

        elif userinput == "3":
            print(hostnames)
            herhalen = False
        else:
            print("Geef geldige invoer op\n")
