import json

class LogAnalyzer:
    """
        Class to analyze log files and summarize log levels.
    """

    def __init__(self, file_name, output_file):
        self.file_name = file_name
        self.output_file = output_file

    def read_logs(self):
        with open(self.file_name, "r") as logs:
            return logs.readlines()  # Read all lines from the log file

    def analyze_logs(self, log_lines):    # Analyzes log lines and prints a summary of log levels
        log_count = {   # Dictionary to hold counts of each log level
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }

        for line in log_lines:  # Iterate through each log line
            if "INFO" in line:
                log_count.update({"INFO": log_count["INFO"] + 1})   # Increment INFO count
            elif "WARNING" in line:
                log_count.update({"WARNING": log_count["WARNING"] + 1})   # Increment WARNING count
            elif "ERROR" in line:
                log_count.update({"ERROR": log_count["ERROR"] + 1})  # Increment ERROR count
            pass

        return log_count

    # Print the log level counts in JSON format
    def write_json(self, log_count):
        with open(self.output_file, "w+") as json_file:
            print(f"Log Summary: {json.dumps(log_count)}")  # Print log counts in JSON format
            json.dump(log_count, json_file, indent=4)   # Write log counts to a JSON file

log_analyzer = LogAnalyzer("app.log", "log_summary.json")
log_lines = log_analyzer.read_logs()  # Read log lines from the log file
log_count = log_analyzer.analyze_logs(log_lines) # Analyze the log lines to get counts
log_analyzer.write_json(log_count)   # Write the log counts to a JSON file