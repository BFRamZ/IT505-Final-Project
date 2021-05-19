# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 23:10:18 2021

@author: charrington
"""

#Comment out input before submitting to Mimir

# f = open('input2.txt','r')
# def input(prompt=''):
#     print(prompt, end='')
#     return f.readline().strip()

class CLI:
    
    def __init__(self):
        self.passenger = passenger
        self.flight = flight
        self.commands = {}
        
    def add_command(self, name, foo):
        self.commands[name] = foo
        
    def start(self):
        print('hello')
        
        while(1):
            line = input().strip()
            
            if not line or line[0]=='#':
                print(line)
                continue
            
            tokens = line.split()
            cmd = tokens[0]
            args = tokens[1:]
            
            if cmd == 'exit' or cmd == 'quit' or cmd == 'bye':
                print('goodbye')
                break
            
                self.process( cmd, args)
            #--------------- passengers ------------------
            
            elif cmd == 'create_passenger':
                result = self.passenger.create_passenger(args[0], args[1], args[2], args[3], args[4])
                print(result)
                
            elif cmd == 'view_passenger':
                passenger = self.passenger.view_passenger(args[0])
                print(passenger)
                
            elif cmd == 'view_passengers':
                passenger = self.passenger.view_passengers()
                print(passenger)
                
            elif cmd == 'delete_passengers':
                passenger = self.passenger.delete_passengers()
                print(passenger)
            
            #----------------- flights-----------------------
            
            elif cmd == 'create_flight':
                result = self.flight.create_flight(args[0], args[1], args[2], args[3], args[4])
                print(result)
                
            elif cmd == 'view_flight':
                passenger = self.flight.view_flight(args[0])
                print(passenger)
                
            elif cmd == 'view_flights':
                passenger = self.flight.view_flights()
                print(passenger)
                
            elif cmd == 'delete_flights':
                passenger = self.flight.delete_flights()
                print(passenger)
            
           
            
if __name__=="__main__":
    
    from database2 import Database
    from passenger2 import passenger
    from flight2 import flight
    
    my_db = Database('my_database.sqlite')
    
    passenger = passenger(my_db)
    flight = flight(my_db)
    
    
    myCLI = CLI()
    
    commands = {
        "create_passenger": passenger.create_passenger,
        "view_passenger": passenger.view_passenger,
        "view_passengers": passenger.view_passengers,
        "delete_passengers": passenger.delete_passengers,
        
        "create_flight": flight.create_flight,
        "view_flight": flight.view_flight,
        "view_flights": flight.view_flights,
        "delete_flights": flight.delete_flights,
        
        }
    
    for cmd in commands:
        myCLI.add_command(cmd, commands[cmd])
        
    myCLI.start()
    pass
    
            
