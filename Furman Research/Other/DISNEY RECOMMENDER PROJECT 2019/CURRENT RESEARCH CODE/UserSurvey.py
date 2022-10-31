import Group
import Timestamp
import RoomsData
#import SeasonCalculator
import SurveySubmittedTimestamp
import project_globals
## import DisneySeasonCalculator
import AgeCategories
from collections import OrderedDict
import Header

PARTY_SIZE = "party_size"

def UpdateMetadataTitles(survey_header):
    
    """ All applicable column titles are added here."""

    survey_header.append(PARTY_SIZE)

         #Party Group Compuatation 
#        self.od[] = group.getPartySize()
#        #print(self.od["party_size"])
#        self.od["num_males"] = group.getNumMales()
#        self.od["num_females"] = group.getNumFemales()
#        self.od["ages"] = group.getAges()
#        self.od["age_categories"] = age_categories.getFrequencyCount(self.od["ages"])
#        self.od["male_ages"] = group.getAgesMale()
#        self.od["female_ages"] = group.getAgesFemale()
#        self.od["male_age_categories"] = age_categories.getFrequencyCountMale(self.od["male_ages"])
#        self.od["female_age_categories"] = age_categories.getFrequencyCountFemale(self.od["female_ages"])


class UserSurvey:
    
    
#    def __init__(self):
#        self.od = OrderedDict()
#        self.od["survey_id"] = -1
#        self.od["survey_submitted_at"] = -1
#        self.od["trip_start_date"] = -1
#        self.od["trip_finish_date"] = -1
#        self.od["hotel_name"] = -1
#        self.od["hotel_code"] = -1
#        self.od["hotel_trip_other_name"] = -1
#        self.od["hotel_trip_other_name_2"] = -1
#        self.od["hotel_trip_other_name_3"] = -1
#        self.od["hotel_any_other"] = -1
#        self.od["hotel_ritz_carlton"] = -1
#        self.od["hotel_super_eight"] = -1
#        self.od["hotel_embassy_suites"] = -1
#        self.od["hotel_days_inn"] = -1
#        self.od["hotel_hampton_inn"] = -1
#        self.od["hotel_quality_inn"] = -1
#        self.od["hotel_marriott"] = -1
#        self.od["hotel_holiday_inn"] = -1
#        self.od["hotel_omni"] = -1
#        self.od["hotel_hilton"] = -1
#        self.od["hotel_millenium"] = -1
#        self.od["hotel_radisson"] = -1
#        self.od["hotel_hyatt"] = -1
#        self.od["hotel_fairfield_inn"] = -1
#        self.od["hotel_ramada_inn"] = -1
#        self.od["hotel_drury_inn"] = -1
#        self.od["hotel_four_seasons"] = -1
#        self.od["hotel_best_western"] = -1
#        self.od["hotel_past_other_name_1"] = -1
#        self.od["hotel_past_other_name_2"] = -1
#        self.od["hotel_past_other_name_3"] = -1
#        self.od["hotel_past_other_name_4"] = -1
#        self.od["hotel_past_other_name_5"] = -1
#        self.od["hotel_past_other_name_6"] = -1
#        self.od["hotel_past_other_name_7"] = -1
#        self.od["hotel_past_other_name_8"] = -1
#        self.od["hotel_selection_cost"] = -1
#        self.od["hotel_selection_bar"] = -1
#        self.od["hotel_selection_distance_to_parks"] = -1
#        self.od["hotel_selection_in_room_dining"] = -1
#        self.od["hotel_selection_food_court"] = -1
#        self.od["hotel_selection_sit_down_dining"] = -1
#        self.od["hotel_selection_fine_dining"] = -1
#        self.od["hotel_selection_parks_shuttle"] = -1
#        self.od["hotel_selection_airport_shuttle"] = -1
#        self.od["hotel_selection_in_room_kitchen"] = -1
#        self.od["hotel_selection_room_size"] = -1
#        self.od["hotel_selection_multiple_bedroom_suites"] = -1
#        self.od["hotel_selection_pool"] = -1
#        self.od["hotel_selection_theme"] = -1
#        self.od["hotel_selection_kids_activities"] = -1
#        self.od["hotel_selection_location_on_property"] = -1
#        self.od["hotel_selection_other_string"] = -1
#        self.od["hotel_selection_other_string_2"] = -1
#        self.od["hotel_selection_other_string_3"] = -1
#        self.od["hotel_selection_other_rating"] = -1
#        self.od["hotel_satisfied_room_cleanliness"] = -1
#        self.od["hotel_satisfied_room_size"] = -1
#        self.od["hotel_satisfied_room_quietness"] = -1
#        self.od["hotel_satisfied_beds_pillows"] = -1
#        self.od["hotel_satisfied_pool_size"] = -1
#        self.od["hotel_satisfied_pool_crowds"] = -1
#        self.od["hotel_satisfied_pool_cleanliness"] = -1
#        self.od["hotel_satisfied_parks_shuttle"] = -1
#        self.od["hotel_satisfied_airport_shuttle"] = -1
#        self.od["hotel_satisfied_check_in_out_process"] = -1
#        self.od["hotel_satisfied_staff"] = -1
#        self.od["hotel_satisfied_recreation_amenities"] = -1
#        self.od["hotel_satisfied_food_court_overall"] = -1
#        self.od["hotel_satisfied_food_court_value"] = -1
#        self.od["hotel_satisfied_find_your_way_around"] = -1
#        self.od["hotel_satisfied_child_services"] = -1
#        self.od["hotel_satisfied_sit_down_dining"] = -1
#        self.od["hotel_satisfaction_code"] = -1
#        self.od["hotel_stay_again"] = -1
#        self.od["hotel_recommendation_code"] = -1
#        self.od["hotel_room_number"] = -1
#        self.od["hotel_room_number_2"] = -1
#        self.od["hotel_room_number_3"] = -1
#        self.od["hotel_room_connecting"] = -1
#        self.od["hotel_room_connecting_room_number"] = -1
#        self.od["hotel_room_connecting_room_number_2"] = -1
#        self.od["hotel_room_bed_code"] = -1
#        self.od["user_id"] = -1
#        self.od["party_members"] = -1
#        self.od["town_city"] = -1
#        self.od["state_province"] = -1
#        self.od["international_country"] = -1
#        self.od["how_many_trips"] = -1
#        self.od["ip_address"] = -1
  
    def __init__(self, header, rowList):
        self.__surveyHeader = header

        # Populate the survey dictionary
        self.__dict = {}
        for index in range(len(header)):
            self.__dict[header[index]] = rowList[index]
    
