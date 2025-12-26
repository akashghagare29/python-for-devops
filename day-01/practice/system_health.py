import psutil

def check_system_health():
    cpu_threshold = int(input("Enter CPU usage threshold (in percentage): "))
    disk_threshold = int(input("Enter disk usage threshold (in percentage): "))
    memory_threshold = int(input("Enter memory usage threshold (in percentage): "))

    print("Checking system health... \n" )
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_usage = psutil.disk_usage('/').percent
    memory_usage = psutil.virtual_memory().percent

    if cpu_usage > cpu_threshold:
        print(f"===========CPU usage metrics=======") 
        print(f"CPU usage is: {cpu_usage}%")
        print(f"CPU usage is above threshold: {cpu_usage}% \n")
    if disk_usage > disk_threshold:
        print(f"===========Disk usage metrics=======")
        print(f"Disk usage is: {disk_usage}%")
        print(f"Disk usage is above threshold: {disk_usage}% \n")
    if memory_usage > memory_threshold:
        print(f"===========Memory usage metrics=======")
        print(f"Memory usage is: {memory_usage}%")
        print(f"Memory usage is above threshold: {memory_usage}%")

check_system_health()