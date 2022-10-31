"""
    This is a utility class for representing a date, time, etc.
    Input of a date should be a string similar to what is found in our data: month / day / year as well as time
    Parse that string in the constructor
    Provide public methods for accessing date information (month, day, year, etc.)
"""

class SurveySubmittedTimestamp:
    
    def __parseGroup(self, string):
        """Takes in string of party data of the form "YYYY-MM-DDTHH:MM:SSZ"
        First M is month, second M is minutes
           returns list of Tuples corresponding to the input string representing a party
        """
        if len(string) == 0:
            return []

        self.__listOfTimeStamp = []

        date = string[0:10]
        time = string[11:19]
        
        self.__listOfTimeStamp.append(date)
        self.__listOfTimeStamp.append(time)

        return self.__listOfTimeStamp
    
    def __init__(self, timeStampString):
        self.__listOfTimeStamp = self.__parseGroup(timeStampString)
    
    def getTimeStamp(self):
        '''
        function returns list of strings of date and time
        '''
        return self.__listOfTimeStamp
    
    def getDate(self):
        '''
        function returns string of date
        '''
        return self.__listOfTimeStamp[0]
    
    def getTime(self):
        '''
        function returns string of time 
        '''
        return self.__listOfTimeStamp[1]
    
    def getYear(self):
        '''
        function returns string of year
        '''
        date = self.__listOfTimeStamp[0]
        year = date[0:4]
        
        return year
    
    def getMonth(self):
        '''
        function returns string of month
        '''
        date = self.__listOfTimeStamp[0]
        month = date[5:7]
        
        return month
    
    def getDay(self):
        '''
        function returns string of day
        '''
        date = self.__listOfTimeStamp[0]
        day = date[8:10]

        return day
    
    def getHour(self):
        '''
        function returns string of hour
        '''
        time = self.__listOfTimeStamp[1]
        hour = time[0:2]
        
        return hour
    
    def getMinute(self):
        '''
        function returns string of minute
        '''
        time = self.__listOfTimeStamp[1]
        minute = time[3:5]
        
        return minute
    
    def getSecond(self):
        '''
        function returns string of second
        '''
        time = self.__listOfTimeStamp[1]
        second = time[6:8]
        
        return second
        
   
def test():

    tS1 = Timestamp("2017-10-09T17:01:10Z")
    tS1.getTimeStamp()
    
    assert tS1.getDate() == "2017-10-09", "Test 1"
    assert tS1.getTime() == "17:01:10", "Test 2"
    
    assert tS1.getYear() == "2017", "Test 3"
    assert tS1.getMonth() == "10", "Test 4"
    assert tS1.getDay() == "09", "Test 5"
    
    assert tS1.getHour() == "17", "Test 6"
    assert tS1.getMinute() == "01", "Test 7"
    assert tS1.getSecond() == "10", "Test 8"
    
    
    print("Tests succeeded")  
  
  
if __name__ == "__main__":
    test()
     
  
    