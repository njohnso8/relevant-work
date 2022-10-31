#
#
#
#    Group takes in string of party data, creates lists of Tuples
#    has functions to return party size, get num males or num females
#
#
#
 
class Group:

    def __parseGroup(self, string):
        """Takes in string of party data of the form "genderAGE|genderAGE|...genderAGE
           returns list of Tuples corresponding to the input string representing a party
        """
        if len(string) == 0:
            return []

        listOfGenderAge = string.split("|")
        listOfTuples = []

        for string in listOfGenderAge:
            gender = string[0]
            age = string[1:]
            listOfTuples.append((gender, int(age)))

        return listOfTuples
    
    def __init__(self, partyString):
        self.__listOfTuples = self.__parseGroup(partyString)
    
    def getGroup(self):
        return self.__listOfTuples
    
    def getPartySize(self):
        return len(self.__listOfTuples)
  
    def getNumMales(self):

        intCount = 0
        for (gender, age) in self.__listOfTuples:
            if gender == "M":
                intCount += 1
        return intCount

    def getAges(self):
        return [age for (gender, age) in self.__listOfTuples]
    
    def getAgesFemale(self):
        
        agesFemale = []
        for (gender, age) in self.__listOfTuples:
            if gender == "F":
                agesFemale.append( age )

        return agesFemale
    
    def getAgesMale(self):
        agesMale = []
        
        for (gender, age) in self.__listOfTuples:
            if gender == "M":
                agesMale.append( age )
        
        return agesMale
    
    def getNumFemales(self):
        return self.getPartySize() - self.getNumMales()

def test():

    g1 = Group("M67")
    assert g1.getPartySize() == 1, "Test 8"
    assert g1.getNumMales() == 1, "Test 9"
    assert g1.getNumFemales() == 0, "Test 10" 

    g2 = Group("F40|F65|F76|M1|M4|M42|M65") 
    assert g2.getPartySize() == 7, "Test 11"
    assert g2.getNumMales() == 4, "Test 12"
    assert g2.getNumFemales() == 3, "Test 13"
    assert g2.getAgesFemale() == [40, 65, 76], "Test 14"
    assert g2.getAgesMale() == [1, 4, 42, 65], "Test 15"
    
    assert Group("F61|M76").getGroup() == [("F", 61), ("M", 76)], "Test 1"
    assert Group("M67").getGroup() == [("M", 67)], "Test 2"
    assert Group("").getGroup() == [], "Test 3"
    assert Group("F40|F65|F76|M1|M4|M42|M65").getGroup() == [("F", 40), ("F", 65), ("F", 76), ("M", 1), ("M", 4), ("M", 42), ("M", 65)], "Test 4"
    assert Group("F2|F4|F33|F37|F50|F54|M1|M3|M32|M33|M54").getGroup() == [("F", 2), ("F", 4), ("F", 33), ("F", 37), ("F", 50), ("F", 54), ("M", 1), ("M", 3), ("M", 32), ("M", 33), ("M", 54)], "Test 5"
    assert Group("F9|F28|F36|F41|F46|F61|M2|M4|M7|M11|M14|M17|M32|M36|M41|M70").getGroup() == [("F", 9), ("F", 28), ("F", 36), ("F", 41), ("F", 46), ("F", 61), ("M", 2), ("M", 4), ("M", 7), ("M", 11), ("M", 14), ("M", 17), ("M", 32), ("M", 36), ("M", 41), ("M", 70)], "Test 6"
    assert Group("F0|F59|M3|M32|M60").getGroup() == [("F", 0), ("F", 59), ("M", 3), ("M", 32), ("M", 60)], "Test 7"
    
    print("Tests succeeded")  
  
  
if __name__ == "__main__":
    test()
 

