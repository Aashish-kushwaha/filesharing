import pymongo
from urllib.parse import quote_plus

username = 'kushwahaashu444'
password = 'ashu'

# Escape the username and password using quote_plus
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Construct the MongoDB connection string
connection_string = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.g247luz.mongodb.net/"

print(connection_string)

# Create a MongoDB client
conn = pymongo.MongoClient(connection_string)

db=conn.filesharing
