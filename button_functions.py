""" button_functions.py - Module containing the logic related to the logic of the buttons

This module contains the information for for what happens when the user clicks any of the buttons
on the gui


This script pools from these custom modules:
    rectangles.py:
        A module that contains the logic related to displaying the data to the screen as rectangles
    message_system.py:
        A module that contains the logic for a message system used to display what is currently happening to the user
    gui.py:
        A module that contains the logic for the gui that is displayed to the user
    data.py:
        A module that contains the logic related to creating the data that is manipulated as well as a rainbow effect
        
"""

import main
import gui
import rectangles as rects
import data
from message_system import DisplayMessage as msg

currentListToSort = []

isDataSorted = False
isDataCurrentlyBeingSorted = False


def GrabDataBools(dataSorted: bool, currentlySorting: bool):
    """The current values for the bools related to isDataSorted
    and isCurrentlySortingData from the main module are passed in
    and set to bools inside this script

        Arguments:
            bool(dataSorted): The value of isDataSorted from the main.py module
            bool(currentlySorting): The value of the isCurrentlySortingData from the main.py module
    """
    global isDataSorted, isDataCurrentlyBeingSorted
    # Setting isDataSorted to the passed in value of dataSorted
    isDataSorted = dataSorted
    # Setting isDataCurrentlyBeingSorted to the passed in value of currentlySorting
    isDataCurrentlyBeingSorted = currentlySorting


def GrabCurrentListToSort(listToSort):
    """The current SortList object is passed in as an argument
    and placed in a list to refrence in
    the different functions of this module

        Arguments:
            SortList(curList): The current SortList object
    """
    global currentListToSort
    # Clearing out the list of any SortList objects
    currentListToSort.clear()
    # Appending the passed in SortList object to the list
    currentListToSort.append(listToSort)


def RunSelectionSort():
    """Checks if the data is ready to be sorted using a selection sort"""

    # If the data is already sorted, prompt the user, return
    if isDataSorted:
        msg("RESET DATA BEFORE SORTING")
        return
    # If the data is currently being sorted, prompt the user, return
    elif isDataCurrentlyBeingSorted:
        msg("WAIT FOR CURRENT ACTION TO FINISH")
        return
    # Ready to run selection sort
    msg("RUNNING SELECTION SORT")
    # Run a selection sort on the current list inside the SortList object
    ##print(currentList.listToSort)
    currentListToSort[0].SelectSortList()


def RunBubbleSort():
    """Checks if the data is ready to be sorted using a Bubble sort"""
    # If the data is already sorted, prompt the user, return
    if isDataSorted:
        msg("RESET DATA BEFORE SORTING")
        return
    # If the data is currently being sorted, prompt the user, return
    elif isDataCurrentlyBeingSorted:
        msg("WAIT FOR CURRENT ACTION TO FINISH")
        return

    # Ready to run bubble sort
    msg("RUNNING BUBBLE SORT")
    # Run a bubble sort on the current list inside the SortList object
    currentListToSort[0].BubbleSortList()


def RunMergeSort():
    """Checks if the data is ready to be sorted using a Merge Sort"""
    # If the data is already sorted, prompt the user, return
    if isDataSorted:
        msg("RESET DATA BEFORE SORTING")
        return
    # If the data is currently being sorted, prompt the user, return
    elif isDataCurrentlyBeingSorted:
        msg("WAIT FOR CURRENT ACTION TO FINISH")
        return

    # Ready to run bubble sort
    msg("RUNNING MERGE SORT")
    # Run a bubble sort on the current list inside the SortList object
    currentListToSort[0].MergeSortList(currentListToSort[0].listToSort)


def ResetWithNewData():
    """Resets the current rectangle data"""

    # If the data is currently being sorted, wait to reset
    if isDataCurrentlyBeingSorted:
        msg("WAIT FOR CURRENT ACTION TO FINISH")
        return
    if not isDataSorted:
        msg("SORT DATA BEFORE RESETTING")
        return
    # The data will no longer be sorted once this runs, set to False
    main.SetDataSortedBool(0)
    # Clear the list holding the SortList object
    currentListToSort.clear()
    # Clear all the rectangles from the screen
    for rect in rects.currentRectanglesOnScreen:
        rect.frame.destroy()
    rects.currentRectanglesOnScreen.clear()
    # Create a new list of ints and a new SortList object
    main.CreateIntList(60)
    # Create new rectangles
    rects.CreateRectangleFrames(
        gui.currentlyDisplayedMainFrame[0], gui.currentCenterFrame[0]
    )


def SearchForValue():
    """This is ran when the user clicks to search for a chosen
    value, checking if they need to wait, sort data or if its ok to run
    a binary search on their value
    """
    # Data is being sorted, alert user, return
    if isDataCurrentlyBeingSorted:
        msg("WAIT FOR CURRENT ACTION TO FINISH")
        return
    # Data is not sorted, alert user, return
    if not isDataSorted:
        msg("SORT DATA BEFORE SEARCH")
        return
    # Check that the input is valid
    try:
        xValue = int(gui.userInputButton[0].get())
    except ValueError:
        # Input not valid, alert user, return
        msg("Invalid Input")
        return
    # Made it past all checks, run the binary search
    msg("RUNNING BINARY SEARCH")
    # Running binary search after a 3 second delay, this gives time for the text message to be read before wiping with a new message
    gui.currentlyDisplayedMainFrame[0].after(
        100,
        lambda x=xValue, minV=0, maxV=(
            len(currentListToSort[0].listToSort) - 1
        ): data.BinarySearch(x, minV, maxV),
    )
