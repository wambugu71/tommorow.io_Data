import  os
from google.cloud import  storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dsail-misc-new.json"
import  requests
import  json
import  pandas as  pd
from datetime  import  datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
file_name = f"Data_{formatted_datetime}.json"
url = "https://api.tomorrow.io/v4/weather/forecast?location=-0.416667,36.950000&apikey=Uuww83qb9dv3Ehj9L3ugaO1PF4DD3D4Z"
response = requests.get(url)
file   =  open(file_name, "wb")
file.write(response.content)
# features added.
responseData = response.json()
data = responseData["timelines"]["minutely"]
df = pd.DataFrame(data)
data_values = []
for i in range(list(df["values"].shape)[0]):
  data_values.append(df["values"][i].values())
data = pd.DataFrame(data_values, columns = df["values"][0].keys())
data["time"] = df["time"]
path2  =  f"weather{formatted_datetime}.csv"

data.to_csv(path2)

print(f"Data has been written to {file_name}")
storage_client = storage.Client()
bucket_name = "tomorrow_io"
#bucket = storage_client.create_bucket(bucket_name)\
#my_bucket   = list(storage_client.list_buckets())
#print(my_bucket)
bucket_storage = storage_client.get_bucket("tomorrow_io")
#print(bucket_storage)

# upload  file to bucket
def  upload_file(file):
    bucket = storage_client.get_bucket("tomorrow_io")
    blob = bucket.blob(file)
    blob.upload_from_filename(file)
    print("File  uploded  succesfully")

upload_file(path2)

