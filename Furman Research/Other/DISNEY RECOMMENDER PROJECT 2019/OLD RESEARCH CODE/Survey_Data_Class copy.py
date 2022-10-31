import User_Survey_Class

class SurveyData:
    def __init__(self):
        self.__listOfSurveys = [] 

    def __init__(self, listOfSurveys = []):
        self.__listOfSurveys = listOfSurveys

    def get_listOfSurveys(self):
        return self.__listOfSurveys

    def get_survey_id():
        return User_Survey_Class.UserSurvey.__survey_id

    def get_survey_submitted_at():
        return User_Survey_Class.UserSurvey.__survey_submitted_at

    def get_trip_start_date():
        return User_Survey_Class.UserSurvey.__trip_start_date

    def get_trip_finish_date():
        return User_Survey_Class.UserSurvey.__trip_finish_date

    def get_hotel_name():
        return User_Survey_Class.UserSurvey.__hotel_name

    def get_hotel_code():
        return User_Survey_Class.UserSurvey.__hotel_code

    def get_hotel_trip_other_name():
        return User_Survey_Class.UserSurvey.__hotel_trip_other_name

    def get_hotel_any_other():
        return User_Survey_Class.UserSurvey.__hotel_any_other

    def get_hotel_ritz_carlton():
        return User_Survey_Class.UserSurvey.__hotel_ritz_carlton

    def get_hotel_super_eight():
        return User_Survey_Class.UserSurvey.__hotel_super_eight

    def get_hotel_embassy_suites():
        return User_Survey_Class.UserSurvey.__hotel_embassy_suites

    def get_hotel_days_inn():
        return User_Survey_Class.UserSurvey.__hotel_days_inn

    def get_hotel_hampton_inn():
        return User_Survey_Class.UserSurvey.__hotel_hampton_inn

    def get_hotel_quality_inn():
        return User_Survey_Class.UserSurvey.__hotel_quality_inn

    def get_hotel_marriott():
        return User_Survey_Class.UserSurvey.__hotel_marriott

    def get_hotel_holiday_inn():
        return User_Survey_Class.UserSurvey.__hotel_holiday_inn

    def get_hotel_omni():
        return User_Survey_Class.UserSurvey.__hotel_omni

    def get_hotel_hilton():
        return User_Survey_Class.UserSurvey.__hotel_hilton

    def get_hotel_millenium():
        return User_Survey_Class.UserSurvey.__hotel_millenium

    def get_hotel_radisson():
        return User_Survey_Class.UserSurvey.__hotel_radisson

    def get_hotel_hyatt():
        return User_Survey_Class.UserSurvey.__hotel_hyatt

    def get_hotel_fairfield_inn():
        return User_Survey_Class.UserSurvey.__hotel_fairfield_inn

    def get_hotel_ramada_inn():
        return User_Survey_Class.UserSurvey.__hotel_ramada_inn

    def get_hotel_drury_inn():
        return User_Survey_Class.UserSurvey.__hotel_drury_inn

    def get_hotel_four_seasons():
        return User_Survey_Class.UserSurvey.__hotel_four_seasons

    def get_hotel_best_western():
        return User_Survey_Class.UserSurvey.__hotel_best_western

    def get_hotel_past_other_name():
        return User_Survey_Class.UserSurvey.__hotel_past_other_name
    
    def get_hotel_selection_cost():
        return User_Survey_Class.UserSurvey.__hotel_selection_cost

    def get_hotel_selection_bar():
        return User_Survey_Class.UserSurvey.__hotel_selection_bar

    def get_hotel_selection_distance_to_parks():
        return User_Survey_Class.UserSurvey.__hotel_selection_distance_to_parks

    def get_hotel_selection_in_room_dining():
        return User_Survey_Class.UserSurvey.__hotel_selection_in_room_dining

    def get_hotel_selection_food_court():
        return User_Survey_Class.UserSurvey.__hotel_selection_food_court

    def get_hotel_selection_sit_down_dining():
        return User_Survey_Class.UserSurvey.__hotel_selection_sit_down_dining

    def get_hotel_selection_fine_dining():
        return User_Survey_Class.UserSurvey.__hotel_selection_fine_dining

    def get_hotel_selection_parks_shuttle():
        return User_Survey_Class.UserSurvey.__hotel_selection_parks_shuttle

    def get_hotel_selection_airport_shuttle():
        return User_Survey_Class.UserSurvey.__hotel_selection_airport_shuttle

    def get_hotel_selection_in_room_kitchen():
        return User_Survey_Class.UserSurvey.__hotel_selection_in_room_kitchen

    def get_hotel_selection_room_size():
        return User_Survey_Class.UserSurvey.__hotel_selection_room_size

    def get_hotel_selection_multiple_bedroom_suites():
        return User_Survey_Class.UserSurvey.__hotel_selection_multiple_bedroom_suites

    def get_hotel_selection_spa_fitness_center():
        return User_Survey_Class.UserSurvey.__hotel_selection_spa_fitness_center

    def get_hotel_selection_pool():
        return User_Survey_Class.UserSurvey.__hotel_selection_pool

    def get_hotel_selection_theme():
        return User_Survey_Class.UserSurvey.__hotel_selection_theme

    def get_hotel_selection_kids_activities():
        return User_Survey_Class.UserSurvey.__hotel_selection_kids_activities

    def get_hotel_selection_location_on_property():
        return User_Survey_Class.UserSurvey.__hotel_selection_location_on_property

    def get_hotel_selection_other_string():
        return User_Survey_Class.UserSurvey.__hotel_selection_other_string

    def get_hotel_selection_other_rating():
        return User_Survey_Class.UserSurvey.__hotel_selection_other_rating

    def get_hotel_satisfied_room_cleanliness():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_room_cleanliness

    def get_hotel_satisfied_room_size():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_room_size

    def get_hotel_satisfied_room_quietness():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_room_quietness

    def get_hotel_satisfied_beds_pillows():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_beds_pillows

    def get_hotel_satisfied_pool_size():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_pool_size

    def get_hotel_satisfied_pool_crowds():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_pool_crowds

    def get_hotel_satisfied_pool_cleanliness():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_pool_cleanliness

    def get_hotel_satisfied_parks_shuttle():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_parks_shuttle

    def get_hotel_satisfied_airport_shuttle():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_airport_shuttle

    def get_hotel_satisfied_check_in_out_process():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_check_in_out_process

    def get_hotel_satisfied_staff():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_staff

    def get_hotel_satisfied_recreation_amenities():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_recreation_amenities

    def get_hotel_satisfied_food_court_overall():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_food_court_overall

    def get_hotel_satisfied_food_court_value():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_food_court_value

    def get_hotel_satisfied_find_your_way_around():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_find_your_way_around

    def get_hotel_satisfied_child_services():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_child_services

    def get_hotel_satisfied_sit_down_dining():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_sit_down_dining

    def get_hotel_satisfied_other_string():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_other_string

    def get_hotel_satisfied_other_rating():
        return User_Survey_Class.UserSurvey.__hotel_satisfied_other_rating

    def get_hotel_satisfaction_code():
        return User_Survey_Class.UserSurvey.__hotel_satisfaction_code

    def get_hotel_stay_again():
        return User_Survey_Class.UserSurvey.__hotel_stay_again

    def get_hotel_recommendation_code():
        return User_Survey_Class.UserSurvey.__hotel_recommendation_code

    def get_hotel_room_number():
        return User_Survey_Class.UserSurvey.__hotel_room_number

    def get_hotel_room_connecting():
        return User_Survey_Class.UserSurvey.__hotel_room_connecting

    def get_hotel_room_connecting_room_number():
        return User_Survey_Class.UserSurvey.__hotel_room_connecting_room_number

    def get_hotel_room_bed_code():
        return User_Survey_Class.UserSurvey.__hotel_room_bed_code

    def get_user_id():
        return User_Survey_Class.UserSurvey.__user_id

    def get_party_members():
        return User_Survey_Class.UserSurvey.__party_members

    def get_hometown():
        return User_Survey_Class.UserSurvey.__hometown

    def get_how_many_trips():
        return User_Survey_Class.UserSurvey.__how_many_trips

    def get_ip_address():
        return User_Survey_Class.UserSurvey.__ip_address

    def addListOfSurveysWriteCSV(self):
        self.__listOfSurveys.append(User_Survey_Class.UserSurvey.buildListWriteCSV(self))
        listOfStringSurveys = [str(item) for item in self.__listOfSurveys]
        s = ","
        return s.join(listOfStringSurveys)

##    def __str__(self):
##        return [str(i) for i in addSurvey(self)]
##
##    def writeCSV(self, listOfSurveys):
##        resultString = ""
##        
##        for user_survey in addSurvey(self):
##            resultString += str(User_Survey_Class.UserSurvey.writeCSV()) + " "
##        
##        return resultString
