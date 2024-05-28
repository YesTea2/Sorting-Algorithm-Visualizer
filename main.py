""" main.py - An application that runs the main logic for an application that shows different sorting algorithms

A user is presented with a GUI where they can sort a list of integers using different sorting methods including Bubble, Selection and Merge.
As well as search the organized data using a bubble sort to find an inputted value

This script pools from these custom modules:
    data.py: 
        A module that contains the logic related to creating the data that is manipulated as well as a rainbow effect
    rectangles.py:
        A module that contains the logic related to displaying the data to the screen as rectangles
    button_functions.py:
        A module that contains the logic for all of the different buttons the user can interact with
    message_system.py:
        A module that contains the logic for a message system used to display what is currently happening to the user
    gui.py:
        A module that contains the logic for the gui that is displayed to the user
        

Name: Joshua Owen
Class: CS162 Linn-Benton Community College
Date: 5/27/2024

*** Notes ***

    While the merge sort option does work and will eventually display the data sorted properly, I was unable to find a solution to have it
    display each step without breaking how the merge sort operates, instead there is a print statement kept inside this function so it can be
    seen that is, in fact, running a merge sort. 
    
    The merge sort also presented a problem with not being able to find a good way to have a coniditon to check when its finished, once you click the merge sort
    DO NOT CLICK any other buttons until the GUI updates with the sorted data otherwise it will break the application.
    
    All of the other sorting options have fail safes to prevent the user from clicking anything while the sorting is happening, but the merge sort toggles the bools off
    the second its clicked instead of when its finished.

"""

# Importing packages
import customtkinter
import pytest
import random

# Importing custom modules
import gui
import rectangles
import message_system
import data
import button_functions

randomIntList = []
currentListToSort = []


# Bool toggles to check if there is currently data being sorted, and if the
# data is already sorted (used for checking during binary search)
isDataSorted = False
isCurrentlySortingData = False


def Main():
    """The main logic that needs to run when the application is loaded, calls all the methods used for displaying the frames, gui elements
    and creates the rectangle data and integer list
    """
    # Creating a list of ints, this also creates the current SortList object
    CreateIntList(60)
    # Creating the frames
    gui.CreateRootFrame()
    gui.CreateMainFrame()
    gui.CreateCenterFrame()
    gui.CreateMainButtonFrame()
    # Sending the current SortList object to the rectangles module
    rectangles.GrabCurrentListToSort(currentListToSort[0])
    # Creating the rectangles for the data
    rectangles.CreateRectangleFrames(
        gui.currentlyDisplayedMainFrame[0], gui.currentCenterFrame[0]
    )
    # Creating the frame that displays messages to the user
    message_system.CreateMessageFrame(gui.currentlyDisplayedMainFrame[0])
    # Creating the buttons
    gui.CreateLeftSideMainButtonFrame()
    gui.CreateRightSideMainButtonFrame()
    # Sending the current SortList object to the button_functions module
    button_functions.GrabCurrentListToSort(currentListToSort[0])
    # Running a loop that continues to draw the application to the screen until the user closes it
    gui.rootFrame[0].mainloop()


def SetDataSortedBool(trueOrFalse: int):
    """Sets the isDataSorted bool to true or false
    given the passed in integer value

        Arguments:
            int(trueOrFalse): If the int is 0, the bool is toggled false,
            any other number and its toggled true.
    """
    global isDataSorted

    # If the arg passed in is 0, set the bool to false
    if trueOrFalse == 0:
        isDataSorted = False
    # Else set the bool to True
    else:
        isDataSorted = True

    # Sending the updated bools to the button_function script, to update all of the button logic
    button_functions.GrabDataBools(isDataSorted, isCurrentlySortingData)


def SetCurrentlySortingDataBool(trueOrFalse: int):
    """Sets the isCurrentlySortingData bool to true or false
    given the passed in integer value.

        Arguments:
            int(trueOrFalse): If the int is 0, the bool is toggled false,
            any other number and its toggled true.
    """
    global isCurrentlySortingData

    # If the arg passed in is 0, set the bool to false
    if trueOrFalse == 0:
        isCurrentlySortingData = False
    # Else set the bool to True
    else:
        isCurrentlySortingData = True

    # Sending the updated bools to the button_function script, to update all of the button logic
    button_functions.GrabDataBools(isDataSorted, isCurrentlySortingData)


