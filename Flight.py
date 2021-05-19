"""
Created on Wed Apr 28 18:39:17 2021

@author: BFRamZ
"""
from sqlite3 import IntegrityError
import csv
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
        
        for x in flights:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            rstr += f"\n\t{b} to {c}: ID({a}) Time({d}) Seats({e})"
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
        
    def import_flight_csv(self, fn):
        with open(fn) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            flight_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    
                    if len(row) > 9 and row[0].isnumeric():
                        
                        flight_id = row[0]
                        source = row[1]
                        destination = row[2]
                        flight_time = row[3]
                        seats = row[4]
                        
                        Flight.create_flight(flight_id, source, destination, flight_time, seats)
                        
                        flight_count += 1
                        
                    else:
                        pass
                    line_count += 1
            return f'loaded {flight_count} flights from {fn}'
