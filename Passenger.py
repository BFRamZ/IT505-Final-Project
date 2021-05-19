"""
Created on Wed Apr 28 18:39:17 2021

@author: BFRamZ
"""
from sqlite3 import IntegrityError
import csv
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
        
        for x in passengers:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            rstr += f"\n\t{c}, {b}: ID({a}) Level({d}) Number({e})"
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
        
    def import_passenger_csv(self, fn):
        with open(fn) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            pass_count = 0
            for row in csv_reader:
                pass_id = row[0]
                first = row[1]
                last = row[2]
                class_lvl = row[3]
                seat_num = row[9]
                        
                Passenger.create_passenger(pass_id, first, last, class_lvl, seat_num)
                        
                pass_count += 1
        return f'loaded {pass_count} passengers from {fn}'
    
    def save_passenger_csv(self, fn):
        
        with open(fn, mode='w') as output_file:
            
            pass_count = 0
            writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            headings = ['Pass ID', 'First', 'Last', "ID", "Seat Num"]
            writer.writerow(headings)
            
            query = "SELECT * from passengers"
        
            passengers = self.db.execute_read_query(query)
            
            for row in passengers:
                
                
                writer.writerow(row)
                pass_count += 1
                
        print(f"saved {pass_count} passengers to {fn}")
    
   
