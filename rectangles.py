import customtkinter as ctk

currentListToSort = []
currentRectanglesOnScreen = []

class RectangleWithValue:
    """ The RectangleWithValue class, is used when creating the frames that
    will be used as the visual for the data, this holds a frame object, its current value and its label
    """
    def __init__(self, frame, value, label):
        self.frame = frame
        self.value = value
        self.label = label
  
  
def GrabCurrentListToSort(curList):
    global currentListToSort
    currentListToSort.clear()
    currentListToSort.append(curList)
        
def CreateRectangleFrames(rectFrame, centerFrame, i=0):
    """ This is the same method as the CreateRectanglesFramesWithoutDelayAndHighlight, only
    its recursive, creating a delay after each rectangle to make a smooth effect at runtime. There is also
    no highlighting of the values
    """

    # Creating a new frame and label
    rectFrame = ctk.CTkFrame(master=centerFrame, height=(currentListToSort[0].listToSort[i] *3.5), width=23, border_color="#52796F", border_width=1, fg_color="#84A98C")
    rectLabel = ctk.CTkLabel(master=rectFrame, text=str(currentListToSort[0].listToSort[i]), text_color="white", font=("Great Vibes", 15))
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
        rectFrame.after(20, lambda frame=rectFrame, cFrame=centerFrame, index=(i+1):CreateRectangleFrames(frame,cFrame, index))
        
            
def UpdateRectangleFrames(valuesToCheck):
    """ This class is used for refreshing the data rectangles on the screen, two values are passed in
    and checked against, if the values are found inside of the rectangles, it highlights those rectangles.
    
    There is a second method very similer to this one, but has a delay when creating the information, its used
    at the initial start of the application to create a smooth effect of spawning in the data
    
        Arguments:
            int(valueOneToCheck): the first value to check against
            int(valueTwoToCheck): the second value to check against
    """

    
    # For the amount of numbers in the list to sort
    for index, i in enumerate(currentListToSort[0].listToSort):
        currentRectanglesOnScreen[index].frame.configure(height=3.5*i) 
        currentRectanglesOnScreen[index].label.configure(text=str(i))
        currentRectanglesOnScreen[index].value = i
       
    if not valuesToCheck:
        for rect in currentRectanglesOnScreen:
            rect.frame.configure(border_color="#52796F", fg_color="#84A98C")
    else:       
        for z in currentRectanglesOnScreen:
            # Assume no match initially
            match_found = False
            for value in valuesToCheck:
                if value == z.value:
                    # If a match is found, highlight the rectangle and break out of the inner loop
                    z.frame.configure(border_color="#52796F", fg_color="#28392c")
                    match_found = True
                    break

            # If no match was found, set default color
            if not match_found:
                z.frame.configure(border_color="#52796F", fg_color="#84A98C")