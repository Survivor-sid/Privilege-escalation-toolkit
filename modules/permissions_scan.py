import subprocess

def run():

    writable = subprocess.getoutput(
    "find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null | head"
    )

    return {
        "name":"World Writable Files",
        "data":writable
    }
