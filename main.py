""" search_gui.py - An application that runs a binary search along with multiple sorting algorithms

A user is presented with a GUI where they can sort a list of integers using different sorting methods including Bubble, Selection and Merge(Not implemented yet).
As well as search the organized data using a bubble sort to find an inputted value

Name: Joshua Owen
Class: CS162 Linn-Benton Community College
Date: 5/20/2024

"""

# Importing the customTkinter package that enhances tkinter
import customtkinter
import pytest
import random
import gui
import rectangles
import message_system
import data
import button_functions

# These hold information that is refrenced during runtime
randomIntList = []
currentListToSort =[]


# Bool toggles to check if there is currently data being sorted, and if the 
# data is already sorted (used for checking during binary search)
global isDataSorted, isCurrentlySortingData
isDataSorted = False
isCurrentlySortingData = False


    
def Main():
    """ The main logic that needs to run when the application is loaded, calls all the methods used for displaying the frames, gui elements
    and creates the rectangle data and integer list
    """
    # Creating a list of ints
    CreateIntList(60, randomIntList)
    # Creating the frames
    gui.CreateRootFrame()
    gui.CreateMainFrame()
    gui.CreateCenterFrame()
    gui.CreateMainButtonFrame()
    rectangles.GrabCurrentListToSort(currentListToSort[0])
    rectangles.CreateRectangleFrames(gui.currentlyDisplayedMainFrame[0], gui.currentCenterFrame[0])
    message_system.CreateMessageFrame(gui.currentlyDisplayedMainFrame[0])
    # Creating the buttons
    gui.CreateLeftSideMainButtonFrame()
    gui.CreateRightSideMainButtonFrame()
    # Running a loop that continues to draw the application to the screen until the user closes it
    button_functions.GrabCurrentListToSort(currentListToSort[0])
    gui.rootFrame[0].mainloop()
    


