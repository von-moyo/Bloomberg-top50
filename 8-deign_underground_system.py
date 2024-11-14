class UndergroundSystem:

    def __init__(self):
        # To store the customer check-in data: {id: (stationName, checkInTime)}
        self.check_in_data = {}
        
        # To store the travel times between stations: {(startStation, endStation): [times]}
        self.travel_times = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Record the check-in time and station for the given customer
        self.check_in_data[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Get the check-in data for the customer
        check_in_station, check_in_time = self.check_in_data.pop(id)
        
        # Calculate the travel time
        travel_time = t - check_in_time
        
        # Record the travel time for the pair of stations
        if (check_in_station, stationName) not in self.travel_times:
            self.travel_times[(check_in_station, stationName)] = []
        
        self.travel_times[(check_in_station, stationName)].append(travel_time)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Get the list of travel times for the given pair of stations
        travel_times = self.travel_times[(startStation, endStation)]
        
        # Calculate the average time
        return sum(travel_times) / len(travel_times)

# Time Complexity:
# checkIn:
# O(1), as it only involves storing customer data in a dictionary.
# checkOut: 
# O(1), as it only involves retrieving data from a dictionary, calculating the travel time, and updating the dictionary.
# getAverageTime: 
# O(k), where k is the number of trips between the given start and end stations. This is due to the need to compute the sum and the count of travel times for the given pair.