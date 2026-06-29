import re

def parse_log_entry(log_entry):
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?) (.*?) (.*?)" (\d+) (\d+)'

    match = re.match(pattern, log_entry)

    if match:
        return {
            "ip": match.group(1),
            "timestamp": match.group(2),
            "method": match.group(3),
            "url": match.group(4),
            "protocol": match.group(5),
            "status": int(match.group(6)),
            "size": int(match.group(7))
        }