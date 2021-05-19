"""
Created on Wed Apr 28 18:39:17 2021

@author: BFRamZ
"""
from sqlite3 import IntegrityError

class Passenger:
    
    def __init__(self, db):
        self.db = db
        self.create_passengers_table()
        
    def create_passengers_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS passengers (
              pass_id INTEGER PRIMARY KEY AUTOINCREMENT,
              first_name TEXT NOT NULL,
              last_name TEXT NOT NULL,
              class_level TEXT NOT NULL,
              seat_number string DEFAULT 0
            );
            """
            
        self.db.execute_query(query)
    
    def update_passenger(self, pass_id, attr, val):
        
        if attr in self.headers:
            sql = f''' UPDATE passengers
                SET {attr}=?
                WHERE pass_id=?'''
            
            params = (val, pass_id)
            self.db.execute_query(sql, params)
            return(f"Updated {attr} for Passenger {pass_id}")
        else:
            return("Could not update: Invalid attribute")
    
    def select_passenger(self, pass_id):
        
        query = "SELECT * from passengers WHERE pass_id=?"
        
        result = self.db.execute_read_query(query, (pass_id))
        
        return result
    
    def view_passenger(self, pass_id):
        
        result = self.select_passenger(pass_id)
        
        if result:
            
            name = result[0][1]
            name += " "
            name += result[0][2]
            rstr = f"Passenger: {name}"
        else:
            rstr = "Passenger not found"
            
        return rstr
    
    def view_passengers(self):
        
        rstr = "passengers:"
        
        query = "SELECT * from passengers"
        
        passengers = self.db.execute_read_query(query)
        
        for c in passengers:
            title = c[3]
            rstr += f"\n\t{title}"
        return rstr

    
    def create_passenger(self, pass_id, first_name, last_name, class_level, seat_number):
        
        taken = self.select_passenger(pass_id)
        
        if taken:
            rstr = f"Passenger ID {pass_id} is taken."
            
        else:
            query = """
            INSERT INTO passengers (pass_id, first_name, last_name, class_level, seat_number)
            VALUES (?, ?, ?, ?, ?);
            """
            self.db.execute_query(query, (pass_id, first_name, last_name, class_level, seat_number, ))
            
            rstr = f"Created new passenger: {last_name}, {first_name} ID: {pass_id}"
        '''    
        except IntegrityError as e:
            print(f"create_passenger fail: {e}")
        '''    
        return rstr
    
    def delete_passenger(self, pass_id):
        
        real = self.select_passenger(pass_id)
        
        if real:
            query = "DELETE FROM passengers WHERE pass_id=?"
            self.db.execute_query(query, (pass_id, ))
            rstr = f"Deleted Passenger with ID {pass_id}"
        else:
            rstr = f"Passenger with ID {pass_id} does not exist."
            
        return rstr

    def delete_passengers(self):
        
        #query = "PRAGM foreign_keys = OFF;"
        #self.db.execute_query(query)
        
        self.db.execute_query("DROP TABLE IF EXISTS passengers")
        self.create_passengers_table()
        return('deleted passengers')
        
        #query = "PRAGM foreign_keys = ON;"
        #self.db.execute_query(query)
        
    def __str__(self):
        return f"{self.debt} {self.passenger_num} {self.title}"
    
   