class SortList:
    # Initilizing a new SortList class object
    def __init__(self, listToSort):
        """ The SortList class contains methods for sorting
        lists using Bubble Sorting, Merge Sorting (not implemented currently), and Selection Sorting
        
        """
        self.listToSort = listToSort
        
    def SelectSortList(self, number=0):
        """ Runs one loop of a selection sort, recursive
        this method will continue to run itself until its counter has reached
        the length of the list its checking
        
            Arguments:
            int(number): This is used as the index count for its recursion
        """
        # Setting the bool toggles to global so they can be changed inside this method
        global isDataSorted, isCurrentlySortingData
        # Grabbing the list from this SortList object
        listForSorting = self.listToSort

        # We are currently sorting the data, toggle bool True
        isCurrentlySortingData = True
        
        # If the index number is greater or equal to the length of the list, the search is complete
        if number >= len(listForSorting) - 1:
            # The search is complete, recreate the rectangles without color highlight
            #UpdateRectangleFrames([0,0])
            #def PerformRainbow(textToDisplay, currentRectanglesOnScreen:list, buttonsOnScreen:list, labelsOnScreen:list, userInputButton:list, sendMessageLabel: list, mainFrame, index = 0):
            data.PerformRainbow("SELECTION SORT FINISHED!", rectangles.currentRectanglesOnScreen, gui.buttonsOnScreen, gui.labelsOnScreen, gui.userInputButton, message_system.messageLabel, gui.currentlyDisplayedMainFrame[0])
            # Reset the sorting data bool
            isCurrentlySortingData = False
            # The data is now sorted, set to True
            isDataSorted = True
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
        listForSorting[number], listForSorting[curMin] = listForSorting[curMin], listForSorting[number]
        
        highlight_values = [listForSorting[index] for index in highlight_indices]
        # Recreating the rectangles, and highlighting the current rectangles that had been swapped
        rectangles.GrabCurrentListToSort(currentListToSort[0])
        rectangles.UpdateRectangleFrames(highlight_values + highlight_indices)

        # Recursive loop, runs after 1/2 of a second, recalling this method
        gui.currentlyDisplayedMainFrame[0].after(150, lambda numToUse=(number+1):self.SelectSortList(numToUse))
    
    def BubbleSortList(self, currentIndex=0):
        """ Runs one loop of a Bubble Sort, recursive
        this method will continue to run itself until its counter has reached
        the length of the list its checking
        
        Arguments:
            int(currentIndex): The current loop index for the recursion
        """
        global isDataSorted, isCurrentlySortingData
        listForSorting = self.listToSort
        isCurrentlySortingData = True

        if currentIndex >= len(listForSorting) - 1:
            isDataSorted = True
            isCurrentlySortingData = False
            # Highlight the sorted list
            PerformRainbow("BUBBLE SORT FINISHED!")
            return  

        swapped = False

        for i in range(0, len(listForSorting) - currentIndex - 1):
            if listForSorting[i] > listForSorting[i + 1]:
                listForSorting[i], listForSorting[i + 1] = listForSorting[i + 1], listForSorting[i]
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
            # Highlight the values being compared
            rectangles.GrabCurrentListToSort(currentListToSort[0])
            rectangles.UpdateRectangleFrames(values + swappedIndices)
            # Schedule the next iteration after a delay
            currentlyDisplayedMainFrame[0].after(400, lambda: self.BubbleSortList(currentIndex))
        else:
            # If no swap occurred, directly proceed to the next iteration
            self.BubbleSortList(currentIndex + 1)


        
    def MergeSortList(self, array):
        """ Runs one loop of a merge sort, recursive

        Arguments:
        array (list): The list to be sorted.
        number (int): This is used as the index count for its recursion.
        """
        global isDataSorted, isCurrentlySortingData

        isCurrentlySortingData = True
            
        listForSorting = array.copy()

        print("Sorting:", listForSorting)
        
        if len(array) > 1:

            mid = len(array) // 2
            leftHalf = array[:mid]
            rightHalf = array[mid:]

        
            self.MergeSortList(leftHalf)
            self.MergeSortList(rightHalf)
            


            i = j = k = 0
            while i < len(leftHalf) and j < len(rightHalf):
                if leftHalf[i] <= rightHalf[j]:  
                    array[k] = leftHalf[i]
                    i += 1
                else:
                    array[k] = rightHalf[j]
                    j += 1
                k += 1
                

            while i < len(leftHalf):
                array[k] = leftHalf[i]
                i += 1
                k += 1

            while j < len(rightHalf):
                array[k] = rightHalf[j]
                j += 1
                k += 1
            
            

            print("Merged:", array)
           
        self.listToSort = array
        print("self" + str(self.listToSort))
        rectangles.GrabCurrentListToSort(currentListToSort[0])
        rectangles.UpdateRectangleFrames([0])
        isDataSorted = True
        isCurrentlySortingData = False


    

def CreateIntList(amountOfInts: int, listForInts: list):
    """ Creates a list of integers, starting at 10
    to the length of amountOfInts, then shuffles the list
    to have an unorganized list to work with
    
        Arguments:
            int(amountOfInts): The amount of integers to create
            list(listForInts): A list that the integers will be appended to
    """
    global currentListToSort
    # Clearing the list of ints, if there happens to be any stored information
    listForInts.clear()
    
    # Setting the loop to start at 10
    # 10 was used, to have the rectangles be tall enough to visualize 
    i = 10
    # While the index is less than the amount of ints
    while i < amountOfInts:
        # Append the index to the list of ints
        listForInts.append(i)
        # Increase the value of the index
        i+= 1

    # Shuffling the list of ints
    random.shuffle(listForInts)
    # Clearing the list that holds the current SortList object
    currentListToSort.clear()
    # Initilizing a new SortList object, passing in the created list of ints 
    listForSorting = SortList(listForInts)
    # Appending the newly created SortList object to the list for the current SortList object
    currentListToSort.append(listForSorting)
    print(currentListToSort[0].listToSort)
        

    
if __name__ == "__main__":
    Main()