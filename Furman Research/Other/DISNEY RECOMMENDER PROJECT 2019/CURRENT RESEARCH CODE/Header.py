

class Header:
    """If column titles is a string, need to parse"""
#    def __parseHeader(self, headerString):
#        if len(headerString) == 0:
#            return []
#        
#        listH = []
#        
#        for string in headerString:
#            listH.append(string)
#            
#        return listH
        
    
    def __init__(self, headerString):
        self.__headerList = headerString
    
    def getHeader(self): 
        return self.__headerList
    
    def addColumn(strTitle):
        self.__headerList.append(strTitle)
        
    def __str__(self):
        L = [str(item) for item in self.__headerList]
        return ",".join(L)
        
 
   
def test():
    
    header = Header('survey_id, trip_start, trip_end' )

    print(header.getHeader())
    print("Test Complete")
        
if __name__ == "__main__":
    test()
    
    