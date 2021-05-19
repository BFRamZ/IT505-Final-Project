"""
Created on Wed Apr 28 18:39:17 2021

@author: BFRamZ
"""
from sqlite3 import IntegrityError

class Flight:
    
    def __init__(self, db):
        self.db = db
        self.create_flights_table()
        
    def create_flights_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS flights (
              flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
              source STRING NOT NULL,
              destination TEXT NOT NULL,
              flight_time TEXT NOT NULL,
              seats INTEGER DEFAULT 0
            );
            """
            
        self.db.execute_query(query)
    
    def update_flight(self, flight_id, attr, val):
        
        if attr in self.headers:
            sql = f''' UPDATE flights
                SET {attr}=?
                WHERE flight_id=?'''
            
            params = (val, flight_id)
            self.db.execute_query(sql, params)
            return(f"Updated {attr} for Flight {flight_id}")
        else:
            return("Could not update: Invalid attribute")
    
    def select_flight(self, flight_id):
        
        query = "SELECT * from flights WHERE flight_id=?"
        
        result = self.db.execute_read_query(query, (flight_id))
        
        return result
    
    def view_flight(self, flight_id):
        
        result = self.select_flight(flight_id)
        
        if result:
            
            name = result[0][1]
            name += " "
            name += result[0][2]
            rstr = f"Flight: {name}"
        else:
            rstr = "Flight not found"
            
        return rstr
    
    def view_flights(self):
        
        rstr = "flights:"
        
        query = "SELECT * from flights"
        
        flights = self.db.execute_read_query(query)
        
        for c in flights:
            title = c[3]
            rstr += f"\n\t{title}"
        return rstr

    
    def create_flight(self, flight_id, source, destination, flight_time, seats):
        
        taken = self.select_flight(flight_id)
        
        if taken:
            rstr = f"flight ID {flight_id} is taken."
            
        else:
            query = """
            INSERT INTO flights (flight_id, source, destination, flight_time, seats)
            VALUES (?, ?, ?, ?, ?);
            """
            self.db.execute_query(query, (flight_id, source, destination, flight_time, seats, ))
            
            rstr = f"Created new flight: {destination}, {source} ID: {flight_id}"
        '''    
        except IntegrityError as e:
            print(f"create_course fail: {e}")
        '''    
        return rstr
    
    def delete_flight(self, flight_id):
        
        real = self.select_flight(flight_id)
        
        if real:
            query = "DELETE FROM flights WHERE flight_id=?"
            self.db.execute_query(query, (flight_id, ))
            rstr = f"Deleted flight with ID {flight_id}"
        else:
            rstr = f"flight with ID {flight_id} does not exist."
            
        return rstr

    def delete_flights(self):
        
        #query = "PRAGM foreign_keys = OFF;"
        #self.db.execute_query(query)
        
        self.db.execute_query("DROP TABLE IF EXISTS flights")
        self.create_flights_table()
        return('deleted flights')
        
        #query = "PRAGM foreign_keys = ON;"
        #self.db.execute_query(query)
