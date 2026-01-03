from datetime import datetime, timezone, timedelta
import boto3

def get_bucket_info():
    """
        Function to retrieve S3 bucket information.
    """

    s3_client = boto3.client("s3")
    buckets = s3_client.list_buckets()["Buckets"]
    current_date = datetime.now(timezone.utc).astimezone()
    print(f"Current Time: {current_date}")

    new_buckets = []  # Initialize an empty list to store new bucket names
    old_buckets = []  # Initialize an empty list to store old bucket names

    for bucket in buckets:  # For loop 
        bucket_name = bucket["Name"]    # Store bucket name
        creation_date = bucket["CreationDate"]  # Date and time
        days_ago_10 = current_date - timedelta(days=10)

        if creation_date < days_ago_10:
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)

    return {
        "Current Time": current_date,
        "Total Buckets": len(buckets),
        "New Buckets": len(new_buckets),
        "Old Buckets": len(old_buckets),
        "New Bucket Names": new_buckets,
        "Old Bucket Names": old_buckets
    }
