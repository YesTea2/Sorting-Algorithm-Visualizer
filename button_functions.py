import main
import gui
import rectangles as rects
from message_system import DisplayMessage as msg

currentListToSort = []

def GrabCurrentListToSort(listToSort):
    global currentListToSort
    currentListToSort.clear()
    currentListToSort.append(listToSort)
    
def RunSelectionSort():
    """ Checks if the data is ready to be sorted using a selection sort
    """

    # If the data is already sorted, prompt the user, return
    if main.isDataSorted:
        msg("RESET DATA BEFORE SORTING")
        return
    # If the data is currently being sorted, prompt the user, return
    elif main.isCurrentlySortingData:
        main.msg("WAIT FOR CURRENT ACTION TO FINISH")
        return
    # Ready to run selection sort
    msg("RUNNING SELECTION SORT")
    # Run a selection sort on the current list inside the SortList object
    ##print(currentList.listToSort)
    currentListToSort[0].SelectSortList()

    
def RunBubbleSort():
    """ Checks if the data is ready to be sorted using a Bubble sort"""
    # If the data is already sorted, prompt the user, return
    if main.isDataSorted:
        msg("RESET DATA BEFORE SORTING")
        return
    # If the data is currently being sorted, prompt the user, return
    elif main.isCurrentlySortingData:
        msg("WAIT FOR CURRENT ACTION TO FINISH")
        return
    
    # Ready to run bubble sort
    msg("RUNNING BUBBLE SORT")
    # Run a bubble sort on the current list inside the SortList object
    currentListToSort[0].BubbleSortList()
    
def RunMergeSort():
    """ Checks if the data is ready to be sorted using a Merge Sort"""
    # If the data is already sorted, prompt the user, return
    if main.isDataSorted:
        msg("RESET DATA BEFORE SORTING")
        return
    # If the data is currently being sorted, prompt the user, return
    elif main.isCurrentlySortingData:
        msg("WAIT FOR CURRENT ACTION TO FINISH")
        return
    
    # Ready to run bubble sort
    msg("RUNNING MERGE SORT")
    # Run a bubble sort on the current list inside the SortList object
    currentListToSort[0].MergeSortList(currentListToSort[0].listToSort)


    
def ResetWithNewData():
    """ Resets the current rectangle data"""

    # If the data is currently being sorted, wait to reset
    if main.isCurrentlySortingData:
        msg("WAIT FOR CURRENT ACTION TO FINISH")
        return
    if not main.isDataSorted:
        msg("SORT DATA BEFORE RESETTING")
        return
    # The data will no longer be sorted once this runs, set to False
    main.isDataSorted = False
    # Clear the list holding the SortList object
    currentListToSort.clear()
    # Clear all the rectangles from the screen
    for rect in rects.currentRectanglesOnScreen:
        rect.frame.destroy()
    rects.currentRectanglesOnScreen.clear()
    # Create a new list of ints and a new SortList object
    main.CreateIntList(60, randomIntList)
    # Create new rectangles
    rects.CreateRectangleFrames()
    
    
def SearchForValue():
    """ This is ran when the user clicks to search for a chosen
    value, checking if they need to wait, sort data or if its ok to run
    a binary search on their value
    """
    # Data is being sorted, alert user, return
    if main.isCurrentlySortingData:
        msg("WAIT FOR CURRENT ACTION TO FINISH")
        return
    # Data is not sorted, alert user, return
    if not main.isDataSorted:
        msg("SORT DATA BEFORE SEARCH")
        return
    # Check that the input is valid
    try:
        xValue = int(gui.userInput.get())
    except ValueError:
        # Input not valid, alert user, return
        msg("Invalid Input")
        return
    # Made it past all checks, run the binary search
    msg("RUNNING BINARY SEARCH")
    # Running binary search after a 3 second delay, this gives time for the text message to be read before wiping with a new message
    gui.currentlyDisplayedMainFrame[0].after(100, lambda x=xValue, minV=0, maxV=(len(currentListToSort[0].listToSort)-1): BinarySearch(x, minV, maxV))