# -*- coding: utf-8 -*-
import random
import project_globals
import Utilities

"""@author Rebecca Wilhelmi
   @version June 4, 2019
   Methods to take the raw hotel room data file and break it down in a usable
   format. 
   Converts the long string of info into a parsed list. 
   Parses the whole document. 
   Search the room view by hotel and room number. 
   Makes a list of rooms in a hotel with a certain view and randomly returns one."""

class RoomsData:

    def __parseHotelRoomData(self, string):
        """ @param takes in a string which is one line of the Hotel Room Data
        breaks up the line into the hotel name, room number, and view and adds
        commas between the elements
        @return a list with string hotel name, int room number, and string room view """
        roomData = string.split("\t")
        #print(roomData)
        return (roomData[0], int(roomData[1]), roomData[2]) 

    def __init__(self, filename):
        """ Opens the hotel room data file and reads it
        Read the first line (title line) and get rid of it
        Loops through all the lines of the file, parse the line
        using the parseHotelRoomData function and adds them to the listOfRooms
        @return a list of all the parsed rows from the raw room file """

        inFileObj = Utilities.safe_open(filename, "r")

        self.__listOfRooms = []

        # Read and ignore the header line
        firstline = inFileObj.readline()

        # Cycle through the file
        for string in inFileObj:
            #print (string)
            string = string.strip()
            string = string.replace('"', '')
            self.__listOfRooms.append(self.__parseHotelRoomData(string))
 
    def lookUpByHotelAndNumber(self, strHotel, roomNumber):
        """ @param listOfRooms: parsed list of room data
        @param strHotel: the hotel name you want to search for
        @param roomNumber: the room number you want to search for
        loops through the list to see if the hotel name and room number are what 
        you are searching for
        @return returns the view of the inputed hotel and room"""
        #print(listOfRooms)
        for(hotel, rmNum, view) in self.__listOfRooms:
            if hotel == strHotel and rmNum == roomNumber:
                return view

        return "Problem"
        
    def __roomsWithHotelAndView(self, strHotel, strView):
        """ @param listOfRooms: parsed list of room data
        @param strHotel: the hotel name you want to search for
        @param strView: the room view you want to search for
        Loops through all the rooms and if the hotel and view match the inputs
        if they match, adds the room number to a list
        @return returns a sublist of room numbers that match the desired hotel and view"""

        subListOfRooms = []
        for(hotel, rmNum, view) in self.__listOfRooms:
            if hotel == strHotel and view == strView:
                subListOfRooms.append(rmNum)

        #        print(subListOfRooms)
        return subListOfRooms
    
    def randomRoomWithHotelAndView (self, strHotel, strView):
        """@param takes in a sublist of room numbers that match the desired hotel and view
        @return randomly chooses one of the room numbers and returns it"""

        subListOfRooms = self.__roomsWithHotelAndView(strHotel, strView)

        #print(random.choice(subListOfRooms))
        return random.choice(subListOfRooms)



def test():
    room_data = RoomsData(project_globals.HOTEL_ROOM_DATA_FILE) 
    room = room_data.randomRoomWithHotelAndView("Disney's Polynesian Village Resort", "magic_kingdom")
    print(room)

    view = room_data.lookUpByHotelAndNumber("Bay Lake Tower at Disney's Contemporary Resort", 8025)
    print (view)
    assert view == "bay_lake", "Test 1"
    print("Test succeeded!")
    

if __name__ == "__main__":
    test()