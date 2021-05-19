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
            
    def load_passenger_csv(fn):
        with open(fn) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            pass_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    
                    if len(row) > 9 and row[0].isnumeric():
                        
                        pass_id = row[0]
                        first = row[1]
                        last = row[2]
                        class_lvl = row[3]
                        seat_num = row[4]
                        
                        Passenger.create_passenger(pass_id, first, last, class_lvl, seat_num)
                        
                        pass_count += 1
                        
                    else:
                        pass
                    line_count += 1
            return f'loaded {pass_count} passengers from {fn}'
        
    def load_flight_csv(fn):
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
            #print(query)
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except Error as e:
            #print(f"The error '{e}' occured")
            raise e
