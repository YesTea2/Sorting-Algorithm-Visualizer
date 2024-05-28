""" gui.py - Module containing the logic related to creating the GUI the user is presented with on the screen

This module contains the information for creating the frames, buttons, labels and any other visual element
that is displayed on the screen other than the rectangle data information.


This script pools from these custom modules:
    button_functions:
        A module that contains the logic for what happens when the user clicks a button
        
"""



import customtkinter as ctk
import button_functions as bttns

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

userInputButton = []
buttonsOnScreen = []
labelsOnScreen = []

# Creating an empty list to hold all of the buttons
buttonOnScreen = []

def CreateRootFrame():
    """" Creates the root frame that all other frames are children of."""

    # Initilizing a new instance of cTK
    frame = ctk.CTk()
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
    mainFrame = ctk.CTkFrame(master=rootFrame[0])

    # Packing the frame to the screen, setting it to fill the length and width of the window and to expand to max value
    mainFrame.pack(fill="both", expand=True)

    # Setting the color for the entire window
    mainFrame.configure(fg_color="black")

    # Appending the newly created main frame to the list of main frame
    currentlyDisplayedMainFrame.append(mainFrame)

def CreateCenterFrame():
    """ Creates the centeral frame"""
    # Creating the center frame, setting its master to the mainFrame
    centerFrame = ctk.CTkFrame(master=currentlyDisplayedMainFrame[0], width= 1340, height=450, fg_color="#354F52",border_color="#84A98C",border_width=2)
    # Packing to the screen
    centerFrame.pack(expand=True, pady= 75, fill="both")
    # Adding it to its list to carry over into other methods
    
    currentCenterFrame.append(centerFrame)
    
    
def CreateMainButtonFrame():
    """ Creates the frame that the bottom buttons will nest inside of"""

    # Initilizing a new frame and setting its parent to the main frame
    mainButtonFrame = ctk.CTkFrame(master=currentlyDisplayedMainFrame[0])

    # Setting it to fill its width and height to the parent frame
    mainButtonFrame.pack(pady=40, padx=0,expand=False)

    # Setting the background color of the frame ( this could also be set as transparent as
    # its the same color as the parent frame, but its the same amount of memory either way).
    mainButtonFrame.configure(fg_color="transparent")

    # Appending the frame to the list of main button frames.
    currentlyDisplayedMainButtonFrame.append(mainButtonFrame)


        

def CreateRightSideMainButtonFrame():
    """ Creates the frame that holds the left side buttons """
    
    # Creating the frame
    frame = ctk.CTkFrame(master=currentlyDisplayedMainButtonFrame[0], width=300, fg_color="transparent")
    # Packing to the screen
    frame.pack(side="right", padx=(200,200))
    # Creating a label to sit at the top of the frame
    label = ctk.CTkLabel(master=frame, text="DATA SEARCHING", text_color="white", font=("Great Vibes", 30))
    # Packing the label
    label.pack(side="top", pady=(0,20))
    # Appending the newly created frame to the list that holds it for refrence
    
    
    currentlyDisplayedRightSideMainButtonFrame.append(frame)

    labelsOnScreen.append(label)
    # Creating the frame that nest inside this frame
    CreateSearchButtonFrame()
    
    
    
def CreateLeftSideMainButtonFrame():
    """ Creates the frame that holds the right side buttons """
    # Creating the frame
    frame = ctk.CTkFrame(master=currentlyDisplayedMainButtonFrame[0], width = 250, fg_color="transparent")
    # Packing to the screen
    frame.pack(side="left", padx=(200,0))
    # Creating a label to sit at the top of the frame
    label = ctk.CTkLabel(master=frame, text="DATA SORTING", text_color="white", font=("Great Vibes", 30))
    # Packing the label
    label.pack(side="top", pady=(0,20))
    # Appending the newly created frame to the list that holds it for refrence
    currentlyDisplayedLeftSideMainButtonFrame.append(frame)
    labelsOnScreen.append(label)
    # Creating the frames that will nest inside this frame
    CreateSortButtonFrameLeft()
    CreateSortButtonFrameRight()



