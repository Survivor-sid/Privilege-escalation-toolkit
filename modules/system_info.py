import subprocess, os

def run():

    data = f"""
User: {os.getlogin()}

ID:
{subprocess.getoutput("id")}

Kernel:
{subprocess.getoutput("uname -a")}

OS:
{subprocess.getoutput("cat /etc/os-release")}
"""

    return {"name":"System Info","data":data}
