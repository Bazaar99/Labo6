import os
import json
from colorama import Fore, Style
from datetime import datetime


def check_ping():

    with open("servers.json", "r") as servers:
        hostnames = json.load(servers)
    with open("index.html", "r") as html_logger:
        html_text = html_logger.read()
    with open("logs.json", "r") as logfile:
        logs = json.load(logfile)
    content = ""
    dt = str(datetime.now())
    for hostname in hostnames:

        logs.append("on " + dt[:19] + f" pinged {hostname}")

        response = os.system("ping -n 1 " + hostname)
        # and then check the response...
        if response == 0:
            pingstatus = "Network Active"
        else:
            pingstatus = "Network Error"

        print(Fore.GREEN + pingstatus)
        print(Style.RESET_ALL)

        content = content + \
            f"<li>{dt[:19]} ----------------- {pingstatus} ------------------ {hostname}</li>"

    front = html_text[:263]
    middle = html_text[263: -24]
    end = html_text[-24:]

    html_join = front + content + middle + end
    with open("index.html", "w") as html_logger:
        html_logger.write(html_join)
    with open("logs.json", "w") as logfile:
        json.dump(logs, logfile)
