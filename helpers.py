import re
from colorama import Fore, Style, init

init(autoreset=True)

def print_colored(text, color):
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "cyan": Fore.CYAN
    }
    print(colors.get(color, Fore.WHITE) + text + Style.RESET_ALL)

def validate_domain(domain):
    # Simple regex for domain or IPv4 validation
    domain_regex = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    ip_regex = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    if re.match(domain_regex, domain) or re.match(ip_regex, domain):
        return True
    return False
