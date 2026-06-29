def generate_report(
        request_count,
        failed_attempts,
        admin_access,
        not_found_count,
        success_count
):
    total_requests = sum(request_count.values())
    unique_ips = len(request_count)
    total_failed_logins = sum(failed_attempts.values())
    total_404_errors = sum(not_found_count.values())
    total_admin_attempts = len(admin_access)

    report = []

    report.append("=" * 50)
    report.append("             LOG ANALYSIS REPORT")
    report.append("=" * 50)

    report.append("")
    report.append("Summary")
    report.append("-------")
    report.append(f"Total Requests: {total_requests}")
    report.append(f"Unique IP Addresses: {unique_ips}")
    report.append(f"Successful Requests: {success_count}")
    report.append(f"Failed Login Attempts: {total_failed_logins}")
    report.append(f"404 Errors: {total_404_errors}")
    report.append(f"Admin Access Attempts: {total_admin_attempts}")

    report.append("")
    report.append("-" * 50)

    report.append("")
    report.append("Request Count")
    report.append("-------------")
    for ip, count in request_count.items():
        word = "request" if count == 1 else "requests"
        report.append(f"{ip} -> {count} {word}")

    report.append("")
    report.append("-" * 50)

    report.append("")
    report.append("Failed Login Attempts")
    report.append("---------------------")
    if failed_attempts:
        for ip, count in failed_attempts.items():
            word = "attempt" if count == 1 else "attempts"
            report.append(f"{ip} -> {count} {word}")
    else:
        report.append("None")

    report.append("")
    report.append("-" * 50)

    report.append("")
    report.append("404 Errors")
    report.append("----------")
    if not_found_count:
        for ip, count in not_found_count.items():
            report.append(f"{ip} -> {count}")
    else:
        report.append("None")

    report.append("")
    report.append("-" * 50)

    report.append("")
    report.append("Admin Access Attempts")
    report.append("---------------------")
    if admin_access:
        for ip in admin_access:
            report.append(ip)
    else:
        report.append("None")

    output = "\n".join(report)

    print(output)

    with open("reports/report.txt", "w") as file:
        file.write(output)