class SortList:
    # Initilizing a new SortList class object
    def __init__(self, listToSort):
        """The SortList class contains methods for sorting
        lists using Bubble Sorting, Merge Sorting (not implemented currently), and Selection Sorting

        """
        self.listToSort = listToSort

    def SelectSortList(self, number=0):
        """Runs one loop of a selection sort, recursive
        this method will continue to run itself until its counter has reached
        the length of the list its checking

            Arguments:
            int(number): This is used as the index count for its recursion
        """

        # Grabbing the list from this SortList object
        listForSorting = self.listToSort

        # Toggling the isCurrentlySortingData bool to True
        SetCurrentlySortingDataBool(1)

        # If the index number is greater or equal to the length of the list, the search is complete
        if number >= len(listForSorting) - 1:
            # The sorting is finished, display the data with a fun rainbow effect
            data.PerformRainbow(
                "SELECTION SORT FINISHED!",
                rectangles.currentRectanglesOnScreen,
                gui.buttonsOnScreen,
                gui.labelsOnScreen,
                gui.userInputButton,
                message_system.messageLabel,
                gui.currentlyDisplayedMainFrame[0],
            )
            # Toggling the isCurrentlySortingData bool to false
            SetCurrentlySortingDataBool(0)
            # Toggling the isDataSorted bool to True
            SetDataSortedBool(1)

            return

        # Setting the curMin to be the current index
        curMin = number
        # Checking the range of the list from the current index + 1, to the length of the list
        for i in range(number + 1, len(listForSorting)):
            # If the current index i, is less than the current list at the index of the curMin
            if listForSorting[i] < listForSorting[curMin]:
                # The current min is now i
                curMin = i

        # Store the indices of elements being compared or swapped
        highlight_indices = [number, curMin]

        # Swappping the values at the index of number, with the index of curMin, and the index of curMin with the index of number
        listForSorting[number], listForSorting[curMin] = (
            listForSorting[curMin],
            listForSorting[number],
        )

        highlight_values = [listForSorting[index] for index in highlight_indices]

        # Sending the updated sorted list to both the rectangles module and data module
        rectangles.GrabCurrentListToSort(currentListToSort[0])
        data.GrabCurrentListToSort(currentListToSort[0])
        # Recreating the rectangles, and highlighting the current rectangles that had been swapped
        rectangles.UpdateRectangleFrames(highlight_values + highlight_indices)

        # Recursive loop, runs after 1/2 of a second, recalling this method
        gui.currentlyDisplayedMainFrame[0].after(
            150, lambda numToUse=(number + 1): self.SelectSortList(numToUse)
        )

    def BubbleSortList(self, currentIndex=0):
        """Runs one loop of a Bubble Sort, recursive
        this method will continue to run itself until its counter has reached
        the length of the list its checking

        Arguments:
            int(currentIndex): The current loop index for the recursion
        """
        # Setting the current list to the liset of this object
        listForSorting = self.listToSort
        # Toggling the isCurrentlySorting bool to True
        SetCurrentlySortingDataBool(1)

        if currentIndex >= len(listForSorting) - 1:
            # Toggling the isDataSorted bool to True
            SetDataSortedBool(1)
            # Toggling the isCurrentlySorted bool to False
            SetCurrentlySortingDataBool(0)

            # Display that the bubble sort is finished with a fun rainbow effect
            data.PerformRainbow(
                "BUBBLE SORT FINISHED!",
                rectangles.currentRectanglesOnScreen,
                gui.buttonsOnScreen,
                gui.labelsOnScreen,
                gui.userInputButton,
                message_system.messageLabel,
                gui.currentlyDisplayedMainFrame[0],
            )
            return

        swapped = False

        for i in range(0, len(listForSorting) - currentIndex - 1):
            if listForSorting[i] > listForSorting[i + 1]:
                listForSorting[i], listForSorting[i + 1] = (
                    listForSorting[i + 1],
                    listForSorting[i],
                )
                swapped = True

        if swapped:
            # If there was a swap, schedule the visualization update
            self.UpdateBubbleSortVisual(listForSorting, currentIndex)
        else:
            # If no swap occurred, directly proceed to the next iteration
            self.BubbleSortList(currentIndex + 1)

    def UpdateBubbleSortVisual(self, listForSorting, currentIndex):
        """Schedule visualization update after a swap occurs"""
        swappedIndices = []
        for i in range(len(listForSorting) - currentIndex - 1):
            if listForSorting[i] > listForSorting[i + 1]:
                swappedIndices.append(i)
        if swappedIndices:
            # Get the values at swapped indices for visualization
            values = [listForSorting[i] for i in swappedIndices]

            # Sending the updated list to both the rectangles and data module
            rectangles.GrabCurrentListToSort(currentListToSort[0])
            data.GrabCurrentListToSort(currentListToSort[0])
            # Highlight the values being compared
            rectangles.UpdateRectangleFrames(values + swappedIndices)
            # Schedule the next iteration after a delay
            gui.currentlyDisplayedMainFrame[0].after(
                400, lambda: self.BubbleSortList(currentIndex)
            )
        else:
            # If no swap occurred, directly proceed to the next iteration
            self.BubbleSortList(currentIndex + 1)

    def MergeSortList(self, array):
        """Runs one loop of a merge sort, recursive

        Arguments:
            array (list): The list to be sorted.
            number (int): This is used as the index count for its recursion.
        """
        global isDataSorted, isCurrentlySortingData

        # Toggling the isCurrentlySortingData bool to True
        SetCurrentlySortingDataBool(1)

        # Making a copy of the passed in array
        listForSorting = array.copy()

        print("Sorting:", listForSorting)

        # If the current array from the arguments length is greater than 1
        if len(array) > 1:

            # Dividing the array into halves
            mid = len(array) // 2
            leftHalf = array[:mid]
            rightHalf = array[mid:]

            # Recursively calling MergeSortList on both halves
            self.MergeSortList(leftHalf)
            self.MergeSortList(rightHalf)

            # Merging the sorted halves
            i = j = k = 0
            while i < len(leftHalf) and j < len(rightHalf):
                if leftHalf[i] <= rightHalf[j]:
                    array[k] = leftHalf[i]
                    i += 1
                else:
                    array[k] = rightHalf[j]
                    j += 1
                k += 1

            # Adding remaining elements from leftHalf
            while i < len(leftHalf):
                array[k] = leftHalf[i]
                i += 1
                k += 1

            # Adding remaining elements from rightHalf
            while j < len(rightHalf):
                array[k] = rightHalf[j]
                j += 1
                k += 1

            # Printing the values in the current array to show its working
            print("Merged:", array)

        # Setting the sorted list to self.listToSort
        self.listToSort = array
        # Printing the current value of the list to show its working
        print("self" + str(self.listToSort))
        # Sending the updated list to both the rectangles and data module
        rectangles.GrabCurrentListToSort(currentListToSort[0])
        data.GrabCurrentListToSort(currentListToSort[0])
        # Updating the rectangle data
        rectangles.UpdateRectangleFrames([0])
        # Toggling the isDataSorted bool to True
        SetDataSortedBool(1)
        # Toggling the isCurrentlySortingData bool to False
        SetCurrentlySortingDataBool(0)


def CreateIntList(amountOfInts: int):
    """Creates a list of integers, starting at 10
    to the length of amountOfInts, then shuffles the list
    to have an unorganized list to work with

        Arguments:
            int(amountOfInts): The amount of integers to create
            list(listForInts): A list that the integers will be appended to
    """
    global currentListToSort

    listForInts = []

    # Setting the loop to start at 10
    # 10 was used, to have the rectangles be tall enough to visualize
    i = 10
    # While the index is less than the amount of ints
    while i < amountOfInts:
        # Append the index to the list of ints
        listForInts.append(i)
        # Increase the value of the index
        i += 1

    # Shuffling the list of ints
    random.shuffle(listForInts)
    # Clearing the list that holds the current SortList object
    currentListToSort.clear()
    # Initilizing a new SortList object, passing in the created list of ints
    listForSorting = SortList(listForInts)
    # Appending the newly created SortList object to the list for the current SortList object
    currentListToSort.append(listForSorting)
    button_functions.GrabCurrentListToSort(listForSorting)
    rectangles.GrabCurrentListToSort(listForSorting)
    data.GrabCurrentListToSort(currentListToSort[0])
    print(currentListToSort[0].listToSort)


if __name__ == "__main__":
    Main()
