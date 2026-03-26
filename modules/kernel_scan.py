import subprocess

def run():

    kernel = subprocess.getoutput("uname -r")

    data = f"""
Kernel Version:
{kernel}

Check:
https://www.exploit-db.com
"""

    return {
        "name":"Kernel Version",
        "data":data
    }
