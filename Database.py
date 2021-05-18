import sqlite3
from sqlite3 import Error

class Database:
    
    def __init__(self, datfile):
        
        self.connection = self.create_connection(datfile)
        
        pass
    
    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            
        except Error as e:
            print(f"The error '{e}' occured")
        return connection
    
    def execute_query(self, query, params=()):
        
        cursor = self.connection.cursor()
        try: 
            cursor.execute(query, params)
            self.connection.commit()
        except Error as e:
            print(f"The error '{e}' occured")
            raise e
            
    def execute_read_query(self, query, params=()):
        cursor = self.connection.cursor()
        result = None
        try:
            #print(params)
            #print(query)
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except Error as e:
            #print(f"The error '{e}' occured")
            raise e