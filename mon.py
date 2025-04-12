from pymongo import MongoClient
db_password = "Babalola@alltech1"
connection_string = "mongodb+srv://Azbabdesignhub:Babalola@alltech1@azbabdesignhub.rke6b.mongodb.net/"

client = MongoClient(connection_string)
db = client.list_database_names()
print(db)