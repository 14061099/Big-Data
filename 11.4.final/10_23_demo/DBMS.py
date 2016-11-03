import pymongo

class DBMS(object):

    def __init__(self,host,ip):
        self.__connect = pymongo.MongoClient(host,ip)

    def __connect_to_db(self,stock_name):
         self.__db = self.__connect.get_database(stock_name)
         self.__db.authenticate("hadoop","BUAAQuant",mechanism='MONGODB-CR')


    def get_col(self,stock_name,col_name):
        self.__connect_to_db(stock_name)
        if col_name in self.__db.collection_names():
            self.col = self.__db.get_collection(col_name)
            if 'datetime_1' not in list(self.col.index_information()):
                result = self.col.create_index([('datetime',pymongo.ASCENDING)],unique=True)
            return self.col
        else:
            raise Exception("Illegal collection name")


