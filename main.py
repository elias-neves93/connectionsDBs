import argparse
import cx_Oracle
import pymongo

version = 0.1

class Query(object):
    def __init__(self, name, address, port, user, password, database, query):
        self.__name = name
        self.__address = address
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database
        self.__query = query


    @property
    def name(self):
        return self.__name.lower()

    @property
    def address(self):
        return self.__address

    @property
    def port(self):
        return self.__port

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def database(self):
        return self.__database

    @property
    def query(self):
        return self.__query


    def run_query_oracle(self, name, address, port, user, password, database, query) -> str:

        db = cx_Oracle.connect("{0}/{1}@{2}:{3}/{4}".format(self.user, self.password, self.address, self.port, self.database))
        cur = db.cursor()
        with open(self.query, 'r', encoding='utf-8') as sql:
            sql = sql.read().replace(";"," ") # remove any ";" on file query.sql
            cur.execute(sql)
            res = cur.fetchall()
            for i in res:
                final = i[0]
                cur.close()
                db.close()
        return final



def main():

    # Fazendo os parses para pegar as informações.
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", metavar="Str", help="DB Name", type=str, required=True)
    parser.add_argument("--address", metavar="Str", help="Address", type=str, required=True)
    parser.add_argument("--port", metavar="Int", help="port", type=str, required=True)
    parser.add_argument("--user", metavar="Str", help="User for connection", type=str, required=False)
    parser.add_argument("--password", metavar="Str", help="Password", type=str, required=False)
    parser.add_argument("--database", metavar="Str", help="database", type=str, required=False)
    parser.add_argument("--query", metavar="Str", help="Query", type=str, required=True)

    args = parser.parse_args()

    # Atribuindo os parses nas variaveis
    name = args.name
    address = args.address
    port = args.port
    user = args.user
    password = args.password
    database = args.database
    query = args.query

    # create a Object
    r = Query(name, address, port, user, password, database, query)

    if r.name == 'oracle':
        try:
            response = r.run_query_oracle(r.name, r.address, r.port, r.user, r.password, r.database, r.query)
            print (response)
        except Exception as e:
            print ("Unexpected error:", type(e), e)



if __name__ == "__main__":
    main()
