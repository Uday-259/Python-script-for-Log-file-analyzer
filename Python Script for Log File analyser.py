import re
from collections import Counter

LOG_FILE = "access.log"  # sample Apache/Nginx log file

def analyze_logs():
    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    # Count 404 errors
    error_404 = sum(1 for line in logs if " 404 " in line)

    # Most requested pages
    pages = [re.search(r'\"[A-Z]+\s([^\s]+)', line).group(1)
             for line in logs if re.search(r'\"[A-Z]+\s([^\s]+)', line)]
    top_pages = Counter(pages).most_common(5)

    # Top IP addresses
    ips = [line.split()[0] for line in logs if line.strip()]
    top_ips = Counter(ips).most_common(5)

    print("\n===== Log Analysis Report =====")
    print(f"Total 404 Errors: {error_404}")
    print("\nTop 5 Requested Pages:")
    for page, count in top_pages:
        print(f"{page} -> {count} requests")

    print("\nTop 5 IP Addresses:")
    for ip, count in top_ips:
        print(f"{ip} -> {count} requests")

if __name__ == "__main__":
    analyze_logs()
