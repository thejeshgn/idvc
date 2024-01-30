import csv
import os
import pandas as pd
from datetime import datetime
dt = datetime.now()

## THIS IS A HACK. WILL UPDATE LATER

CSV_PATH = "../raw/raw.csv"
ALLOW_UPDATE = False
input_file = csv.DictReader(open(CSV_PATH), delimiter=";")


def simple_stat(year, current=True):
    data_rows = []
    for row in input_file:
        # This is bad but its fine for now
        if str(year) in row["_submission_time"]:
            #print(row)
            ## if you want the approved rows then check
            ## data["_validation_status"] == "validation_status_approved"
            data = {}        
            #data["_id"] = row["_id"]
            #data["type"] = "data"
            #data["name_of_restaurant"] = row["Name_of_Restaurant"]
            data["idly_two"] = None if row["Idly_Two"] == "" else int(row["Idly_Two"])
            data["masala_dosa"] = None if row["Masala_Dosa"] == "" else int(row["Masala_Dosa"])
            data["vada"] = None if row["Vada"] == "" else int(row["Vada"]) 
            data["regular_coffee"] = None if row["Regular_Coffee"] == "" else int(row["Regular_Coffee"])
            #data["mini_coffee"] = None if row["Mini_Coffee"] == "" else int(row["Mini_Coffee"])
            #data["ac"] = row["AC"]
            #data["type_of_restaurant"] = row["Type_of_Restaurant"].split(",")
            #data["lat"] = str(row["_Location_latitude"])
            #data["lng"] = str(row["_Location_longitude"])
            #data["submission_time"] = (row["_submission_time"]).replace(" ", "T") + ".00+05:30"
            #data["submitted_by"] = row["_submitted_by"]
            data_rows.append(data)

    df = pd.DataFrame(data_rows)
    aggregate1 = df.agg(["max","min","mean","median","std"])
    aggregate1 = aggregate1.round(decimals = 2)
    # Because - ValueError: cannot combine transform and aggregation operations
    aggregate2 = df.agg(["mode"])
    
    document = {}
    if current:
        document["_id"] = "current_stats"
        document["type"] = "stat"
        document["last_updated_on"] = dt.astimezone().isoformat()
        for item in ["idly_two","masala_dosa","vada","regular_coffee"]:
            doc = aggregate1[item]
            doc["mode"] = aggregate2[item]["mode"].iloc[0]
            doc = doc.to_dict()
            doc["sd"] = doc["std"]
            del doc["std"]
            document[item] = doc        
        print(document)
    else:
        document["_id"] = "stats_{year}".format(year=year)
        document["type"] = "stat"
        document["last_updated_on"] = dt.astimezone().isoformat()
        for item in ["idly_two","masala_dosa","vada","regular_coffee"]:
            doc = aggregate1[item]
            doc["mode"] = aggregate2[item]["mode"].iloc[0]
            doc = doc.to_dict()
            doc["sd"] = doc["std"]
            del doc["std"]
            document[item] = doc        
        print(document)
    
if __name__ == "__main__":
    simple_stat(year=2024, current=True)
