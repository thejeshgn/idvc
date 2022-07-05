import csv
import couchdb
import os

idvc_db_full_url = str(os.environ.get("IDVC_DB"))
couchdb_db_name = "idvc"
couch = couchdb.Server(idvc_db_full_url)
database = couch[couchdb_db_name]

CSV_PATH = "../raw/raw.csv"
ALLOW_UPDATE = False
input_file = csv.DictReader(open(CSV_PATH), delimiter=";")

def load_data():
    for row in input_file:
        data = {}        
        #print(row)
        ## if you want the approved rows then check
        ## data["_validation_status"] == "validation_status_approved"
        data["_id"] = row["_id"]
        data["type"] = "data"
        data["name_of_restaurant"] = row["Name_of_Restaurant"]
        data["idly_two"] = None if row["Idly_Two"] == "" else int(row["Idly_Two"])
        data["masala_dosa"] = None if row["Masala_Dosa"] == "" else int(row["Masala_Dosa"])
        data["vada"] = None if row["Vada"] == "" else int(row["Vada"]) 
        data["regular_coffee"] = None if row["Regular_Coffee"] == "" else int(row["Regular_Coffee"])
        data["mini_coffee"] = None if row["Mini_Coffee"] == "" else int(row["Mini_Coffee"])
        data["ac"] = row["AC"]
        data["type_of_restaurant"] = row["Type_of_Restaurant"].split(",")
        data["lat"] = str(row["_Location_latitude"])
        data["lng"] = str(row["_Location_longitude"])
        data["submission_time"] = (row["_submission_time"]).replace(" ", "T") + ".00+05:30"
        data["submitted_by"] = row["_submitted_by"]
        print("==================================================")
        print(data)
        upsert_data(data)



def upsert_data(data):
    if data:
        _id = data["_id"]
        try:
            if database[_id] and ALLOW_UPDATE:
                print("##### UPDATING #####")
                existing_data = database[_id]
                _rev = existing_data["_rev"]
                data["_rev"] = _rev
                database.save(data)
                print("saved",data)
        except couchdb.http.ResourceNotFound:
                print("##### ADDING #####")
                database.save(data)
                print("saved", data)




if __name__ == "__main__":
    load_data()
