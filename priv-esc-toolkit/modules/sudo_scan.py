import subprocess

def run():

    sudo = subprocess.getoutput(
    "sudo -l 2>/dev/null"
    )

    return {
        "name":"Sudo Permissions",
        "data":sudo
    }
