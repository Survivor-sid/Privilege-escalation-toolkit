import subprocess

def run():

    suid = subprocess.getoutput(
    "find / -perm -4000 -type f 2>/dev/null"
    )

    return {
        "name":"SUID Binaries",
        "data":suid
    }
