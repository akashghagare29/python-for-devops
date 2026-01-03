import psutil

def get_system_metrics():
    """
        Retrieve system metrics such as CPU and memory usage.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    cpu_threshold = 10

    status = "High CPU usage" if cpu_usage > cpu_threshold else "Normal CPU usage"

    return {
        "cpu_threshold": cpu_threshold,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_percent,
        "disk_usage": disk_usage,
        "status": status
    }