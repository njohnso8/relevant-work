import Survey_Data_Class
import User_Survey_Class

def main():
    sd = Survey_Data_Class.SurveyData()

    print(sd)

    print(sd.get_listOfSurveys())

    print(sd.addListOfSurveysWriteCSV())

main()
