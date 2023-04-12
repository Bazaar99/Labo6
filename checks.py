import os
import json
from colorama import Fore, Style


def check_ping():

    with open("servers.json", "r") as servers:
        hostnames = json.load(servers)

    for hostname in hostnames:
        response = os.system("ping -n 1 " + hostname)
        # and then check the response...
        if response == 0:
            pingstatus = "Network Active"
        else:
            pingstatus = "Network Error"

        print(Fore.GREEN + pingstatus)
        print(Style.RESET_ALL)

    with open("index.html", "r") as html_logger:
        html_text = html_logger.read()

        front = html_text[:263]
        middle = html_text[263: -24]
        end = html_text[-24:]

        content = ""
        for hostname in hostnames:
            content = content + f"<li>{hostname}</li>"

        html_join = front + middle + content + end
    with open("index.html", "w") as html_logger:
        html_logger.write(html_join)
