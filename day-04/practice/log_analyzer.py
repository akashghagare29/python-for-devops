import json

def read_logs():
    with open("app.log", "r") as logs:
        return logs.readlines()  # Read all lines from the log file

def analyze_logs(log_lines):    # Analyzes log lines and prints a summary of log levels
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
def write_json(log_count):
    with open("log_summary.json", "w+") as json_file:
        print(f"Log Summary: {json.dumps(log_count)}")  # Print log counts in JSON format
        json.dump(log_count, json_file, indent=4)   # Write log counts to a JSON file

log_lines = read_logs()  # Read log lines from the log file
log_count = analyze_logs(log_lines) # Analyze the log lines to get counts
write_json(log_count)   # Write the log counts to a JSON file