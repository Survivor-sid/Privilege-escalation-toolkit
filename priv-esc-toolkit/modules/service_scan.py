import subprocess

def run():

    services = subprocess.getoutput(
    "systemctl list-units --type=service --state=running"
    )

    return {
        "name":"Running Services",
        "data":services
    }
