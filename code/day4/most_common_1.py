from pathlib import Path

ip_list = Path("ip_addresses.txt").read_text().split()
most_common = {}
for ip, port in (string.split(":") for string in ip_list):
    if ip not in most_common:
        most_common[ip] = 0
    most_common[ip] += 1

for k, v in sorted(most_common.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(k, v)
