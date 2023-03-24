import sys
import pymongo
import config

def get_client():
    client = pymongo.MongoClient(
        config.mongodb_url)
        # "mongodb+srv://Melodylovescat:Zxw981120@cluster0.nuvqv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    return client


def t1():

    c = get_client()
    print(list(c.list_databases()))


if __name__ == "__main__":
    t1()