"""
A class to represent seasons of the year.
It should provide the following functionality:
     initialize with approximate dates for seasons: Winter, spring, summer, fall
     A function to lookup the season based on a given date.
"""
import Timestamp

class SeasonCalculator:
    
    """ Winter starts December 22
        Spring starts March 21
        Summer starts June 22
        Fall starts September 23 """
        
    def __init__(self):
            
        self.__season = ''
            
            
            
    def calcSeason(startDate):
        """ Based on user input start date, returns the season """
        
        month = int(startDate.getMonth())
        day = int(startDate.getDay())
        
        if month < 3:
            season = "winter"
        elif month == 3 and day < 21:
            season = "winter"
        elif month == 3 and day > 20:
            season = "spring"
        elif month < 6:
            season = "spring"
        elif month == 6 and day < 22:
            season = "spring"
        elif month == 6 and day > 21:
            season = "summer"
        elif month < 9:
            season = "summer"
        elif month == 9 and day < 23:
            season = "summer"
        elif month == 9 and day > 22:
            season = "fall"
        elif month < 12:
            season = "fall"
        elif month == 12 and day < 22:
            season = "fall"
        elif month == 12 and day > 21:
            season = "winter"
        else:
            season = "error"
            
        return season
        
            
                
        