from modules import system_info
from modules import suid_scan
from modules import capabilities_scan
from modules import permissions_scan
from modules import cron_scan
from modules import sudo_scan
from modules import service_scan
from modules import kernel_scan

from core.report_writer import write_report

from colorama import Fore, Style, init
import time

init(autoreset=True)


def banner():

    print(Fore.CYAN + Style.BRIGHT + """
=========================================
 Linux Privilege Escalation Toolkit
 Automated Security Enumeration Scanner
=========================================
""")


def run_step(step_name, func):

    print(Fore.CYAN + Style.BRIGHT + f"[+] Running {step_name} scan...")

    start = time.time()

    result = func()

    end = time.time()

    print(
        Fore.GREEN + Style.Bright
        + f"[✔] {step_name} completed in {round(end-start,2)}s\n"
    )

    return result


banner()

results = []

results.append(run_step("System Info", system_info.run))
results.append(run_step("SUID Binaries", suid_scan.run))
results.append(run_step("Linux Capabilities", capabilities_scan.run))
results.append(run_step("Writable Files", permissions_scan.run))
results.append(run_step("Cron Jobs", cron_scan.run))
results.append(run_step("Sudo Rules", sudo_scan.run))
results.append(run_step("Services", service_scan.run))
results.append(run_step("Kernel", kernel_scan.run))


print(Fore.YELLOW + Style.BRIGHT + "[+] Generating report...\n")

write_report(results)

print(Fore.GREEN + "\n[✔] Report generation complete")
print(Fore.GREEN + "[✔] Report is saved at: reports/report.txt created")
print(Fore.GREEN + "[✔] reports/report.json created\n")

print(
    Fore.CYAN
    + Style.BRIGHT
    + "=== Scan Finished Successfully ===\n"
)
