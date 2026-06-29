def detect_failed_logins(logs):
    failed_attempts = {}

    for log in logs:
        if log["status"] == 401:
            ip = log["ip"]

            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

    return failed_attempts


def detect_admin_access(logs):
    admin_access = []
    for log in logs:
        if log["url"] == "/admin":
            admin_access.append(log["ip"])
    return admin_access

def count_requests(logs):
    request_count = {}

    for log in logs:
        ip = log["ip"]

        if ip in request_count:
            request_count[ip] += 1
        else:
            request_count[ip] = 1

    return request_count

def detect_404_errors(logs):
    not_found_count = {}
    for log in logs:
        if log["status"] == 404:
            ip = log["ip"]

            if ip in not_found_count:
                not_found_count[ip] += 1
            else:
                not_found_count[ip] = 1

    return not_found_count

def count_successful_requests(logs):
    success_count = 0

    for log in logs:
        if log["status"] == 200:
            success_count += 1

    return success_count