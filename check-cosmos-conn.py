#!/usr/bin/env python3
# replace username/password/db_url
# this script just allows you to check connectivity/access to a CosmosDB. Occasionally they can have IP whitelisting in place which can block access.

# import datetime & random
import random

# import the MongoClient class of the PyMongo library
from pymongo import MongoClient

# import ObjectID from MongoDB's BSON library
# (use pip3 to install bson)
from bson import ObjectId

# create a client instance of the MongoClient class
# readwrite conn string
mongo_client = MongoClient('mongodb://username:password@db_url:db_port/?ssl=true&replicaSet=globaldb')

# create database and collection instances
db = mongo_client["db_name"]
col = db["col_name"]

# check if collection has documents
total_docs = col.count_documents( {} )
print (col.name, "has", total_docs, "total documents.")

# Query to get the docs
#docs = col.find({ "_id": ObjectId("5d5e1dc70e7bf70001a14b11")})

# Query to get all the docs
docs = col.find()

