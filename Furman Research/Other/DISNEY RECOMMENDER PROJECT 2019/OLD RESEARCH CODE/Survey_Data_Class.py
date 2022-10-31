import User_Survey_Class

class SurveyData:
    def __init__(self):
        self.__listOfSurveys = [] 

    def __init__(self, listOfSurveys = []):
        self.__listOfSurveys = listOfSurveys

    def get_listOfSurveys(self):
        return self.__listOfSurveys

    def addListOfSurveysWriteCSV(self):
        self.__listOfSurveys.append(User_Survey_Class.UserSurvey())
        listOfStringSurveys = [str(item) for item in self.__listOfSurveys]
        s = ","
        return s.join(listOfStringSurveys)
