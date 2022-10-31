import UserSurvey
import Utilities
import csv

class SurveyData:

    def __init__(self):
        self.__listOfSurveys = [] 

#    def __init__(self, listOfSurveys = []):
#        self.__listOfSurveys = listOfSurveys

    def addUserSurvey(self, userSurvey):
        """ Adds the rows of userSurvey to a list of all the rows """
        self.__listOfSurveys.append(userSurvey)


    def __buildCSV(self):
        """Build the string-based representation of the survey data (including metadata)"""        
        results = [survey.writeCSV()+"\n" for survey in self.__listOfSurveys]        
        entireFile = ''.join(results)
        return entireFile

    def writeCSV(self, filename, header):
        """Actually write the content to the output file."""
        
        #userSurvey = UserSurvey.UserSurvey()

        #
        # Open the output file to write
        #
        outFile = Utilities.safe_open(filename, "w");

        # Write in the following format:
        #   Header
        outFile.write( str(header) + "\n" )

        #   All rows (UserSurveys)
        outFile.write(self.__buildCSV())

        # Done: close it
        outFile.close()
        
    def compute(self, survey_header, room_data, age_categories):
        """Initiate metadata computations"""

        # Update the header with any new metadata column titles
        UserSurvey.UpdateMetadataTitles(survey_header)

        for survey in self.__listOfSurveys:
            survey.compute(room_data, age_categories)
        
        
    def __str__(self):
        return self.__buildCSV()

def test():
    sd = SurveyData()

    print(sd)

if __name__ == "__main__":
    test()
