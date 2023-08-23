class Flight:
    def __init__(self, flight_id, s, d, p):
        self.flight_id = flight_id
        self.s = s
        self.d = d
        self.p = p

class FlightTable:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def get_flights_for_city(self, city):
        city_flights = [flight for flight in self.flights if city in  (flight.d)]
        return city_flights
    
    def get_flights_from_city(self, city):
        city_flights = [flight for flight in self.flights if flight.s == city]
        return city_flights
    
    def get_flights_between_cities(self, s, d):
        city_flights = [flight for flight in self.flights if flight.s == s and flight.d == d]
        return city_flights

def main():
    flight_table = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for data in flight_data:
        flight = Flight(*data)
        flight_table.add_flight(flight)
    
    while True:
        print("Search Options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            city = input("Enter a city: ")
            city_flights = flight_table.get_flights_for_city(city)
            for flight in city_flights:
                print(f"Flight {flight.flight_id}: {flight.s} to {flight.d}, Price: {flight.p}")
        elif choice == 2:
            city = input("Enter a city: ")
            city_flights = flight_table.get_flights_from_city(city)
            for flight in city_flights:
                print(f"Flight {flight.flight_id}: {flight.s} to {flight.d}, Price: {flight.p}")
        elif choice == 3:
            s = input("Enter source city: ")
            d = input("Enter destination city: ")
            city_flights = flight_table.get_flights_between_cities(s, d)
            for flight in city_flights:
                print(f"Flight {flight.flight_id}: {flight.s} to {flight.d}, Price: {flight.p}")
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
