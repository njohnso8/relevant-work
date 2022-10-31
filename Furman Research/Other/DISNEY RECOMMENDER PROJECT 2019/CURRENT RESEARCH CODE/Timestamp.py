"""
    This is a utility class for representing a date, time, etc.
    Input of a date should be a string similar to what is found in our data: month / day / year as well as time
    Parse that string in the constructor
    Provide public methods for accessing date information (month, day, year, etc.)
"""

class Timestamp:
    
    def __parseGroup(self, string):
        """Takes in string of party data of the form "MM/DD/YY"
        First M is month, second M is minutes
           returns list of Tuples corresponding to the input string representing a party
        """
        if len(string) == 0:
            return []
        else:

            self.__listOfTimeStamp = string.split("/")
            print(self.__listOfTimeStamp)
            self.__listOfTriuples = []
        
            month = self.__listOfTimeStamp[0]
            day = self.__listOfTimeStamp[1]
            year = self.__listOfTimeStamp[2]
            self.__listOfTriuples.append(int(month))
            self.__listOfTriuples.append(int(day)) 
            self.__listOfTriuples.append(int(year))

            return self.__listOfTriuples
    
    def __init__(self, timeStampString):
        self.__listOfTriuples = self.__parseGroup(timeStampString)
    
  
#    def getDate(self):
#        '''
#        function returns string of date
#        '''
#        return self.__listOfTimeStamp[:]
    
    def getYear(self):
        '''
        function returns string of year
        '''
        year = self.__listOfTriuples[2]
        
        return year
    
    def getMonth(self):
        '''
        function returns string of month
        '''
        month = self.__listOfTriuples[0]
        
        return month
    
    def getDay(self):
        '''
        function returns string of day
        '''
        day = self.__listOfTriuples[1]

        return day
    
        
   
def test():

    tS1 = Timestamp("10/21/95")
    
    assert tS1.getYear() == 95, "Test 1"
    assert tS1.getMonth() == 10, "Test 2"
    assert tS1.getDay() == 21, "Test 3"
    
    
    print("Tests succeeded")  
  
  
if __name__ == "__main__":
    test()
     
  
    