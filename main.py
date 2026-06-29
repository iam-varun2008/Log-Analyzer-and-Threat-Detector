from utils import LOG_FILE
from parser import parse_log_entry
from detector import (detect_failed_logins, detect_admin_access, count_requests, detect_404_errors,count_successful_requests)
from report import generate_report

def main():

    with open(LOG_FILE, 'r') as file:
        content = file.readlines()

    parsed_logs = []

    for line in content:
        log = parse_log_entry(line)
        parsed_logs.append(log)
    failed_attempts = detect_failed_logins(parsed_logs)
    admin_access = detect_admin_access(parsed_logs)
    request_count = count_requests(parsed_logs)
    not_found_count = detect_404_errors(parsed_logs)
    success_count = count_successful_requests(parsed_logs)

    generate_report(
        request_count,
        failed_attempts,
        admin_access,
        not_found_count,
        success_count
    )


if __name__ == "__main__":
    main()