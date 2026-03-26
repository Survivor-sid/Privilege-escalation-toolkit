import json
import os

from core.risk_engine import classify

from colorama import Fore, Style, init

init(autoreset=True)


# color mapping for severity
severity_colors = {

    "CRITICAL": Fore.RED + Style.BRIGHT,
    "HIGH": Fore.RED,
    "MEDIUM": Fore.YELLOW,
    "LOW": Fore.BLUE
}


def write_report(results):

    os.makedirs("reports", exist_ok=True)

    report_txt = open("reports/report.txt", "w")

    report_json = []


    for module in results:

        severity, mitigation = classify(module["data"])


        # terminal color
        color = severity_colors.get(severity, Fore.WHITE)


        print(
            color +
            f"[{severity}] {module['name']}"
        )


        report_txt.write("\n" + "="*60 + "\n")

        report_txt.write(f"MODULE: {module['name']}\n")

        report_txt.write(f"SEVERITY: {severity}\n")

        report_txt.write(f"MITIGATION: {mitigation}\n\n")

        report_txt.write(module["data"] + "\n")


        report_json.append({

            "module": module["name"],

            "severity": severity,

            "mitigation": mitigation,

            "findings": module["data"]

        })


    report_txt.close()


    with open("reports/report.json", "w") as f:

        json.dump(report_json, f, indent=4)
