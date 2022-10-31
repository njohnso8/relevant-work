import csv
import SurveyData
import UserSurvey
import project_globals
import Header

class SurveyParser:
    
    def __init__(self, csv_filename):
        #
        # Variable Initialization
        #
        self.__surveyData = None
        self.__columnTitles = ''
        self.__surveyHeader = ''

        # Private method invocation for actual initialization 
        self.__parse(csv_filename)


#    def __buildUserSurvey(self, rowList):
#        """Noah: TBD
#           @output: UserSurvey Object
#        """
#        
#        """Thoughts: rowLists has all the rows, the goal of this function is to break down rowLists into
#        individual rows, which are UserSurvey objects"""
#        
#        userSurveyObject = UserSurvey.UserSurvey(rowList)
#
#        return userSurveyObject 
        

    def __parse(self, csv_filename):
        """Constructs a SurveyData object consisting of all user surveys"""

        self.__surveyData = SurveyData.SurveyData()

        with open(project_globals.ORIGINAL_SURVEY_DATA_FILE) as csvfile:
            hotel_data_reader = csv.reader(csvfile, delimiter=',')
        
        
            # Get the header data from the spreadsheet    
            self.__columnTitles = next(hotel_data_reader)

            """What is going on with columnTitles? It originally was a list, but that doesn't make sense.
            It is empty, thererfore, header is empty"""
            print(self.__columnTitles)

            self.__surveyHeader = Header.Header(self.__columnTitles)
        
            # We are interested in sifting out all of the unique columns from the given data
            # We thus have a list of lists representing these values
            unique_column_values = [[] for _ in range(len(self.__columnTitles))]
                
            #
            # Cycle through all of the data (all rows)
            #
            row_counter = 2
            rows_omitted = 0
            row = next(hotel_data_reader)
            while True:
        
                #
                # Add the column value to the particular list if is a unique value
                #
                index_col = 0
                for col_value in row:
                    
                    if col_value not in unique_column_values[index_col]:
                        unique_column_values[index_col].append(col_value)
                    
                    index_col = index_col + 1
                row_counter = row_counter + 1
        
                if row_counter < 5 or row_counter % 25 == 0:
                    print("Processed row", row_counter)
                
                self.__surveyData.addUserSurvey(UserSurvey.UserSurvey(self.__surveyHeader, row))
                
                try:
                    # Grab next line
                    row = next(hotel_data_reader)
                # Skip entries with strange decoding issues 
                except UnicodeDecodeError:
                    rows_omitted = rows_omitted + 1
                    pass
                # If reading fails, because we are at the end, break out 
                except:
                    break
                

            
            # Sanity check on expected number of columns
            assert len(self.__columnTitles) == len(unique_column_values), "column title size does not match number of unique list"
            
            # Create a mapping of titles to possible values
            categories = []
            for i in range(len(self.__columnTitles)):
                categories.append((self.__columnTitles[i], unique_column_values[i]))
        
            print("Rows omitted", rows_omitted)
    

    
    def getSurveyData(self):
        return self.__surveyData
    
    def getHeader(self):
        return self.__surveyHeader
    
    
def test():
    sp = SurveyParser(project_globals.ORIGINAL_SURVEY_DATA_FILE)
    
if __name__ == "__main__":
    test()
        

