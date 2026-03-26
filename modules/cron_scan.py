import subprocess

def run():

    cron = subprocess.getoutput(
    "ls -la /etc/cron* 2>/dev/null"
    )

    return {
        "name":"Cron Jobs",
        "data":cron
    }
