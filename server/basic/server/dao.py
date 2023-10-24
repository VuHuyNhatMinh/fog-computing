import psycopg2
# import puchikarui
# from logs import Log
 
class PostgresDAO:
    """Postgres Data Access Object provides API to work with Postgres Database"""
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.__dbname = dbname
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port

    def _connect(self):
        try: 
            self.__conn = psycopg2.connect(
                self.__dbname,
                self.__user,
                self.__password,
                self.__host,
                self.__port,
            )
            self.__cursor = self.__conn.cursor()
        except psycopg2.Error as error:
            self.__logger.exception(error)

    def _do(self, query):
        try:
            self.__cursor.execute(query)
            self.__conn.commit()
        except psycopg2.Error as error:
            self.__logger.exception(error)

    def _close(self):
        self.__conn.close()
        self.__cursor.close()

    # CREATE
    def createTable(self, tableName, col):
        """Create a Table"""
        try:
            self._connect()
            self._do(f"CREATE TABLE {tableName} ({col});")
            self.__logger.info("Created table successfully")
        except (Exception, psycopg2.Error) as error:
            self.__logger.info("Creted table unsuccessfully")
            self.__logger.exception(error)
        finally:
            self._close()
    
    # RETRIEVE
    def listAllTables(self):
        """Show all tables in database"""
        try: 
            self._connect()
            self._do("SELECT * FROM pg_catalog.pg_tables;;")
            tables = self.__cursor.fetchall()
            print(tables) if len(tables) != 0 else print(None)
        finally:
            self._close()
 

    def listAllColumns(self, tableName):
        try:
            self._connect()
            self.__curosr.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_schema='public' AND table_name='{tableName}'")
            colNames = self.__cursor.fetchall()
            print(colNames) if len(colNames) != 0 else print(None) 
        finally:
            self._close()

    def listAllRecords(self, tableName):
        try:
            self._connect()
            self._do(f"SELECT * FROM {tableName};")
            res = self.__cursor.fetchall()
            #self.__logger.debug(res)
            self.__logger.info("Retrieved all values successfully")
        except (Exception, psycopg2.Error) as error:
            self.__logger.info("Retrieved all values unsuccessfully")
            self.__logger.exception(error)
        finally:
            self._close()
    
    # UPDATE
    def insertOneRecord(self, tableName, colValues):
        try:
            self._connect()
            self._do(f"INSERT INTO {tableName} VALUES ({colValues});")
            self.__logger.info("Inserted a record successfully")
        except (Exception, psycopg2.Error) as error:
            self.__logger.info("Insertted a record unsuccessfully")
            self.__logger.exception(error)            
        finally:
            self._close()
    # DISCLAIMED: These functions have not been tested
    # TODO: use rowid
    def updateOneRecord(self, tableName, new, condition):
        try:
            self._connect()
            self._do(f"UPDATE {tableName} SET {new} WHERE {condition}")
            self.__logger.info("Updated a record successfully")
        except (Exception, psycopg2.Error) as error:
            self.__logger.info("Updated a record unsuccessfully")
            self.__logger.exception(error)
        finally:
            self._close()
    
    # DELETE
    def deleteOneRecord(self, tableName, condition):
        try:
            self._connect()
            self._do(f"DELETE FROM {tableName} WHERE {condition}")
            self.__logger.info("Deleted a record successfully")
        except (Exception, psycopg2.Error) as error:
            self.__logger.info("Deleted a record unsuccessfully")
            self.__logger.exception(error)
        finally:
            self._close()     

if __name__=="__main__":
    pass        