#    """SOS do we need to delete all these inputs and put a list?"""  
#    def __init__(self, \
#                 survey_id = '', \
#                 survey_submitted_at = '', \
#                 trip_start_date = -1, \
#                 trip_finish_date = -1, \
#                 hotel_name = -1, \
#                 hotel_code = -1, \
#                 hotel_trip_other_name = -1, \
#                 hotel_trip_other_name_2 = -1, \
#                 hotel_trip_other_name_3 = -1, \
#                 hotel_any_other = -1, \
#                 hotel_ritz_carlton = -1, \
#                 hotel_super_eight = -1, \
#                 hotel_embassy_suites = -1, \
#                 hotel_days_inn = -1, \
#                 hotel_hampton_inn = -1, \
#                 hotel_quality_inn = -1, \
#                 hotel_marriott = -1, \
#                 hotel_holiday_inn = -1, \
#                 hotel_omni = -1, \
#                 hotel_hilton = -1, \
#                 hotel_millenium = -1, \
#                 hotel_radisson = -1, \
#                 hotel_hyatt = -1, \
#                 hotel_fairfield_inn = -1, \
#                 hotel_ramada_inn = -1, \
#                 hotel_drury_inn = -1, \
#                 hotel_four_seasons = -1, \
#                 hotel_best_western = -1, \
#                 hotel_past_other_name_1 = -1, \
#                 hotel_past_other_name_2 = -1, \
#                 hotel_past_other_name_3 = -1, \
#                 hotel_past_other_name_4 = -1, \
#                 hotel_past_other_name_5 = -1, \
#                 hotel_past_other_name_6 = -1, \
#                 hotel_past_other_name_7 = -1, \
#                 hotel_past_other_name_8 = -1, \
#                 hotel_selection_cost = -1, \
#                 hotel_selection_bar = -1, \
#                 hotel_selection_distance_to_parks = -1, \
#                 hotel_selection_in_room_dining = -1, \
#                 hotel_selection_food_court = -1, \
#                 hotel_selection_sit_down_dining = -1, \
#                 hotel_selection_fine_dining = -1, \
#                 hotel_selection_parks_shuttle = -1, \
#                 hotel_selection_airport_shuttle = -1, \
#                 hotel_selection_in_room_kitchen = -1, \
#                 hotel_selection_room_size = -1, \
#                 hotel_selection_multiple_bedroom_suites = -1, \
#                 hotel_selection_pool = -1, \
#                 hotel_selection_theme = -1, \
#                 hotel_selection_kids_activities = -1, \
#                 hotel_selection_location_on_property = -1, \
#                 hotel_selection_other_string = -1, \
#                 hotel_selection_other_string_2 = -1, \
#                 hotel_selection_other_string_3 = -1, \
#                 hotel_selection_other_rating = -1, \
#                 hotel_satisfied_room_cleanliness = -1, \
#                 hotel_satisfied_room_size = -1, \
#                 hotel_satisfied_room_quietness = -1, \
#                 hotel_satisfied_beds_pillows = -1, \
#                 hotel_satisfied_pool_size = -1, \
#                 hotel_satisfied_pool_crowds = -1, \
#                 hotel_satisfied_pool_cleanliness = -1, \
#                 hotel_satisfied_parks_shuttle = -1, \
#                 hotel_satisfied_airport_shuttle = -1, \
#                 hotel_satisfied_check_in_out_process = -1, \
#                 hotel_satisfied_staff = -1, \
#                 hotel_satisfied_recreation_amenities = -1, \
#                 hotel_satisfied_food_court_overall = -1, \
#                 hotel_satisfied_food_court_value = -1, \
#                 hotel_satisfied_find_your_way_around = -1, \
#                 hotel_satisfied_child_services = -1, \
#                 hotel_satisfied_sit_down_dining = -1, \
#                 hotel_satisfaction_code = -1, \
#                 hotel_stay_again = -1, \
#                 hotel_recommendation_code = -1, \
#                 hotel_room_number = -1, \
#                 hotel_room_number_2 = -1, \
#                 hotel_room_number_3 = -1, \
#                 hotel_room_connecting = -1, \
#                 hotel_room_connecting_room_number = -1, \
#                 hotel_room_connecting_room_number_2 = -1, \
#                 hotel_room_bed_code = -1, \
#                 user_id = -1, \
#                 party_members = -1, \
#                 town_city = -1, \
#                 state_province = -1, \
#                 international_country = -1, \
#                 how_many_trips = -1, \
#                 ip_address = -1):
#        
#    
#        
#        self.od = OrderedDict()
#        #od = OrderedDict()
#        
#        self.od['survey_id'] = survey_id
#        self.od['survey_submitted_at'] = survey_submitted_at
#        self.od['trip_start_date'] = trip_start_date
#        self.od['trip_finish_date'] = trip_finish_date
#        self.od['hotel_name'] = hotel_name
#        self.od['hotel_code'] = hotel_code
#        self.od['hotel_trip_other_name'] = hotel_trip_other_name
#        self.od['hotel_trip_other_name_2'] = hotel_trip_other_name_2
#        self.od['hotel_trip_other_name_3'] = hotel_trip_other_name_3
#        self.od['hotel_any_other'] = hotel_any_other
#        self.od['hotel_ritz_carlton'] = hotel_ritz_carlton
#        self.od['hotel_super_eight'] = hotel_super_eight
#        self.od['hotel_embassy_suites'] = hotel_embassy_suites
#        self.od['hotel_days_inn'] = hotel_days_inn
#        self.od['hotel_hampton_inn'] = hotel_hampton_inn
#        self.od['hotel_quality_inn'] = hotel_quality_inn
#        self.od['hotel_marriott'] = hotel_marriott
#        self.od['hotel_holiday_inn'] = hotel_holiday_inn
#        self.od['hotel_omni'] = hotel_omni
#        self.od['hotel_hilton'] = hotel_hilton
#        self.od['hotel_millenium'] = hotel_millenium
#        self.od['hotel_radisson'] = hotel_radisson
#        self.od['hotel_hyatt'] = hotel_hyatt
#        self.od['hotel_fairfield_inn'] = hotel_fairfield_inn
#        self.od['hotel_ramada_inn'] = hotel_ramada_inn
#        self.od['hotel_drury_inn'] = hotel_drury_inn
#        self.od['hotel_four_seasons'] = hotel_four_seasons
#        self.od['hotel_best_western'] = hotel_best_western
#        self.od['hotel_past_other_name_1'] = hotel_past_other_name_1
#        self.od['hotel_past_other_name_2'] = hotel_past_other_name_2
#        self.od['hotel_past_other_name_3'] = hotel_past_other_name_3
#        self.od['hotel_past_other_name_4'] = hotel_past_other_name_4
#        self.od['hotel_past_other_name_5'] = hotel_past_other_name_5
#        self.od['hotel_past_other_name_6'] = hotel_past_other_name_6
#        self.od['hotel_past_other_name_7'] = hotel_past_other_name_7
#        self.od['hotel_past_other_name_8'] = hotel_past_other_name_8
#        self.od['hotel_selection_cost'] = hotel_selection_cost
#        self.od['hotel_selection_bar'] = hotel_selection_bar
#        self.od['hotel_selection_distance_to_parks'] = hotel_selection_distance_to_parks
#        self.od['hotel_selection_in_room_dining'] = hotel_selection_in_room_dining
#        self.od['hotel_selection_food_court'] = hotel_selection_food_court
#        self.od['hotel_selection_sit_down_dining'] = hotel_selection_sit_down_dining
#        self.od['hotel_selection_fine_dining'] = hotel_selection_fine_dining
#        self.od['hotel_selection_parks_shuttle'] = hotel_selection_parks_shuttle
#        self.od['hotel_selection_airport_shuttle'] = hotel_selection_airport_shuttle
#        self.od['hotel_selection_in_room_kitchen'] = hotel_selection_in_room_kitchen
#        self.od['hotel_selection_room_size'] = hotel_selection_room_size
#        self.od['hotel_selection_multiple_bedroom_suites'] = hotel_selection_multiple_bedroom_suites
#        self.od['hotel_selection_pool'] = hotel_selection_pool
#        self.od['hotel_selection_theme'] = hotel_selection_theme
#        self.od['hotel_selection_kids_activities'] = hotel_selection_kids_activities
#        self.od['hotel_selection_location_on_property']= hotel_selection_location_on_property
#        self.od['hotel_selection_other_string'] = hotel_selection_other_string
#        self.od['hotel_selection_other_string_2'] = hotel_selection_other_string_2
#        self.od['hotel_selection_other_string_3'] = hotel_selection_other_string_3
#        self.od['hotel_selection_other_rating'] = hotel_selection_other_rating
#        self.od['hotel_satisfied_room_cleanliness'] = hotel_satisfied_room_cleanliness
#        self.od['hotel_satisfied_room_size'] = hotel_satisfied_room_size
#        self.od['hotel_satisfied_room_quietness'] = hotel_satisfied_room_quietness
#        self.od['hotel_satisfied_beds_pillows'] = hotel_satisfied_beds_pillows
#        self.od['hotel_satisfied_pool_size'] = hotel_satisfied_pool_size
#        self.od['hotel_satisfied_pool_crowds'] = hotel_satisfied_pool_crowds
#        self.od['hotel_satisfied_pool_cleanliness'] = hotel_satisfied_pool_cleanliness
#        self.od['hotel_satisfied_parks_shuttle'] = hotel_satisfied_parks_shuttle
#        self.od['hotel_satisfied_airport_shuttle'] = hotel_satisfied_airport_shuttle
#        self.od['hotel_satisfied_check_in_out_process'] = hotel_satisfied_check_in_out_process
#        self.od['hotel_satisfied_staff'] = hotel_satisfied_staff
#        self.od['hotel_satisfied_recreation_amenities'] = hotel_satisfied_recreation_amenities
#        self.od['hotel_satisfied_food_court_overall'] = hotel_satisfied_food_court_overall
#        self.od['hotel_satisfied_food_court_value'] = hotel_satisfied_food_court_value
#        self.od['hotel_satisfied_find_your_way_around'] = hotel_satisfied_find_your_way_around
#        self.od['hotel_satisfied_child_services'] = hotel_satisfied_child_services
#        self.od['hotel_satisfied_sit_down_dining'] = hotel_satisfied_sit_down_dining
#        self.od['hotel_satisfaction_code'] = hotel_satisfaction_code
#        self.od['hotel_stay_again'] = hotel_stay_again
#        self.od['hotel_recommendation_code'] = hotel_recommendation_code
#        self.od['hotel_room_number'] = hotel_room_number
#        self.od['hotel_room_number_2'] = hotel_room_number_2
#        self.od['hotel_room_number_3'] = hotel_room_number_3
#        self.od['hotel_room_connecting'] = hotel_room_connecting
#        self.od['hotel_room_connecting_room_number'] = hotel_room_connecting_room_number
#        self.od['hotel_room_connecting_room_number_2'] = hotel_room_connecting_room_number_2
#        self.od['hotel_room_bed_code'] = hotel_room_bed_code
#        self.od['user_id'] = user_id
#        self.od['party_members'] = party_members
#        self.od['town_city'] = town_city
#        self.od['state_province'] = state_province
#        self.od['international_country'] = international_country
#        self.od['how_many_trips'] = how_many_trips
#        self.od['ip_address'] = ip_address
#        
#        
#        #self.od = od
#        
        
    def compute(self, room_data, age_categories):
        
           
        """Perform any / all metadata computations
           Rebecca: We have to receive the header information from the original data file.
           We also need to add to that header data in SurveyData. """
       
        #roomData = RoomsData.RoomsData(project_globals.HOTEL_ROOM_DATA_FILE)
        
        #Party Room Computation

        #self.od["view"] = roomData.lookUpByHotelAndNumber(str(self.od["hotel_name"]), str(self.od["hotel_room_number"]))

        """How do we change this to work with header class?
        Need lots of help"""
        # Pass the party string to the Group class for dissection
        print(self.od["party_members"])
        group = Group.Group(str(self.od["party_members"]))

        self.__dict[PARTY_SIZE] = group.getPartySize()


        # TODO: update like this


        
        #Party Group Compuatation 
        self.od["party_size"] = group.getPartySize()
        #print(self.od["party_size"])
        self.od["num_males"] = group.getNumMales()
        self.od["num_females"] = group.getNumFemales()
        self.od["ages"] = group.getAges()
        self.od["age_categories"] = age_categories.getFrequencyCount(self.od["ages"])
        self.od["male_ages"] = group.getAgesMale()
        self.od["female_ages"] = group.getAgesFemale()
        self.od["male_age_categories"] = age_categories.getFrequencyCountMale(self.od["male_ages"])
        self.od["female_age_categories"] = age_categories.getFrequencyCountFemale(self.od["female_ages"])
        
        # Timestamps of survey dates
        #self.__survey_timestamp =  SurveySubmittedTimestamp.SurveySubmittedTimestamp(str(self.od["survey_submitted_at"]))
        #self.od["trip_start_timestamp"] = Timestamp.Timestamp(str(self.od["trip_start_date"]))
        #self.od["trip_end_timestamp"] =   Timestamp.Timestamp(str(self.od["trip_finish_date"]))
        
        #add season
