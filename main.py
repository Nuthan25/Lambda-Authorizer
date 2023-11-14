import boto3
import time
import uuid

s3 = boto3.client('s3')

bucket_name = 'a1ses'
object_key = '100 meg.xlsx'

# Measure the time it takes to download the object
tmp_file = f"{uuid.uuid4()}.csv"

download_start_time = time.time()
s3.download_file(bucket_name, object_key, tmp_file)
download_end_time = time.time()

# Calculate download speed in Mbps
print("download", time.time() - download_start_time)
# download_speed = (download_end_time - download_start_time) / (1024 * 1024)

# # Log the results
# print(f"Download Speed for '{object_key}': {download_speed:.2f} Mbps")

# Upload the downloaded file to the Lambda /tmp folder
# upload_tmp_path = f'/tmp/uploaded_{object_key.replace("/", "_")}'
download_start_time1 = time.time()
s3.upload_file(tmp_file, bucket_name, f"{uuid.uuid4()}from local.csv")
download_end_time1 = time.time()
print("upload", time.time() - download_start_time1)