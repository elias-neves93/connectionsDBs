import argparse
#import cx_Oracle
import pymongo
import json

version = 0.1

class Query(object):
    def __init__(self, db, address, user, password, database, query):
        self.__db = db
        self.__address = address
        self.__user = user
        self.__password = password
        self.__database = database
        self.__query = query


    @property
    def db(self):
        return self.__db.lower()

    @property
    def address(self):
        return self.__address

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def query(self):
        return self.__query

    @property
    def database(self):
        return self.__database

    @property
    def query(self):
        return self.__query







def main():

    # Fazendo os parses para pegar as infos.
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", metavar="Str", help="DB Name", type=str, required=True)
    parser.add_argument("--address", metavar="Str", help="Address", type=str, required=True)
    parser.add_argument("--user", metavar="Str", help="User for connection", type=str, required=False)
    parser.add_argument("--password", metavar="Str", help="Password", type=str, required=False)
    parser.add_argument("--database", metavar="Str", help="database", type=str, required=False)
    parser.add_argument("--query", metavar="Str", help="Query", type=str, required=True)

    args = parser.parse_args()

    # Atribuindo os parses nas variaveis
    db = args.db
    address = args.address
    user = args.user
    password = args.password
    database = args.database
    query = args.query

    # create a Object
    query = Query(db, address, user, password, database, query)

    if query.db == 'mongodb':
        #with open(query.query, "r") as f:

        query = {'name': 'Elias'}
        connection = pymongo.MongoClient("mongodb://127.0.0.1")
        db = connection.test
        names = db.names

        try:
            cursor = names.find(query).count()
        except Exception as e:
            print ("Unexpected error:", type(e), e)

        print(cursor)
        #for i in cursor:
        #    print (i)

    

if __name__ == "__main__":
    main()
