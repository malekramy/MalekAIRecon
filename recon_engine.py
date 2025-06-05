
from helpers import print_colored, validate_domain

def dns_lookup(target):
    print_colored(f"Performing DNS lookup for {target}...", "yellow")
    subprocess.call(["nslookup", target])

def subdomain_enum(target):
    print_colored(f"Enumerating subdomains for {target}...", "yellow")
    # Simple placeholder: print common subdomains
    common_subs = ["www", "mail", "ftp", "vpn", "dev"]
    for sub in common_subs:
        print(f"{sub}.{target}")

def port_scan(target):
    print_colored(f"Scanning top ports on {target}...", "yellow")
    top_ports = [22, 80, 443, 8080, 3306]
    for port in top_ports:
        result = subprocess.run(["nc", "-zv", target, str(port)], capture_output=True, text=True)
        if "succeeded" in result.stderr or "open" in result.stdout:
            print_colored(f"Port {port} is OPEN", "green")
        else:
            print_colored(f"Port {port} is closed or filtered", "red")

def recon_engine():
    target = input("Enter target domain or IP: ").strip()
    if not validate_domain(target):
        print_colored("Invalid domain or IP address!", "red")
        return
    dns_lookup(target)
    subdomain_enum(target)
    port_scan(target)
