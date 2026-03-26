import subprocess

def run():

    caps = subprocess.getoutput(
    "getcap -r / 2>/dev/null"
    )

    return {
        "name":"Linux Capabilities",
        "data":caps
    }
