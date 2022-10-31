class UserSurvey:
    
    def __init__(self):
        
        self.__survey_id = -1
        self.__survey_submitted_at = -1
        self.__trip_start_date = -1
        self.__trip_finish_date = -1
        self.__hotel_name = -1
        self.__hotel_code = -1
        self.__hotel_trip_other_name = -1
        self.__hotel_any_other = -1
        self.__hotel_ritz_carlton = -1
        self.__hotel_super_eight = -1
        self.__hotel_embassy_suites = -1
        self.__hotel_days_inn = -1
        self.__hotel_hampton_inn = -1
        self.__hotel_quality_inn = -1
        self.__hotel_marriott = -1
        self.__hotel_holiday_inn = -1
        self.__hotel_omni = -1
        self.__hotel_hilton = -1
        self.__hotel_millenium = -1
        self.__hotel_radisson = -1
        self.__hotel_hyatt = -1
        self.__hotel_fairfield_inn = -1
        self.__hotel_ramada_inn = -1
        self.__hotel_drury_inn = -1
        self.__hotel_four_seasons = -1
        self.__hotel_best_western = -1
        self.__hotel_past_other_name = -1
        self.__hotel_selection_cost = -1
        self.__hotel_selection_bar = -1
        self.__hotel_selection_distance_to_parks = -1
        self.__hotel_selection_in_room_dining = -1
        self.__hotel_selection_food_court = -1
        self.__hotel_selection_sit_down_dining = -1
        self.__hotel_selection_fine_dining = -1
        self.__hotel_selection_parks_shuttle = -1
        self.__hotel_selection_airport_shuttle = -1
        self.__hotel_selection_in_room_kitchen = -1
        self.__hotel_selection_room_size = -1
        self.__hotel_selection_multiple_bedroom_suites = -1
        self.__hotel_selection_spa_fitness_center = -1
        self.__hotel_selection_pool = -1
        self.__hotel_selection_theme = -1
        self.__hotel_selection_kids_activities = -1
        self.__hotel_selection_location_on_property = -1
        self.__hotel_selection_other_string = -1
        self.__hotel_selection_other_rating = -1
        self.__hotel_satisfied_room_cleanliness = -1
        self.__hotel_satisfied_room_size = -1
        self.__hotel_satisfied_room_quietness = -1
        self.__hotel_satisfied_beds_pillows = -1
        self.__hotel_satisfied_pool_size = -1
        self.__hotel_satisfied_pool_crowds = -1
        self.__hotel_satisfied_pool_cleanliness = -1
        self.__hotel_satisfied_parks_shuttle = -1
        self.__hotel_satisfied_airport_shuttle = -1
        self.__hotel_satisfied_check_in_out_process = -1
        self.__hotel_satisfied_staff = -1
        self.__hotel_satisfied_recreation_amenities = -1
        self.__hotel_satisfied_food_court_overall = -1
        self.__hotel_satisfied_food_court_value = -1
        self.__hotel_satisfied_find_your_way_around = -1
        self.__hotel_satisfied_child_services = -1
        self.__hotel_satisfied_sit_down_dining = -1
        self.__hotel_satisfied_other_string = -1
        self.__hotel_satisfied_other_rating = -1
        self.__hotel_satisfaction_code = -1
        self.__hotel_stay_again = -1
        self.__hotel_recommendation_code = -1
        self.__hotel_room_number = -1
        self.__hotel_room_connecting = -1
        self.__hotel_room_connecting_room_number = -1
        self.__hotel_room_bed_code = -1
        self.__user_id = -1
        self.__party_members = -1
        self.__hometown = -1
        self.__how_many_trips = -1
        self.__ip_address = -1
        

    def __init__(self, \
                 survey_id = -1, \
                 survey_submitted_at = -1, \
                 trip_start_date = -1, \
                 trip_finish_date = -1, \
                 hotel_name = -1, \
                 hotel_code = -1, \
                 hotel_trip_other_name = -1, \
                 hotel_any_other = -1, \
                 hotel_ritz_carlton = -1, \
                 hotel_super_eight = -1, \
                 hotel_embassy_suites = -1, \
                 hotel_days_inn = -1, \
                 hotel_hampton_inn = -1, \
                 hotel_quality_inn = -1, \
                 hotel_marriott = -1, \
                 hotel_holiday_inn = -1, \
                 hotel_omni = -1, \
                 hotel_hilton = -1, \
                 hotel_millenium = -1, \
                 hotel_radisson = -1, \
                 hotel_hyatt = -1, \
                 hotel_fairfield_inn = -1, \
                 hotel_ramada_inn = -1, \
                 hotel_drury_inn = -1, \
                 hotel_four_seasons = -1, \
                 hotel_best_western = -1, \
                 hotel_past_other_name = -1, \
                 hotel_selection_cost = -1, \
                 hotel_selection_bar = -1, \
                 hotel_selection_distance_to_parks = -1, \
                 hotel_selection_in_room_dining = -1, \
                 hotel_selection_food_court = -1, \
                 hotel_selection_sit_down_dining = -1, \
                 hotel_selection_fine_dining = -1, \
                 hotel_selection_parks_shuttle = -1, \
                 hotel_selection_airport_shuttle = -1, \
                 hotel_selection_in_room_kitchen = -1, \
                 hotel_selection_room_size = -1, \
                 hotel_selection_multiple_bedroom_suites = -1, \
                 hotel_selection_spa_fitness_center = -1, \
                 hotel_selection_pool = -1, \
                 hotel_selection_theme = -1, \
                 hotel_selection_kids_activities = -1, \
                 hotel_selection_location_on_property = -1, \
                 hotel_selection_other_string = -1, \
                 hotel_selection_other_rating = -1, \
                 hotel_satisfied_room_cleanliness = -1, \
                 hotel_satisfied_room_size = -1, \
                 hotel_satisfied_room_quietness = -1, \
                 hotel_satisfied_beds_pillows = -1, \
                 hotel_satisfied_pool_size = -1, \
                 hotel_satisfied_pool_crowds = -1, \
                 hotel_satisfied_pool_cleanliness = -1, \
                 hotel_satisfied_parks_shuttle = -1, \
                 hotel_satisfied_airport_shuttle = -1, \
                 hotel_satisfied_check_in_out_process = -1, \
                 hotel_satisfied_staff = -1, \
                 hotel_satisfied_recreation_amenities = -1, \
                 hotel_satisfied_food_court_overall = -1, \
                 hotel_satisfied_food_court_value = -1, \
                 hotel_satisfied_find_your_way_around = -1, \
                 hotel_satisfied_child_services = -1, \
                 hotel_satisfied_sit_down_dining = -1, \
                 hotel_satisfied_other_string = -1, \
                 hotel_satisfied_other_rating = -1, \
                 hotel_satisfaction_code = -1, \
                 hotel_stay_again = -1, \
                 hotel_recommendation_code = -1, \
                 hotel_room_number = -1, \
                 hotel_room_connecting = -1, \
                 hotel_room_connecting_room_number = -1, \
                 hotel_room_bed_code = -1, \
                 user_id = -1, \
                 party_members = -1, \
                 hometown = -1, \
                 how_many_trips = -1, \
                 ip_address = -1):
        
        self.__survey_id = survey_id
        self.__survey_submitted_at = survey_submitted_at
        self.__trip_start_date = trip_start_date
        self.__trip_finish_date = trip_finish_date
        self.__hotel_name = hotel_name
        self.__hotel_code = hotel_code
        self.__hotel_trip_other_name = hotel_trip_other_name
        self.__hotel_any_other = hotel_any_other
        self.__hotel_ritz_carlton = hotel_ritz_carlton
        self.__hotel_super_eight = hotel_super_eight
        self.__hotel_embassy_suites = hotel_embassy_suites
        self.__hotel_days_inn = hotel_days_inn
        self.__hotel_hampton_inn = hotel_hampton_inn
        self.__hotel_quality_inn = hotel_quality_inn
        self.__hotel_marriott = hotel_marriott
        self.__hotel_holiday_inn = hotel_holiday_inn
        self.__hotel_omni = hotel_omni
        self.__hotel_hilton = hotel_hilton
        self.__hotel_millenium = hotel_millenium
        self.__hotel_radisson = hotel_radisson
        self.__hotel_hyatt = hotel_hyatt
        self.__hotel_fairfield_inn = hotel_fairfield_inn
        self.__hotel_ramada_inn = hotel_ramada_inn
        self.__hotel_drury_inn = hotel_drury_inn
        self.__hotel_four_seasons = hotel_four_seasons
        self.__hotel_best_western = hotel_best_western
        self.__hotel_past_other_name = hotel_past_other_name
        self.__hotel_selection_cost = hotel_selection_cost
        self.__hotel_selection_bar = hotel_selection_bar
        self.__hotel_selection_distance_to_parks = hotel_selection_distance_to_parks
        self.__hotel_selection_in_room_dining = hotel_selection_in_room_dining
        self.__hotel_selection_food_court = hotel_selection_food_court
        self.__hotel_selection_sit_down_dining = hotel_selection_sit_down_dining
        self.__hotel_selection_fine_dining = hotel_selection_fine_dining
        self.__hotel_selection_parks_shuttle = hotel_selection_parks_shuttle
        self.__hotel_selection_airport_shuttle = hotel_selection_airport_shuttle
        self.__hotel_selection_in_room_kitchen = hotel_selection_in_room_kitchen
        self.__hotel_selection_room_size = hotel_selection_room_size
        self.__hotel_selection_multiple_bedroom_suites = hotel_selection_multiple_bedroom_suites
        self.__hotel_selection_spa_fitness_center = hotel_selection_spa_fitness_center
        self.__hotel_selection_pool = hotel_selection_pool
        self.__hotel_selection_theme = hotel_selection_theme
        self.__hotel_selection_kids_activities = hotel_selection_kids_activities
        self.__hotel_selection_location_on_property = hotel_selection_location_on_property
        self.__hotel_selection_other_string = hotel_selection_other_string
        self.__hotel_selection_other_rating = hotel_selection_other_rating
        self.__hotel_satisfied_room_cleanliness = hotel_satisfied_room_cleanliness
        self.__hotel_satisfied_room_size = hotel_satisfied_room_size
        self.__hotel_satisfied_room_quietness = hotel_satisfied_room_quietness
        self.__hotel_satisfied_beds_pillows = hotel_satisfied_beds_pillows
        self.__hotel_satisfied_pool_size = hotel_satisfied_pool_size
        self.__hotel_satisfied_pool_crowds = hotel_satisfied_pool_crowds
        self.__hotel_satisfied_pool_cleanliness = hotel_satisfied_pool_cleanliness
        self.__hotel_satisfied_parks_shuttle = hotel_satisfied_parks_shuttle
        self.__hotel_satisfied_airport_shuttle = hotel_satisfied_airport_shuttle
        self.__hotel_satisfied_check_in_out_process = hotel_satisfied_check_in_out_process
        self.__hotel_satisfied_staff = hotel_satisfied_staff
        self.__hotel_satisfied_recreation_amenities = hotel_satisfied_recreation_amenities
        self.__hotel_satisfied_food_court_overall = hotel_satisfied_food_court_overall
        self.__hotel_satisfied_food_court_value = hotel_satisfied_food_court_value
        self.__hotel_satisfied_find_your_way_around = hotel_satisfied_find_your_way_around
        self.__hotel_satisfied_child_services = hotel_satisfied_child_services
        self.__hotel_satisfied_sit_down_dining = hotel_satisfied_sit_down_dining
        self.__hotel_satisfied_other_string = hotel_satisfied_other_string
        self.__hotel_satisfied_other_rating = hotel_satisfied_other_rating
        self.__hotel_satisfaction_code = hotel_satisfaction_code
        self.__hotel_stay_again = hotel_stay_again
        self.__hotel_recommendation_code = hotel_recommendation_code
        self.__hotel_room_number = hotel_room_number
        self.__hotel_room_connecting = hotel_room_connecting
        self.__hotel_room_connecting_room_number = hotel_room_connecting_room_number
        self.__hotel_room_bed_code = hotel_room_bed_code
        self.__user_id = user_id
        self.__party_members = party_members
        self.__hometown = hometown
        self.__how_many_trips = how_many_trips
        self.__ip_address = ip_address

    def get_survey_id(self):
        return self.__survey_id

    def get_survey_submitted_at(self):
        return self.__survey_submitted_at

    def get_trip_start_date(self):
        return self.__trip_start_date

    def get_trip_finish_date(self):
        return self.__trip_finish_date

    def get_hotel_name(self):
        return self.__hotel_name

    def get_hotel_code(self):
        return self.__hotel_code

    def get_hotel_trip_other_name(self):
        return self.__hotel_trip_other_name

    def get_hotel_any_other(self):
        return self.__hotel_any_other

    def get_hotel_ritz_carlton(self):
        return self.__hotel_ritz_carlton

    def get_hotel_super_eight(self):
        return self.__hotel_super_eight

    def get_hotel_embassy_suites(self):
        return self.__hotel_embassy_suites

    def get_hotel_days_inn(self):
        return self.__hotel_days_inn

    def get_hotel_hampton_inn(self):
        return self.__hotel_hampton_inn

    def get_hotel_quality_inn(self):
        return self.__hotel_quality_inn

    def get_hotel_marriott(self):
        return self.__hotel_marriott

    def get_hotel_holiday_inn(self):
        return self.__hotel_holiday_inn

    def get_hotel_omni(self):
        return self.__hotel_omni

    def get_hotel_hilton(self):
        return self.__hotel_hilton

    def get_hotel_millenium(self):
        return self.__hotel_millenium

    def get_hotel_radisson(self):
        return self.__hotel_radisson

    def get_hotel_hyatt(self):
        return self.__hotel_hyatt

    def get_hotel_fairfield_inn(self):
        return self.__hotel_fairfield_inn

    def get_hotel_ramada_inn(self):
        return self.__hotel_ramada_inn

    def get_hotel_drury_inn(self):
        return self.__hotel_drury_inn

    def get_hotel_four_seasons(self):
        return self.__hotel_four_seasons

    def get_hotel_best_western(self):
        return self.__hotel_best_western

    def get_hotel_past_other_name(self):
        return self.__hotel_past_other_name
    
    def get_hotel_selection_cost(self):
        return self.__hotel_selection_cost

    def get_hotel_selection_bar(self):
        return self.__hotel_selection_bar

    def get_hotel_selection_distance_to_parks(self):
        return self.__hotel_selection_distance_to_parks

    def get_hotel_selection_in_room_dining(self):
        return self.__hotel_selection_in_room_dining

    def get_hotel_selection_food_court(self):
        return self.__hotel_selection_food_court

    def get_hotel_selection_sit_down_dining(self):
        return self.__hotel_selection_sit_down_dining

    def get_hotel_selection_fine_dining(self):
        return self.__hotel_selection_fine_dining

    def get_hotel_selection_parks_shuttle(self):
        return self.__hotel_selection_parks_shuttle

    def get_hotel_selection_airport_shuttle(self):
        return self.__hotel_selection_airport_shuttle

    def get_hotel_selection_in_room_kitchen(self):
        return self.__hotel_selection_in_room_kitchen

    def get_hotel_selection_room_size(self):
        return self.__hotel_selection_room_size

    def get_hotel_selection_multiple_bedroom_suites(self):
        return self.__hotel_selection_multiple_bedroom_suites

    def get_hotel_selection_spa_fitness_center(self):
        return self.__hotel_selection_spa_fitness_center

    def get_hotel_selection_pool(self):
        return self.__hotel_selection_pool

    def get_hotel_selection_theme(self):
        return self.__hotel_selection_theme

    def get_hotel_selection_kids_activities(self):
        return self.__hotel_selection_kids_activities

    def get_hotel_selection_location_on_property(self):
        return self.__hotel_selection_location_on_property

    def get_hotel_selection_other_string(self):
        return self.__hotel_selection_other_string

    def get_hotel_selection_other_rating(self):
        return self.__hotel_selection_other_rating

    def get_hotel_satisfied_room_cleanliness(self):
        return self.__hotel_satisfied_room_cleanliness

    def get_hotel_satisfied_room_size(self):
        return self.__hotel_satisfied_room_size

    def get_hotel_satisfied_room_quietness(self):
        return self.__hotel_satisfied_room_quietness

    def get_hotel_satisfied_beds_pillows(self):
        return self.__hotel_satisfied_beds_pillows

    def get_hotel_satisfied_pool_size(self):
        return self.__hotel_satisfied_pool_size

    def get_hotel_satisfied_pool_crowds(self):
        return self.__hotel_satisfied_pool_crowds

    def get_hotel_satisfied_pool_cleanliness(self):
        return self.__hotel_satisfied_pool_cleanliness

    def get_hotel_satisfied_parks_shuttle(self):
        return self.__hotel_satisfied_parks_shuttle

    def get_hotel_satisfied_airport_shuttle(self):
        return self.__hotel_satisfied_airport_shuttle

    def get_hotel_satisfied_check_in_out_process(self):
        return self.__hotel_satisfied_check_in_out_process

    def get_hotel_satisfied_staff(self):
        return self.__hotel_satisfied_staff

    def get_hotel_satisfied_recreation_amenities(self):
        return self.__hotel_satisfied_recreation_amenities

    def get_hotel_satisfied_food_court_overall(self):
        return self.__hotel_satisfied_food_court_overall

    def get_hotel_satisfied_food_court_value(self):
        return self.__hotel_satisfied_food_court_value

    def get_hotel_satisfied_find_your_way_around(self):
        return self.__hotel_satisfied_find_your_way_around

    def get_hotel_satisfied_child_services(self):
        return self.__hotel_satisfied_child_services

    def get_hotel_satisfied_sit_down_dining(self):
        return self.__hotel_satisfied_sit_down_dining

    def get_hotel_satisfied_other_string(self):
        return self.__hotel_satisfied_other_string

    def get_hotel_satisfied_other_rating(self):
        return self.__hotel_satisfied_other_rating

    def get_hotel_satisfaction_code(self):
        return self.__hotel_satisfaction_code

    def get_hotel_stay_again(self):
        return self.__hotel_stay_again

    def get_hotel_recommendation_code(self):
        return self.__hotel_recommendation_code

    def get_hotel_room_number(self):
        return self.__hotel_room_number

    def get_hotel_room_connecting(self):
        return self.__hotel_room_connecting

    def get_hotel_room_connecting_room_number(self):
        return self.__hotel_room_connecting_room_number

    def get_hotel_room_bed_code(self):
        return self.__hotel_room_bed_code

    def get_user_id(self):
        return self.__user_id

    def get_party_members(self):
        return self.__party_members

    def get_hometown(self):
        return self.__hometown

    def get_how_many_trips(self):
        return self.__how_many_trips

    def get_ip_address(self):
        return self.__ip_address

    def buildListWriteCSV(self):
        resultList = []
        resultList.append(self.__survey_id)
        resultList.append(self.__survey_submitted_at)
        resultList.append(self.__trip_start_date)
        resultList.append(self.__trip_finish_date)
        resultList.append(self.__hotel_name)
        resultList.append(self.__hotel_code)
        resultList.append(self.__hotel_trip_other_name)
        resultList.append(self.__hotel_any_other)
        resultList.append(self.__hotel_ritz_carlton)
        resultList.append(self.__hotel_super_eight)
        resultList.append(self.__hotel_embassy_suites)
        resultList.append(self.__hotel_days_inn)
        resultList.append(self.__hotel_hampton_inn)
        resultList.append(self.__hotel_quality_inn)
        resultList.append(self.__hotel_marriott)
        resultList.append(self.__hotel_holiday_inn)
        resultList.append(self.__hotel_millenium)
        resultList.append(self.__hotel_radisson)
        resultList.append(self.__hotel_hyatt)
        resultList.append(self.__hotel_fairfield_inn)
        resultList.append(self.__hotel_ramada_inn)
        resultList.append(self.__hotel_drury_inn)
        resultList.append(self.__hotel_four_seasons)
        resultList.append(self.__hotel_best_western)
        resultList.append(self.__hotel_past_other_name)
        resultList.append(self.__hotel_selection_cost)
        resultList.append(self.__hotel_selection_bar)
        resultList.append(self.__hotel_selection_distance_to_parks)
        resultList.append(self.__hotel_selection_in_room_dining)
        resultList.append(self.__hotel_selection_food_court)
        resultList.append(self.__hotel_selection_sit_down_dining)
        resultList.append(self.__hotel_selection_fine_dining)
        resultList.append(self.__hotel_selection_parks_shuttle)
        resultList.append(self.__hotel_selection_airport_shuttle)
        resultList.append(self.__hotel_selection_in_room_kitchen)
        resultList.append(self.__hotel_selection_room_size)
        resultList.append(self.__hotel_selection_multiple_bedroom_suites)
        resultList.append(self.__hotel_selection_spa_fitness_center)
        resultList.append(self.__hotel_selection_pool)
        resultList.append(self.__hotel_selection_theme)
        resultList.append(self.__hotel_selection_kids_activities)
        resultList.append(self.__hotel_selection_location_on_property)
        resultList.append(self.__hotel_selection_other_string)
        resultList.append(self.__hotel_selection_other_rating)
        resultList.append(self.__hotel_satisfied_room_cleanliness)
        resultList.append(self.__hotel_satisfied_room_size)
        resultList.append(self.__hotel_satisfied_room_quietness)
        resultList.append(self.__hotel_satisfied_beds_pillows)
        resultList.append(self.__hotel_satisfied_pool_size)
        resultList.append(self.__hotel_satisfied_pool_crowds)
        resultList.append(self.__hotel_satisfied_pool_cleanliness)
        resultList.append(self.__hotel_satisfied_parks_shuttle)
        resultList.append(self.__hotel_satisfied_airport_shuttle)
        resultList.append(self.__hotel_satisfied_check_in_out_process)
        resultList.append(self.__hotel_satisfied_staff)
        resultList.append(self.__hotel_satisfied_recreation_amenities)
        resultList.append(self.__hotel_satisfied_food_court_overall)
        resultList.append(self.__hotel_satisfied_food_court_value)
        resultList.append(self.__hotel_satisfied_find_your_way_around)
        resultList.append(self.__hotel_satisfied_child_services)
        resultList.append(self.__hotel_satisfied_sit_down_dining)
        resultList.append(self.__hotel_satisfied_other_string)
        resultList.append(self.__hotel_satisfied_other_rating)
        resultList.append(self.__hotel_satisfaction_code)
        resultList.append(self.__hotel_stay_again)
        resultList.append(self.__hotel_recommendation_code)
        resultList.append(self.__hotel_room_number)
        resultList.append(self.__hotel_room_connecting)
        resultList.append(self.__hotel_room_connecting_room_number)
        resultList.append(self.__hotel_room_bed_code)
        resultList.append(self.__user_id)
        resultList.append(self.__party_members)
        resultList.append(self.__hometown)
        resultList.append(self.__how_many_trips)
        resultList.append(self.__ip_address)
        
        resultList = [str(item) for item in resultList]
        s = ","
        return s.join(resultList)
                          
    ## def writeCSV(self):
    ##    L = [str(item) for item in self.__resultList]
    ##    s = ","
    ##    return s.join(L)
            
            

            

            

            
















        





















        










