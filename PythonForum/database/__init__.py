import os
from mongoengine import connect

# Try and connect to the development server.
# For security reasons the server location isn't pushed with the project.
# Try and import that location here
try:
    from db_config import db_uri as host
except ImportError:
    # On failing to import that connection look for an environ variable to tell us where to connect
    # Failing that just try for a local host connection
    host = os.environ.get("PF_MONGO_SERVER", "mongodb://localhost/pf")

users_db = connect("users", host=host)
forum = connect("forum", host=host)