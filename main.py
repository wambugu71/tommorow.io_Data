
import pyrebase
import  requests
import  json
from datetime  import  datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
file_name = f"Data_{formatted_datetime}.json"
url = "https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=Uuww83qb9dv3Ehj9L3ugaO1PF4DD3D4Z"
response = requests.get(url)
file   =  open(file_name, "wb")
file.write(response.content)
print(f"Data has been written to {file_name}")
config = {
  "apiKey": "AIzaSyDmVHSWHzIJGL-tMzknE90TNGjTWfm9bcs",
  "authDomain": "weatherdata-51a1f.firebaseapp.com",
  "databaseURL": "https://weatherdata-51a1f-default-rtdb.firebaseio.com",
  "storageBucket": "weatherdata-51a1f.appspot.com",
  "serviceAccount": "weatherdata-51a1f-firebase-adminsdk-n0c0k-6b36a3a194.json"
}



firebase = pyrebase.initialize_app(config)

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_local =file_name


# Upload
storage.child(file_name).put(path_local)

# Download
#storage.child(path_on_cloud).download("<file_downloaded>")
