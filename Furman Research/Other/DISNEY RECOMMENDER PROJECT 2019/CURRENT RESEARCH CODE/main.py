#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main class that reads the excel file, reads the room data file, creates
ageCategories, computes metadata, and outputs the file all in a few lines of 
the main method. The other methods are called by the main methods
"""
import SurveyParser
import Utilities
import project_globals
import AgeCategories
import RoomsData
import SurveyData
import Header


def buildGranularAgeCategories():
    """ creats a list of age categories out of age global constants """
    #creates an age category object out of global constants
    listOfAgeCategories = []

    listOfAgeCategories.append(project_globals.NEWBORNS)
    listOfAgeCategories.append(project_globals.TODDLERS)
    listOfAgeCategories.append(project_globals.YOUNG_CHILDREN)
    listOfAgeCategories.append(project_globals.PRE_TEENS)
    listOfAgeCategories.append(project_globals.TEENS)
    listOfAgeCategories.append(project_globals.YOUNG_ADULTS)
    listOfAgeCategories.append(project_globals.OLDER_YOUNG_ADULTS)
    listOfAgeCategories.append(project_globals.ADULTS_WITH_KIDS)
    listOfAgeCategories.append(project_globals.MIDDLE_AGED_ADULTS)
    listOfAgeCategories.append(project_globals.PRE_RETIREMENT_ADULTS)
    listOfAgeCategories.append(project_globals.MAXIMUM_AGE)

    return AgeCategories.AgeCategories(listOfAgeCategories)

    

def main():
    """ reads the CSV excel file, reads the room data file, creates 
    ageCategories, computes the metadata, outputs the file
    Calls methods that are above in order to complete this."""

    # Read the excel survey datafile
    surveyParser = SurveyParser.SurveyParser(project_globals.ORIGINAL_SURVEY_DATA_FILE)
    #survey_data = surveyParser.__parse(project_globals.ORIGINAL_SURVEY_DATA_FILE)
    
    survey_header = surveyParser.getHeader()
    print("Header:" + "|" + str(survey_header) + "|")
    survey_data = surveyParser.getSurveyData()

    # read the room data file
    room_data = RoomsData.RoomsData(project_globals.HOTEL_ROOM_DATA_FILE)

    #create/define the age categories for user data
    age_categories = buildGranularAgeCategories()

    #print(ageCategories)
    #prune/computing the user data
    survey_data.compute(survey_header, room_data, age_categories)

     #output the result

    survey_data.writeCSV(project_globals.SURVEY_DATA_OUTPUT_FILE, survey_header)

    
if __name__ == "__main__":
    main()