def CreateSortButtonFrameLeft():
    """ Creates the left side frame that nests inside the left side button frame, this
    seems redudent, but its the only way to have the buttons sit how I wanted
    """
    # Creating the frame
    sortFrame = ctk.CTkFrame(master=currentlyDisplayedLeftSideMainButtonFrame[0], width= 200, fg_color="transparent")
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
    sortFrame = ctk.CTkFrame(master=currentlyDisplayedLeftSideMainButtonFrame[0], width=200, fg_color="transparent")
    # Packing the frame
    sortFrame.pack(side="left", padx=10)
    
    # Adding the frame to the list that holds it for refrence
    currentlyDisplayedSortButtonRightFrame.append(sortFrame)
    # Creating the buttons that nest inside this frame
    CreateRightSortButtons()
    
def CreateSearchButtonFrame():
    """ Creates the frame that the right side buttons will nest inside """
    # Create the frame
    searchFrame = ctk.CTkFrame(master=currentlyDisplayedRightSideMainButtonFrame[0], width= 600, fg_color="transparent")
    # Pack the frame
    searchFrame.pack(side="right", padx=20)
    # Append the frame to the list that is used for refrence
    currentlyDisplayedSearchButtonFrame.append(searchFrame)
    # Create the search buttons inside this frame
    CreateSearchButtons()
    

def CreateLeftSortButtons():
    """ Creates the first set of buttons that are used for sorting, the Bubble and Merge Buttons"""
    # Creating two buttons, one that runs RunBubbleSort, the other RunMergeSort(not implemented yet, calls selection sort)
    bubbleSortButton = ctk.CTkButton(master=currentlyDisplayedSortButtonLeftFrame[0], width=125,height=65,text="BUBBLE",text_color="white", font=("Great Vibes", 20), border_color="#84A98C", border_width=2, command=bttns.RunBubbleSort, fg_color="#52796F")
    mergeSortButton = ctk.CTkButton(master=currentlyDisplayedSortButtonLeftFrame[0], width=125,height=65,text="MERGE",text_color="white", font=("Great Vibes", 20), border_color="#84A98C", border_width=2, command=bttns.RunMergeSort, fg_color="#52796F")
    # Packing the buttons to the screen
    bubbleSortButton.pack(side="top", expand=False, padx=5, pady=10)
    mergeSortButton.pack(side="bottom", expand=False, padx=5, pady=10)
    
    buttonsOnScreen.append(bubbleSortButton)
    buttonsOnScreen.append(mergeSortButton)
   

def CreateRightSortButtons():
    """ Creates the second set of buttons that are used for sorting, the Selection sort and Reset Buttons"""
    # Creating two buttons, one that runs the Selection Sort and the other that resets the data
    selectionSortButton = ctk.CTkButton(master=currentlyDisplayedSortButtonRightFrame[0], width=125,height=65,text="SELECTION",text_color="white", font=("Great Vibes", 20), border_color="#84A98C", border_width=2, command=bttns.RunSelectionSort, fg_color="#52796F")
    resetButton = ctk.CTkButton(master=currentlyDisplayedSortButtonRightFrame[0], width=125,height=65,text="RESET",text_color="white", font=("Great Vibes", 20), border_color="#84A98C", border_width=2, command=bttns.ResetWithNewData, fg_color="#52796F")
    # Packing the buttons to the screen
    selectionSortButton.pack(side="top", expand=False, padx=5, pady=10)
    resetButton.pack(side="bottom", expand=False, padx=5, pady=10)

    buttonsOnScreen.append(selectionSortButton)
    buttonsOnScreen.append(resetButton)
    

    
def CreateSearchButtons():
    """ Creates the search box and search button to run a binary search """
    # Creating a new input field
    userInput = ctk.CTkEntry(master=currentlyDisplayedSearchButtonFrame[0], placeholder_text="Enter value to highlight", text_color="white", font=("Great Vibes", 15), width = 200, height= 50, placeholder_text_color="white", fg_color="#52796F")
    # Creating a new button
    userSearchButton = ctk.CTkButton(master=currentlyDisplayedSearchButtonFrame[0], width=125,height=65,text="SEARCH",text_color="white", font=("Great Vibes", 20), border_color="#84A98C", border_width=2, command=bttns.SearchForValue, fg_color="#52796F")
    # Packing the input field
    userInput.pack(side="left", padx=10)
    # Packing the button
    userSearchButton.pack(side="left", expand=False)
    
    # Appending the input field to a list, this is used to check when the user clicks search against the value in that input field
    userInputButton.append(userInput)
    buttonsOnScreen.append(userSearchButton)
    
