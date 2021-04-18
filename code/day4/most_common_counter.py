from pathlib import Path
from collections import Counter

ip_list = Path("ip_addresses.txt").read_text().split()
addresses = [text.split(":")[0] for text in ip_list]
for ip, count in Counter(addresses).most_common(5):
    print(ip, count)
