
import pyrebase
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
config = {
  "apiKey": "AIzaSyDmVHSWHzIJGL-tMzknE90TNGjTWfm9bcs",
  "authDomain": "weatherdata-51a1f.firebaseapp.com",
  "databaseURL": "https://weatherdata-51a1f-default-rtdb.firebaseio.com",
  "storageBucket": "weatherdata-51a1f.appspot.com",
  "serviceAccount": "weather.json"
}



firebase = pyrebase.initialize_app(config)

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_local =file_name


# Upload
storage.child(path2).put(path2)

# Download
#storage.child(path_on_cloud).download("<file_downloaded>")
