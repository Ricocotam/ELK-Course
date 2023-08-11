import requests
import time

uri = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=1471"
while True:
    resp = requests.get(uri)
    data = resp.json()
    print(data["nhits"])
    for r in data["records"]:
        name = r["fields"]["name"]
        code = r["fields"]["stationcode"]
        ebike = r["fields"]["ebike"]
        mecha = r["fields"]["mechanical"]
        capacity = r["fields"]["capacity"]
        date = r["fields"]["duedate"]
        timestamp = r["record_timestamp"]
    
        print(f"{timestamp}\tStation {name} with code {code} has {ebike} ebikes, {mecha} bikes out of {capacity} possible at {date}")
        
        coord = r["fields"]["coordonnees_geo"]
        print(f"{name} code {code} at {coord}")
    time.sleep(1)
