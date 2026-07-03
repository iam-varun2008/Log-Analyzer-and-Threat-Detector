# Log Analyzer & Threat Detector

A Python-based cybersecurity project that analyzes Apache access logs, detects suspicious activities, and generates a detailed security report.

A larger synthetic Apache-style sample log is included in `sample_data/access.log` to demonstrate normal traffic, repeated failed login attempts, admin access attempts, suspicious paths, unusual status codes, and basic injection-like URL patterns.

A sample generated report is included in `reports/report.txt`.

## Features

* Parses Apache access logs using Regular Expressions (Regex).
* Extracts important request information:

  * IP Address
  * Timestamp
  * HTTP Method
  * URL
  * Protocol
  * Status Code
  * Response Size
* Detects repeated failed login attempts (401 responses).
* Detects requests to sensitive admin pages.
* Counts requests made by each IP address.
* Detects 404 (Not Found) errors.
* Generates a formatted security report.
* Automatically saves the report as `reports/report.txt`.



## Project Structure

```text
LogAnalyzer/
│
├── main.py              # Entry point of the application
├── parser.py            # Parses raw log entries into structured data
├── detector.py          # Detects suspicious activity from parsed logs
├── report.py            # Generates and saves the analysis report
├── utils.py             # Stores shared constants
├── requirements.txt     # Project dependency information
├── sample_logs/
│   └── access.log       # Sample Apache access log file
├── reports/
│   └── report.txt       # Generated security report
└── README.md            # Project documentation
```




## Technologies Used

* **Python 3**
* **Regular Expressions (Regex)**
* **File Handling**
* **Dictionaries & Lists**
* **Functions & Modular Programming**
* **Git & GitHub**

## How It Works

1. Reads an Apache access log file.
2. Parses each log entry using Regular Expressions.
3. Converts each log entry into a structured Python dictionary.
4. Detects suspicious activities such as:

   * Multiple failed login attempts
   * Admin page access attempts
   * 404 errors
5. Generates a formatted security report.
6. Saves the report to `reports/report.txt`.



## How to Run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd LogAnalyzer
```

3. Run the application:

```bash
python main.py
```

4. The program will:

   * Analyze the sample log file.
   * Display the security report in the terminal.
   * Save the report to `reports/report.txt`.

## Sample Input and Output

This project includes a larger synthetic Apache-style sample log in `sample_logs/access.log`.

A sample generated report is included in `reports/report.txt`.

The report includes:
- total request count
- unique IP addresses
- failed login attempts
- 404 errors
- admin access attempts
- repeated suspicious activity by IP



## Skills Demonstrated

This project demonstrates practical software engineering and cybersecurity concepts, including:

* Regular Expression (Regex) based log parsing
* Modular software architecture
* File handling in Python
* Data processing using dictionaries and lists
* Cybersecurity log analysis
* Threat detection techniques
* Report generation
* Git and GitHub workflow

## Limitations

This project uses rule-based detection and is intended for basic log analysis and learning purposes. It does not use machine learning and does not replace professional security monitoring tools.

The detection results depend on the log format and the rules defined in the program.

## Ethical Use

This project is for educational and defensive security purposes only. It should be used only with log files from systems owned by the user or where permission has been granted.


## Future Improvements

Future versions of this project could include:

* Detection of SQL Injection attempts
* Detection of Cross-Site Scripting (XSS) attacks
* Detection of Directory Traversal attacks
* Support for multiple log formats
* Export reports as PDF or HTML
* Interactive dashboard for visualization
* Real-time log monitoring

## Author

**Nandi Varun Reddy**

This project was built as part of a cybersecurity portfolio to demonstrate Python programming, software engineering, and security analysis skills.