#        self.od["season"] = SeasonCalculator.calcSeason(self.od["trip_start_timestamp"])
        

    def get_survey_id(self):
        return self.od['survey_id']

    def get_survey_submitted_at(self):
        return self.od['survey_submitted_at']

    def get_trip_start_date(self):
        return self.od['trip_start_date']

    def get_trip_finish_date(self):
        return self.od['trip_finish_date']

    def get_hotel_name(self):
        return self.od['hotel_name']

    def get_hotel_code(self):
        return self.od['hotel_code']

    def get_hotel_trip_other_name(self):
        return self.od['hotel_trip_other_name']

    def get_hotel_any_other(self):
        return self.od['hotel_any_other']

    def get_hotel_ritz_carlton(self):
        return self.od['hotel_ritz_carlton']

    def get_hotel_super_eight(self):
        return self.od['hotel_super_eight']

    def get_hotel_embassy_suites(self):
        return self.od['hotel_embassy_suites']

    def get_hotel_days_inn(self):
        return self.od['hotel_days_inn']

    def get_hotel_hampton_inn(self):
        return self.od['hotel_hampton_inn']

    def get_hotel_quality_inn(self):
        return self.od['hotel_quality_inn']

    def get_hotel_marriott(self):
        return self.od['hotel_marriott']

    def get_hotel_holiday_inn(self):
        return self.od['hotel_holiday_inn']

    def get_hotel_omni(self):
        return self.od['hotel_omni']

    def get_hotel_hilton(self):
        return self.od['hotel_hilton']

    def get_hotel_millenium(self):
        return self.od['hotel_millenium']

    def get_hotel_radisson(self):
        return self.od['hotel_radisson']

    def get_hotel_hyatt(self):
        return self.od['hotel_hyatt']

    def get_hotel_fairfield_inn(self):
        return self.od['hotel_fairfield_inn']

    def get_hotel_ramada_inn(self):
        return self.od['hotel_ramada_inn']

    def get_hotel_drury_inn(self):
        return self.od['hotel_drury_inn']

    def get_hotel_four_seasons(self):
        return self.od['hotel_four_seasons']

    def get_hotel_best_western(self):
        return self.od['hotel_best_western']

    def get_hotel_past_other_name(self):
        return self.od['hotel_past_other_name']
    
    def get_hotel_selection_cost(self):
        return self.od['hotel_selection_cost']

    def get_hotel_selection_bar(self):
        return self.od['hotel_selection_bar']

    def get_hotel_selection_distance_to_parks(self):
        return self.od['hotel_selection_distance_to_parks']

    def get_hotel_selection_in_room_dining(self):
        return self.od['hotel_selection_in_room_dining']

    def get_hotel_selection_food_court(self):
        return self.od['hotel_selection_food_court']

    def get_hotel_selection_sit_down_dining(self):
        return self.od['hotel_selection_sit_down_dining']

    def get_hotel_selection_fine_dining(self):
        return self.od['hotel_selection_fine_dining']

    def get_hotel_selection_parks_shuttle(self):
        return self.od['hotel_selection_parks_shuttle']

    def get_hotel_selection_airport_shuttle(self):
        return self.od['hotel_selection_airport_shuttle']

    def get_hotel_selection_in_room_kitchen(self):
        return self.od['hotel_selection_in_room_kitchen']

    def get_hotel_selection_room_size(self):
        return self.od['hotel_selection_room_size']

    def get_hotel_selection_multiple_bedroom_suites(self):
        return self.od['hotel_selection_multiple_bedroom_suites']

    def get_hotel_selection_spa_fitness_center(self):
        return self.od['hotel_selection_spa_fitness_center']

    def get_hotel_selection_pool(self):
        return self.od['hotel_selection_pool']

    def get_hotel_selection_theme(self):
        return self.od['hotel_selection_theme']

    def get_hotel_selection_kids_activities(self):
        return self.od['hotel_selection_kids_activities']

    def get_hotel_selection_location_on_property(self):
        return self.od['hotel_selection_location_on_property']

    def get_hotel_selection_other_string(self):
        return self.od['hotel_selection_other_string']

    def get_hotel_selection_other_rating(self):
        return self.od['hotel_selection_other_rating']

    def get_hotel_satisfied_room_cleanliness(self):
        return self.od['hotel_satisfied_room_cleanliness']

    def get_hotel_satisfied_room_size(self):
        return self.od['hotel_satisfied_room_size']

    def get_hotel_satisfied_room_quietness(self):
        return self.od['hotel_satisfied_room_quietness']

    def get_hotel_satisfied_beds_pillows(self):
        return self.od['hotel_satisfied_beds_pillows']

    def get_hotel_satisfied_pool_size(self):
        return self.od['hotel_satisfied_pool_size']

    def get_hotel_satisfied_pool_crowds(self):
        return self.od['hotel_satisfied_pool_crowds']

    def get_hotel_satisfied_pool_cleanliness(self):
        return self.od['hotel_satisfied_pool_cleanliness']

    def get_hotel_satisfied_parks_shuttle(self):
        return self.od['hotel_satisfied_parks_shuttle']

    def get_hotel_satisfied_airport_shuttle(self):
        return self.od['hotel_satisfied_airport_shuttle']

    def get_hotel_satisfied_check_in_out_process(self):
        return self.od['hotel_satisfied_check_in_out_process']

    def get_hotel_satisfied_staff(self):
        return self.od['hotel_satisfied_staff']

    def get_hotel_satisfied_recreation_amenities(self):
        return self.od['hotel_satisfied_recreation_amenities']

    def get_hotel_satisfied_food_court_overall(self):
        return self.od['hotel_satisfied_food_court_overall']

    def get_hotel_satisfied_food_court_value(self):
        return self.od['hotel_satisfied_food_court_value']

    def get_hotel_satisfied_find_your_way_around(self):
        return self.od['hotel_satisfied_find_your_way_around']

    def get_hotel_satisfied_child_services(self):
        return self.od['hotel_satisfied_child_services']

    def get_hotel_satisfied_sit_down_dining(self):
        return self.od['hotel_satisfied_sit_down_dining']

    def get_hotel_satisfied_other_string(self):
        return self.od['hotel_satisfied_other_string']

    def get_hotel_satisfied_other_rating(self):
        return self.od['hotel_satisfied_other_rating']

    def get_hotel_satisfaction_code(self):
        return self.od['hotel_satisfaction_code']

    def get_hotel_stay_again(self):
        return self.od['hotel_stay_again']

    def get_hotel_recommendation_code(self):
        return self.od['hotel_recommendation_code']

    def get_hotel_room_number(self):
        return self.od['hotel_room_number']

    def get_hotel_room_connecting(self):
        return self.od['hotel_room_connecting']

    def get_hotel_room_connecting_room_number(self):
        return self.od['hotel_room_connecting_room_number']

    def get_hotel_room_bed_code(self):
        return self.od['hotel_room_bed_code']

    def get_user_id(self):
        return self.od['user_id']

    def get_party_members(self):
        return self.od['party_members']

    def get_hometown(self):
        return self.od['hometown']

    def get_how_many_trips(self):
        return self.od['how_many_trips']

    def get_ip_address(self):
        return self.od['ip_address']

    def buildList(self):
        resultList = []
        for headerKeyItem in self.__headerSurvey.getHeader():
            if value != -1:
                resultList.append(str(self.__dict[headerKeyItem])            
        return resultList
    
#    def buildHeader(self):
#        headerList = []
#        for key in self.od:
#            headerList.append(key)
#        return headerList
    
                          
#    def writeCSV(self):
#        list = self.buildList()
#        L = [str(item) for item in list]
#        s = ","
#        return s.join(L)

    def writeCSV(self):
        list = self.buildList()
        L = [str(item) for item in list]
        strList = ', '.join(L)
        strList = strList.replace('\'', '')
        strList = strList.replace('\"', '')
        strList = strList.replace('[', '')
        strList = strList.replace(']', '')
        return strList
    
    
    
#    def writeCSVHeader(self):
#        list = self.buildHeader()
#        L = [str(item) for item in list]
#        s = ","
#        return s.join(L)

            
def test():

    ## Defining an object from the class defined in original
    
    myUser = UserSurvey()
#    myUser.compute()
    myUser.buildList()
    myUser.buildHeader()
    

    """Functions that use object defined above and the get
    functions defined in User_Survey_Class to print values"""

    print(myUser.od)

    print(myUser.writeCSV())


if __name__ == "__main__":
    test()    

            

            
















        





















        










