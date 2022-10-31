"""
    AgeCategories creates class with list input
    List input will be age categories 
"""

class AgeCategories:
    def __init__(self, listOfAges):      
        self.counts = [0] * len(listOfAges)
        self.categories = listOfAges
    
    
    def __addAge(self, counts, intAge):
        '''
        addAge function compares given input integer (intAge) to list of age categories
        Will then add to input list counts if conditions hold
        '''
        
        #length of counts needs to be the same as length of categories or program will crash
        assert len(counts) == len(self.categories)
        
        '''
        For loop will run through given length of list
        It will then compare input intAge to each index in list
        Then if the intAge is less than index, adds to counts, exits for loop
        Else, it will countinue to cycle through the list
        '''
        for index in range(len(counts)):
            if intAge <= self.categories[index]:
                counts[index] = counts[index] + 1
                break
        
        #return list 
        return counts
    
    
    def addAge(self, intAge):
        '''
        addAge function takes intAge input
        runs __addAge function with given input and instance variable 'counts'
        '''
        
        #runs __addAge
        self.__addAge(self.counts ,intAge)

    
    def addAges(self, partyList):
        '''
        addAges function takes given input list and executes addAge function 
        on each entry 
        '''
        
        for age in partyList:
            self.addAge(age)

  
    def getFrequencyCount(self, partyList):
        '''
        constructs lists of frequency of ages (counts)
        populates list with entries from partyList
        returns counts 
        '''
        
        #construct list
        counts = [0] * len(self.categories)
        
        #populate counts
        for age in partyList:
            self.__addAge(counts, age)
        
        #return list
        return counts
    
    
    def getFrequencyCountFemale(self, partyListFemale):
        '''
        requires user to use getAgesFemale function from group as input
        '''
        
        self.getFrequencyCount(partyListFemale)
    
    
    def getFrequencyCountMale(self, partyListMale):
        '''
        requires user to use getAgesMale function from group as input
        '''
        
        self.getFrequencyCount(partyListMale)
    
    
    def getCounts(self):
        '''
        getCounts returns counts list 
        '''
        
        #returns 'counts'
        return self.counts

    

    #
    # Annie: write functions to compute other group-based category information; test them
    #

def test():
    
    ac = AgeCategories([1,5,15])

    assert ac.getFrequencyCount([0, 4, 9, 8, 11]) == [1,1,3]

    print("Test Suceeded")


if __name__ == "__main__":
    test()

