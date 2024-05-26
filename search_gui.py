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
# Importing random
import random


# Creating empty lists that will hold each of the different frames that are
# used interchangably in methods
rootFrame = []
currentlyDisplayedMainFrame = []
currentlyDisplayedMainButtonFrame = []
currentlyDisplayedSortButtonLeftFrame = []
currentlyDisplayedSortButtonRightFrame = []
currentlyDisplayedSearchButtonFrame = []
currentlyDisplayedLeftSideMainButtonFrame = []
currentlyDisplayedRightSideMainButtonFrame = []
currentCenterFrame = []

# Creating an empty list to hold all of the buttons
buttonOnScreen = []

# Creating an empty list to hold the rectangle class objects
currentRectanglesOnScreen = []

# These hold information that is refrenced during runtime
randomIntList = []
userInputButton = []
errorMessage= []
currentListToSort =[]

# Bool toggles to check if there is currently data being sorted, and if the 
# data is already sorted (used for checking during binary search)
isDataSorted = False
isCurrentlySortingData = False


    
def Main():
    """ The main logic that needs to run when the application is loaded, calls all the methods used for displaying the frames, gui elements
    and creates the rectangle data and integer list
    """
    # Creating a list of ints
    CreateIntList(60, randomIntList)
    # Creating the frames
    CreateRootFrame()
    CreateMainFrame()
    CreateCenterFrame()
    CreateMainButtonFrame()
    CreateRectangleFrames()
    CreateErrorFrame()
    # Creating the buttons
    CreateLeftSideMainButtonFrame()
    CreateRightSideMainButtonFrame()
    # Running a loop that continues to draw the application to the screen until the user closes it
    rootFrame[0].mainloop()




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
            CreateRectangleFramesWithoutDelayAndHighlight(0,0)
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


        # Swappping the values at the index of number, with the index of curMin, and the index of curMin with the index of number
        listForSorting[number], listForSorting[curMin] = listForSorting[curMin], listForSorting[number]
        

        # Recreating the rectangles, and highlighting the current rectangles that had been swapped
        CreateRectangleFramesWithoutDelayAndHighlight(listForSorting[number],listForSorting[curMin])

        # Recursive loop, runs after 1/2 of a second, recalling this method
        currentlyDisplayedMainFrame[0].after(500, lambda numToUse=(number+1):self.SelectSortList(numToUse))
    
    def BubbleSortList(self, current_index=0):
        """ Runs one loop of a Bubble Sort, recursive
        this method will continue to run itself until its counter has reached
        the length of the list its checking
        
            Arguments:
                int(current_index): The current loop index for the recursion
        """
        # Setting the bool flags global that will be toggled
        global isDataSorted, isCurrentlySortingData
        # Grabbing the list from this SortList object
        listForSorting = self.listToSort
        # We are currently sorting data, toggle True
        isCurrentlySortingData = True

        # If our index is already the length of the list, we are finished
        if current_index >= len(listForSorting) - 1:
            # Reset the rectangles to not hightlight a color
            CreateRectangleFramesWithoutDelayAndHighlight(0, 0)
            # The data is sorted, toggle True
            isDataSorted = True
            # We are not longer sorting data, toggle False
            isCurrentlySortingData = False
            return  
        
        # Bool toggle used to only update the visual if there is a swap in values
        swapped = False
        tempIndex = None

        # For the range of the list, minus the index -1
        for i in range(0, len(listForSorting) - current_index - 1):
            # If the index i of the list is greater than the next element in the list
            if listForSorting[i] > listForSorting[i + 1]:
                # Swap the elements
                listForSorting[i], listForSorting[i + 1] = listForSorting[i + 1], listForSorting[i]
                # We made a swap
                tempIndex = i
                swapped = True
        
        # Update visualization if there were any swaps in this pass
        if swapped:
            # Grabbing the numbers that swapped
            curNumSwapOne = listForSorting[tempIndex]
            curNumSwapTwo = listForSorting[tempIndex + 1]
            # Sending the numbers to be displayed on the rectangles
            CreateRectangleFramesWithoutDelayAndHighlight(curNumSwapOne, curNumSwapTwo)

        # Running another loop of this method, increasing the index number
        currentlyDisplayedMainFrame[0].after(500, lambda curIndex=(current_index + 1):self.BubbleSortList(curIndex))
        
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
            left_half = array[:mid]
            right_half = array[mid:]

            self.listToSort = array
            self.MergeSortList(left_half)
            self.MergeSortList(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:  
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1
            CreateRectangleFramesWithoutDelayAndHighlight(j,k)

            print("Merged:", array)
        
        self.listToSort = array
        print("self" + str(self.listToSort))
        CreateRectangleFramesWithoutDelayAndHighlight(0,0)
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
        
        
class RectangleWithValue:
    """ The RectangleWithValue class, is used when creating the frames that
    will be used as the visual for the data, this holds a frame object, its current value and its label
    """
    def __init__(self, frame, value, label):
        self.frame = frame
        self.value = value
        self.label = label
        
            
def CreateRectangleFramesWithoutDelayAndHighlight(valueOneToCheck, valueTwoToCheck):
    """ This class is used for refreshing the data rectangles on the screen, two values are passed in
    and checked against, if the values are found inside of the rectangles, it highlights those rectangles.
    
    There is a second method very similer to this one, but has a delay when creating the information, its used
    at the initial start of the application to create a smooth effect of spawning in the data
    
        Arguments:
            int(valueOneToCheck): the first value to check against
            int(valueTwoToCheck): the second value to check against
    """
    
    # For any rectangles already on the screen, destroy them
    for rect in currentRectanglesOnScreen:
        rect.frame.destroy()
    # clear the list of rectangles
    currentRectanglesOnScreen.clear()
    
    # For the amount of numbers in the list to sort
    for i in currentListToSort[0].listToSort:
        # Create a new frame
        rectFrame = customtkinter.CTkFrame(master=currentCenterFrame[0], height=(i * 3), width=23, border_color="#52796F", border_width=1, fg_color="#84A98C")
        # If the index equals the valueOneToCheck, highlight
        if valueOneToCheck == i:
            rectFrame.configure(border_color="#52796F", fg_color="#28392c")  # Highlight the first value
        # If the index equals the valueTwoToCheck, highlight
        elif valueTwoToCheck == i:
            rectFrame.configure(border_color="#52796F", fg_color="#47664e")  # Highlight the second value
        # Packing the frame to thes creen
        rectFrame.pack(side="left", padx=2, expand=False)
        # Creating a label that has the vaue of the index for the text
        rectLabel = customtkinter.CTkLabel(master=rectFrame, text=str(i), text_color="white", font=("Great Vibes", 15))
        # Packing the label
        rectLabel.pack(padx=2, pady=2, expand=False, side="bottom")
        # Setting both the frame and label to not propogate, this way they ignore padding of other rectangles
        rectFrame.pack_propagate(0)
        rectLabel.pack_propagate(0)
        # Creating a new RectangleWithValue object, passing in the frame, index value and the label  
        rectangleWithValue = RectangleWithValue(rectFrame, i, rectLabel)
        # Appending this new object to the list of rectangles on the screen
        currentRectanglesOnScreen.append(rectangleWithValue)

   
def CreateRectangleFrames(i=0):
    """ This is the same method as the CreateRectanglesFramesWithoutDelayAndHighlight, only
    its recursive, creating a delay after each rectangle to make a smooth effect at runtime. There is also
    no highlighting of the values
    """

    # Creating a new frame and label
    rectFrame = customtkinter.CTkFrame(master=currentCenterFrame[0], height=(currentListToSort[0].listToSort[i]*3), width=23, border_color="#52796F", border_width=1, fg_color="#84A98C")
    rectLabel = customtkinter.CTkLabel(master=rectFrame, text=str(currentListToSort[0].listToSort[i]), text_color="white", font=("Great Vibes", 15))
    # If the index is currently 0, setting padding to not ram the first rectangle against the frame
    if i == 0:
        rectFrame.pack(side="left", padx=(10,2), expand=False)
        rectFrame.pack_propagate(0)
    # Else we are past the first rectangle, only use 2 for padding on the x axis
    else:
        rectFrame.pack(side="left", padx=2, expand=False)
        rectFrame.pack_propagate(0)
    # Packing the label 
    rectLabel.pack(padx=2, pady=2, expand=False, side="bottom")
    rectLabel.pack_propagate(0)  
    # Creating a new RectangleWithValue object, passing in the rectFrame, the value in the list, and the label
    rectangleWithValue = RectangleWithValue(rectFrame, currentListToSort[0].listToSort[i], rectLabel)
    # Appending the newly created RectangleWithValue object to the list of rectangle objects
    currentRectanglesOnScreen.append(rectangleWithValue)
    
    # Checking if we are finished creating rectangles, and if not, rerun this method
    if i+1 < len(currentListToSort[0].listToSort):
        rectFrame.after(20, lambda index=(i+1):CreateRectangleFrames(index))
        


       



def CreateRootFrame():
    """" Creates the root frame that all other frames are children of."""

    # Initilizing a new instance of cTK
    frame = customtkinter.CTk()
    # Setting the x and y values for the entire application window
    frame.geometry("1366x768")
    # Giving the window a title
    frame.title("Search")
    # Setting the window to not allow resizing
    frame.resizable(False, False)
    # Adding the newly created frame to the rootFrame list, this is for easy refrence between methods.
    rootFrame.append(frame)
    

def CreateMainFrame():
    """ Creates the main sub frame of root, all frames inheret from this frame"""

    # Initilizing a new frame, setting its parent to the root frame
    mainFrame = customtkinter.CTkFrame(master=rootFrame[0])

    # Packing the frame to the screen, setting it to fill the length and width of the window and to expand to max value
    mainFrame.pack(fill="both", expand=True)

    # Setting the color for the entire window
    mainFrame.configure(fg_color="black")

    # On the off chance there is already a main frame held inside the list for the main frame, clear it.
    currentlyDisplayedMainFrame.clear()

    # Appending the newly created main frame to the list of main frame
    currentlyDisplayedMainFrame.append(mainFrame)

def CreateCenterFrame():
    """ Creates the centeral frame"""
    # Creating the center frame, setting its master to the mainFrame
    centerFrame = customtkinter.CTkFrame(master=currentlyDisplayedMainFrame[0], width= 1340, height=450, fg_color="#354F52",border_color="#84A98C",border_width=2)
    # Packing to the screen
    centerFrame.pack(expand=True, pady= 75, fill="both")
    # Adding it to its list to carry over into other methods
    currentCenterFrame.append(centerFrame)
    
def CreateMainButtonFrame():
    """ Creates the frame that the bottom buttons will nest inside of"""

    # Initilizing a new frame and setting its parent to the main frame
    mainButtonFrame = customtkinter.CTkFrame(master=currentlyDisplayedMainFrame[0])

    # Setting it to fill its width and height to the parent frame
    mainButtonFrame.pack(pady=40, padx=0,expand=False)

    # Setting the background color of the frame ( this could also be set as transparent as
    # its the same color as the parent frame, but its the same amount of memory either way).
    mainButtonFrame.configure(fg_color="transparent")

    # Clearing the list of main button frames, on the off chance that one is already held.
    currentlyDisplayedMainButtonFrame.clear()
    # Appending the frame to the list of main button frames.
    currentlyDisplayedMainButtonFrame.append(mainButtonFrame)
    
    



def SearchForValue():
    """ This is ran when the user clicks to search for a chosen
    value, checking if they need to wait, sort data or if its ok to run
    a binary search on their value
    """
    # Data is being sorted, alert user, return
    if isCurrentlySortingData:
        DisplayErrorInput("WAIT FOR CURRENT ACTION TO FINISH")
        return
    # Data is not sorted, alert user, return
    if not isDataSorted:
        DisplayErrorInput("SORT DATA BEFORE SEARCH")
        return
    # Check that the input is valid
    try:
        xValue = int(userInputButton[0].get())
    except ValueError:
        # Input not valid, alert user, return
        DisplayErrorInput("Invalid Input")
        return
    # Made it past all checks, run the binary search
    DisplayErrorInput("RUNNING BINARY SEARCH")
    # Running binary search after a 3 second delay, this gives time for the text message to be read before wiping with a new message
    currentCenterFrame[0].after(3000, lambda x=xValue, minV=0, maxV=(len(currentListToSort[0].listToSort)-1): BinarySearch(x, minV, maxV))

def BinarySearch(xValue, minValue, maxValue):
    """ Performs a binary search, using the users inputted value as the xValue
    and continusly checks against the min and max value until found
    """
    # If the max value is greater than the minimum value, this has ran 
    # enough times to have found that the number inputted is not included in this list
    if maxValue < minValue:
        # Value not found
        DisplayErrorInput("Value not found")
        return

    # Creating a midpoint value,  between minValue and maxValue.
    midValue = minValue + (maxValue - minValue) // 2

    # If the middle value inside the list is equal to the users inputted value, the search found their value
    if currentListToSort[0].listToSort[midValue] == xValue:
        # Value found!
        DisplayErrorInput(f"Value {xValue}, found!")
        # Refresh the rectangles, highlight the value
        CreateRectangleFramesWithoutDelayAndHighlight(xValue, 0)
    # If the value in the middle is greater than the users inputted value
    elif currentListToSort[0].listToSort[midValue] > xValue:
        # Highlight the current minValue and maxValue on the rectangles
        CreateRectangleFramesWithoutDelayAndHighlight(minValue, maxValue)
        DisplayErrorInput(f"CHECKING MIN={minValue}, MID={midValue} MAX={maxValue}")
        # Rerun this search after 3 seconds, passing in the same x value, the same minValue but setting the new max value to be the middle value - 1
        currentCenterFrame[0].after(3000, lambda x=xValue, minV=minValue, maxV=(midValue - 1): BinarySearch(x, minV, maxV))
    # Else if the middle value is less than the inputted value
    else:
        # Highlight the current minValue and maxValue on the rectangles
        CreateRectangleFramesWithoutDelayAndHighlight(minValue, maxValue)
        DisplayErrorInput(f"CHECKING MIN={minValue}, MID={midValue}, MAX={maxValue}")
        # Rerun this search after 3 seconds, passing in the same x value, changing the minValue to be the middle value + 1, and using the same maxValue
        currentCenterFrame[0].after(3000, lambda x=xValue, minV=(midValue + 1), maxV=maxValue: BinarySearch(x, minV, maxV))




            
def RunSelectionSort():
    """ Checks if the data is ready to be sorted using a selection sort
    """
    # If the data is already sorted, prompt the user, return
    if isDataSorted:
        DisplayErrorInput("RESET DATA BEFORE SORTING")
        return
    # If the data is currently being sorted, prompt the user, return
    elif isCurrentlySortingData:
        DisplayErrorInput("WAIT FOR CURRENT ACTION TO FINISH")
        return
    # Ready to run selection sort
    DisplayErrorInput("RUNNING SELECTION SORT")
    # Run a selection sort on the current list inside the SortList object
    currentListToSort[0].SelectSortList()

    
def RunBubbleSort():
    """ Checks if the data is ready to be sorted using a Bubble sort"""
    # If the data is already sorted, prompt the user, return
    if isDataSorted:
        DisplayErrorInput("RESET DATA BEFORE SORTING")
        return
    # If the data is currently being sorted, prompt the user, return
    elif isCurrentlySortingData:
        DisplayErrorInput("WAIT FOR CURRENT ACTION TO FINISH")
        return
    
    # Ready to run bubble sort
    DisplayErrorInput("RUNNING BUBBLE SORT")
    # Run a bubble sort on the current list inside the SortList object
    currentListToSort[0].BubbleSortList()
    
def RunMergeSort():
    """ Checks if the data is ready to be sorted using a Merge Sort"""
    # If the data is already sorted, prompt the user, return
    if isDataSorted:
        DisplayErrorInput("RESET DATA BEFORE SORTING")
        return
    # If the data is currently being sorted, prompt the user, return
    elif isCurrentlySortingData:
        DisplayErrorInput("WAIT FOR CURRENT ACTION TO FINISH")
        return
    
    # Ready to run bubble sort
    DisplayErrorInput("RUNNING MERGE SORT")
    # Run a bubble sort on the current list inside the SortList object
    currentListToSort[0].MergeSortList(currentListToSort[0].listToSort)


    
def ResetWithNewData():
    """ Resets the current rectangle data"""
    global isDataSorted
    # If the data is currently being sorted, wait to reset
    if isCurrentlySortingData == True:
        DisplayErrorInput("WAIT FOR CURRENT ACTION TO FINISH")
        return
    # The data will no longer be sorted once this runs, set to False
    isDataSorted = False
    # Clear the list holding the SortList object
    currentListToSort.clear()
    # Clear all the rectangles from the screen
    for rect in currentRectanglesOnScreen:
        rect.frame.destroy()
    currentRectanglesOnScreen.clear()
    # Create a new list of ints and a new SortList object
    CreateIntList(60, randomIntList)
    # Create new rectangles
    CreateRectangleFrames()
        

def CreateErrorFrame():
    """ Creates the label used for displaying the current action to the user """
    # Creating a new label, its text is blank
    errorInput = customtkinter.CTkLabel(master=currentlyDisplayedMainFrame[0], text="", text_color="white", font=("Great Vibes", 30))
    # Packing it to the screen
    errorInput.pack(side="top", pady=(0,25), expand=False)
    # Adding it to its list
    errorMessage.append(errorInput)
    
def DisplayErrorInput(textToDisplay:str):
    """ Updates the text prompt with the given text and displays it to the screen
        Arguments:
            str(textToDisplay): The string for the text to display to the user
    """
    # Setting the text on the label to the passed in string
    errorMessage[0].configure(text=textToDisplay)
    # Updating the label
    errorMessage[0].update_idletasks()
    # After a little more than 2 seconds, resetting the label to be blank
    currentlyDisplayedMainFrame[0].after(2200, ClearErrorInput)

def ClearErrorInput():
    """ Erases any messages on the text prompt """
    # Setting the text on the label to be blank
    errorMessage[0].configure(text="")
    # Updating the label
    errorMessage[0].update_idletasks()


def CreateLeftSideMainButtonFrame():
    """ Creates the frame that holds the right side buttons """
    # Creating the frame
    frame = customtkinter.CTkFrame(master=currentlyDisplayedMainButtonFrame[0], width = 250, fg_color="transparent")
    # Packing to the screen
    frame.pack(side="left", padx=(200,0))
    # Creating a label to sit at the top of the frame
    label = customtkinter.CTkLabel(master=frame, text="DATA SORTING", text_color="white", font=("Great Vibes", 30))
    # Packing the label
    label.pack(side="top", pady=(0,20))
    # Appending the newly created frame to the list that holds it for refrence
    currentlyDisplayedLeftSideMainButtonFrame.append(frame)
    # Creating the frames that will nest inside this frame
    CreateSortButtonFrameLeft()
    CreateSortButtonFrameRight()

def CreateRightSideMainButtonFrame():
    """ Creates the frame that holds the left side buttons """
    
    # Creating the frame
    frame = customtkinter.CTkFrame(master=currentlyDisplayedMainButtonFrame[0], width=300, fg_color="transparent")
    # Packing to the screen
    frame.pack(side="right", padx=(200,200))
    # Creating a label to sit at the top of the frame
    label = customtkinter.CTkLabel(master=frame, text="DATA SEARCHING", text_color="white", font=("Great Vibes", 30))
    # Packing the label
    label.pack(side="top", pady=(0,20))
    # Appending the newly created frame to the list that holds it for refrence
    currentlyDisplayedRightSideMainButtonFrame.append(frame)
    # Creating the frame that nest inside this frame
    CreateSearchButtonFrame()

def CreateSortButtonFrameLeft():
    """ Creates the left side frame that nests inside the left side button frame, this
    seems redudent, but its the only way to have the buttons sit how I wanted
    """
    # Creating the frame
    sortFrame = customtkinter.CTkFrame(master=currentlyDisplayedLeftSideMainButtonFrame[0], width= 200, fg_color="transparent")
    # Packing the frame
    sortFrame.pack(side="left", padx=(0))
    # Adding the frame to the list that holds it for refrence
    currentlyDisplayedSortButtonLeftFrame.append(sortFrame)
    # Creating the buttons that nest inside this frame
    CreateLeftSortButtons()

def CreateSortButtonFrameRight():
    """ Creates the right side frame that nests inside the left side button frame, this
    seems redudent, but its the only way to have the buttons sit how I wanted
    """
    # Creating the frame
    sortFrame = customtkinter.CTkFrame(master=currentlyDisplayedLeftSideMainButtonFrame[0], width=200, fg_color="transparent")
    # Packing the frame
    sortFrame.pack(side="left", padx=10)
    # Adding the frame to the list that holds it for refrence
    currentlyDisplayedSortButtonRightFrame.append(sortFrame)
    # Creating the buttons that nest inside this frame
    CreateRightSortButtons()


def CreateSearchButtonFrame():
    """ Creates the frame that the right side buttons will nest inside """
    # Create the frame
    searchFrame = customtkinter.CTkFrame(master=currentlyDisplayedRightSideMainButtonFrame[0], width= 600, fg_color="transparent")
    # Pack the frame
    searchFrame.pack(side="right", padx=20)
    # Append the frame to the list that is used for refrence
    currentlyDisplayedSearchButtonFrame.append(searchFrame)
    # Create the search buttons inside this frame
    CreateSearchButtons()
    

def CreateLeftSortButtons():
    """ Creates the first set of buttons that are used for sorting, the Bubble and Merge Buttons"""
    # Creating two buttons, one that runs RunBubbleSort, the other RunMergeSort(not implemented yet, calls selection sort)
    bubbleSortButton = customtkinter.CTkButton(master=currentlyDisplayedSortButtonLeftFrame[0], width=125,height=65,text="BUBBLE",text_color="white", font=("Great Vibes", 20), border_color="#84A98C", border_width=2, command=RunBubbleSort, fg_color="#52796F")
    mergeSortButton = customtkinter.CTkButton(master=currentlyDisplayedSortButtonLeftFrame[0], width=125,height=65,text="MERGE",text_color="white", font=("Great Vibes", 20), border_color="#84A98C", border_width=2, command=RunMergeSort, fg_color="#52796F")
    # Packing the buttons to the screen
    bubbleSortButton.pack(side="top", expand=False, padx=5, pady=10)
    mergeSortButton.pack(side="bottom", expand=False, padx=5, pady=10)
   

def CreateRightSortButtons():
    """ Creates the second set of buttons that are used for sorting, the Selection sort and Reset Buttons"""
    # Creating two buttons, one that runs the Selection Sort and the other that resets the data
    selectionSortButton = customtkinter.CTkButton(master=currentlyDisplayedSortButtonRightFrame[0], width=125,height=65,text="SELECTION",text_color="white", font=("Great Vibes", 20), border_color="#84A98C", border_width=2, command=RunSelectionSort, fg_color="#52796F")
    resetButton = customtkinter.CTkButton(master=currentlyDisplayedSortButtonRightFrame[0], width=125,height=65,text="RESET",text_color="white", font=("Great Vibes", 20), border_color="#84A98C", border_width=2, command=ResetWithNewData, fg_color="#52796F")
    # Packing the buttons to the screen
    selectionSortButton.pack(side="top", expand=False, padx=5, pady=10)
    resetButton.pack(side="bottom", expand=False, padx=5, pady=10)
    

    
def CreateSearchButtons():
    """ Creates the search box and search button to run a binary search """
    # Creating a new input field
    userInput = customtkinter.CTkEntry(master=currentlyDisplayedSearchButtonFrame[0], placeholder_text="Enter value to highlight", text_color="white", font=("Great Vibes", 15), width = 200, height= 50, placeholder_text_color="white", fg_color="#52796F")
    # Creating a new button
    userSearchButton = customtkinter.CTkButton(master=currentlyDisplayedSearchButtonFrame[0], width=125,height=65,text="SEARCH",text_color="white", font=("Great Vibes", 20), border_color="#84A98C", border_width=2, command=SearchForValue, fg_color="#52796F")
    # Packing the input field
    userInput.pack(side="left", padx=10)
    # Packing the button
    userSearchButton.pack(side="left", expand=False)
    # Appending the input field to a list, this is used to check when the user clicks search against the value in that input field
    userInputButton.append(userInput)
    

    
if __name__ == "__main__":
    Main()