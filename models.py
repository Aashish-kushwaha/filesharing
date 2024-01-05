import pymongo
from urllib.parse import quote_plus

username = 'kushwahaashu444'
password = 'ashu'


escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

connection_string = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.g247luz.mongodb.net/"

print(connection_string)

conn = pymongo.MongoClient(connection_string)

db=conn.filesharing
