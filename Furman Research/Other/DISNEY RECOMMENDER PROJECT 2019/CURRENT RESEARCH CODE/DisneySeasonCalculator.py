"""
A class to represent Disney seasons of the year.
It should provide the following functionality:
     initialize with approximate dates for Disney seasons: all festivals, parties, special times, etc.
     A function to lookup the Disney season based on a given date.
"""

import Timestamp

class DisneySeasonCalculator:
    
    def __init__(self):
            
        self.__disneySeason = []
        
    
    def calcDisneySeason(self, startDate):
        """ Based on user input start date, returns the Disney season """
        
        month = int(startDate.getMonth())
        day = int(startDate.getDay())
        year = int(startDate.getYear())
        
        if year == 2017:
            if month == 10:
                self.__disneySeason.append("Mickey's Not So Scary Halloween Party")
                self.__disneySeason.append("Epcot's International Food and Wine Festival")
                if day > 26:
                    self.__disneySeason.append("Disney-Pixar's Coco Family Celebration")
                if day > 26 and day < 29:
                    self.__disneySeason.append("Walt Disney World Swan and Dolphin Food and Wine Classic")
            elif month == 11:
                if day == 1:
                    self.__disneySeason.append("Mickey's Not So Scary Halloween Party")
                if day > 14:
                    self.__disneySeason.append("Epcot's International Food and Wine Festival")
                if day > 27:
                    self.__disneySeason.append("Disney-Pixar's Coco Family Celebration")
                if day < 1 and day > 6:
                    self.__disneySeason.append("Disney Wine and Dine Half Marathon Weekend")
                if day > 8:
                    self.__disneySeason.append("Sunset Seasons Greetings")
                    self.__disneySeason.append("Mickey's Very Merry Christmas Party")
            elif month == 12:
                self.__disneySeason.append("Sunset Seasons Greetings")
                self.__disneySeason.append("Mickey's Very Merry Christmas Party")
                
        elif year == 2018:
            if month == 1:
               if day > 2 and day < 8: 
                   self.__disneySeason.append("Walt Disney World Marathon Weekend")
               if day > 11:
                   self.__disneySeason.append("Epcot's Festival of the Arts")
               if day > 23 and day < 29:
                   self.__disneySeason.append("NFL Pro Bowl Weekend")
            elif month == 2:
                if day < 20:
                    self.__disneySeason.append("Epcot's Festival of the Arts")
                if day == 3:
                    self.__disneySeason.append("Disney's Fairy Tale Weddings Showcase")
                if day > 21 and day < 26:
                    self.__disneySeason.append("Disney Princess Half Marathon Weekend")
                if day > 25:
                    self.__disneySeason.append("Atlanta Braves Spring Training")
                if day == 28:
                    self.__disneySeason.append("Epcot's International Flower and Garden Festival")
            elif month == 3:
                self.__disneySeason.append("Epcot's International Flower and Garden Festival")
                if day < 25:
                    self.__disneySeason.append("Atlanta Braves Spring Training")
                if day > 15 and day < 19:
                    self.__disneySeason.append("Mighty St. Patrick's Festival")
            elif month == 4:
                self.__disneySeason.append("Epcot's International Flower and Garden Festival")
                if day > 18 and day < 23:
                    self.__disneySeason.append("Star Wars Half Marathon - The Dark Side")
                if day > 21:
                    self.__disneySeason.append("20th Anniversary of Animal Kingdom Celebration")
            elif month == 5:
                if day < 29:
                    self.__disneySeason.append("Epcot's International Flower and Garden Festival")
                if day < 6:
                    self.__disneySeason.append("20th Anniversary of Animal Kingdom Celebration")
                if day == 27:
                    self.__disneySeason.append("Star Wars: Galactic Nights")
            elif month == 7:
                if day == 3 or day == 4:
                    self.__disneySeason.append("4th of July Celebrations")
            elif month == 8:
                if day > 6 and day < 13:
                    self.__disneySeason.append("Jr. NBA World")
                if day > 16:
                    self.__disneySeason.append("Mickey's Not So Scary Halloween Party")
                if day > 29:
                    self.__disneySeason.append("Epcot's International Food and Wine Festival")
            elif month == 9:
                self.__disneySeason.append("Epcot's International Food and Wine Festival")
                self.__disneySeason.append("Mickey's Not So Scary Halloween Party")
            elif month == 10:
                self.__disneySeason.append("Epcot's International Food and Wine Festival")
                self.__disneySeason.append("Mickey's Not So Scary Halloween Party")
            elif month == 11:
                if day < 13:
                    self.__disneySeason.append("Epcot's International Food and Wine Festival")
                if day < 5:
                    self.__disneySeason.append("Disney Wine and Dine Half Marathon Weekend")
                if day > 7:
                    self.__disneySeason.append("Mickey's Very Merry Christmas Party")
                if day > 17:
                    self.__disneySeason.append("90 Years of Mickey Mouse")
                    self.__disneySeason.append("Epcot's International Festival of the Holidays")
            elif month == 12:
                self.__disneySeason.append("Epcot's International Festival of the Holidays")
                self.__disneySeason.append("Mickey's Very Merry Christmas Party")
                self.__disneySeason.append("90 Years of Mickey Mouse")
                   

            
        return self.__disneySeason
        
            
                