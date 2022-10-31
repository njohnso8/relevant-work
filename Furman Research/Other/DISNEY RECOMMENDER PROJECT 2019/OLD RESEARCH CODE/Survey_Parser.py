import csv
import User_Survey_Class
import User_Survey_Tester
import Survey_Data_Class
import Survey_Data_Tester


with open('wdw_hotel_surveys_20190109160713.csv') as csvfile:
    hotel_data_reader = csv.reader(csvfile, delimiter=',')

    # Get the header data from the spreadsheet    
    column_titles = next(hotel_data_reader)

    # We are interested in sifting out all of the unique columns from the given data
    # We thus have a list of lists representing these values
    unique_column_values = [[] for _ in range(len(column_titles))]


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
    assert len(column_titles) == len(unique_column_values), "column title size does not match number of unique list"
    
    # Create a mapping of titles to possible values
    categories = []
    for i in range(len(column_titles)):
        categories.append((column_titles[i], unique_column_values[i]))

    print(categories[column_titles.index("hotel_satisfaction_code")])
    print(categories[column_titles.index("hotel_recommendation_code")])
    print("Rows omitted", rows_omitted)
