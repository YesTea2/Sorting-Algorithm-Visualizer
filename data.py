""" data.py - Module containing the logic related to creating and manipulating data

This module contains the information for performing a binarysearch on the data as well as displaying
a rainbow text effect


This script pools from these custom modules:
    rectangles.py:
        A module that contains the logic related to displaying the data to the screen as rectangles
    message_system.py:
        A module that contains the logic for a message system used to display what is currently happening to the user
    gui.py:
        A module that contains the logic for the gui that is displayed to the user
        
"""

from message_system import DisplayMessage as msg
from message_system import ClearMessageInput as clrMsg
from rectangles import UpdateRectangleFrames as rectUpdate

import message_system
import rectangles
import gui

currentListToSort = []


def GrabCurrentListToSort(listToSort):
    """The current SortList object is passed in as an argument
    and placed in a list to refrence in
    the different functions of this module

        Arguments:
            SortList(curList): The current SortList object
    """
    global currentListToSort
    # Clearing any SortList objects in the list
    currentListToSort.clear()
    # Appending the passed in SortList object to the list
    currentListToSort.append(listToSort)


def BinarySearch(xValue, minValue, maxValue):
    """Performs a binary search, using the users inputted value as the xValue
    and continusly checks against the min and max value until found
    """
    # If the max value is greater than the minimum value, this has ran
    # enough times to have found that the number inputted is not included in this list
    if maxValue < minValue:
        # Value not found
        msg("Value not found")
        return

    # Creating a midpoint value,  between minValue and maxValue.
    midValue = minValue + (maxValue - minValue) // 2

    # If the middle value inside the list is equal to the users inputted value, the search found their value
    if currentListToSort[0].listToSort[midValue] == xValue:
        # Value found!
        msg(f"VALUE {xValue}, FOUND!")
        # Refresh the rectangles, highlight the value
        rectUpdate([xValue])
        gui.currentlyDisplayedMainFrame[0].after(
            2500,
            lambda value=xValue: PerformRainbow(
                f"VALUE {value} FOUND!",
                rectangles.currentRectanglesOnScreen,
                gui.buttonsOnScreen,
                gui.labelsOnScreen,
                gui.userInputButton,
                message_system.messageLabel,
                gui.currentlyDisplayedMainFrame[0],
            ),
        )

    # If the value in the middle is greater than the users inputted value
    elif currentListToSort[0].listToSort[midValue] > xValue:
        # Highlight the current minValue and maxValue on the rectangles
        rectUpdate([minValue, midValue, maxValue])
        msg(f"CHECKING MIN={minValue}, MID={midValue} MAX={maxValue}")
        # Rerun this search after 3 seconds, passing in the same x value, the same minValue but setting the new max value to be the middle value - 1
        gui.currentlyDisplayedMainFrame[0].after(
            2500,
            lambda x=xValue, minV=minValue, maxV=(midValue - 1): BinarySearch(
                x, minV, maxV
            ),
        )
    # Else if the middle value is less than the inputted value
    else:
        # Highlight the current minValue and maxValue on the rectangles
        rectUpdate([minValue, midValue, maxValue])
        msg(f"CHECKING MIN={minValue}, MID={midValue}, MAX={maxValue}")
        # Rerun this search after 3 seconds, passing in the same x value, changing the minValue to be the middle value + 1, and using the same maxValue
        gui.currentlyDisplayedMainFrame[0].after(
            2500,
            lambda x=xValue, minV=(midValue + 1), maxV=maxValue: BinarySearch(
                x, minV, maxV
            ),
        )


def PerformRainbow(
    textToDisplay,
    currentRectanglesOnScreen: list,
    buttonsOnScreen: list,
    labelsOnScreen: list,
    userInputButton: list,
    sentMessageLabel: list,
    mainFrame,
    index=0,
):
    """Creates a rainbow effect with all of the data and text on the screen

    Arguments:
        str(textToDisplay): the message to display to the user
        list(currentRectanglesOnScreen): A list containing all of the rectangle objects of data
        list(buttonsOnScreen): A list containing all of the button objects on the screen
        list(userInputButton): The button for userInput, grabbed seperatly due to the naming of its text paramater
        list(sentMessageLabel): The main text label to display to the user
        frame(mainFrame): The main gui frame, used for delaying recursion calls
        int(index): The index value of the recursion loop
    """
    # All of this checks what the index number is, depending on the index number
    # changes the color of every element passed into the function as a color of the rainbow based on the index number.

    # This continues to loop until the index is equal to 13, than sets all of the colors
    # back to their original values.

    # It felt incredibly repetitive to add comments to each element in this method,
    # I hope this was descriptive enough as to what is going on in this block of code.
    if index == 13:
        for rect in currentRectanglesOnScreen:
            rect.frame.configure(border_color="#52796F", fg_color="#84A98C")
        sentMessageLabel[0].configure(text=textToDisplay, text_color="white")
        mainFrame.after(2200, clrMsg)
        for button in buttonsOnScreen:
            button.configure(text_color="white")
        for label in labelsOnScreen:
            label.configure(text_color="white")
        userInputButton[0].configure(placeholder_text_color="white")
        return
    else:
        if index == 0 or index == 6:
            for rect in currentRectanglesOnScreen:
                rect.frame.configure(border_color="#52796F", fg_color="#e81416")
            index += 1
            mainFrame.after(
                25,
                lambda textMessage=textToDisplay, curRect=currentRectanglesOnScreen, curBut=buttonsOnScreen, curLab=labelsOnScreen, curUse=userInputButton, sendM=sentMessageLabel, mFrame=mainFrame, i=index: PerformRainbow(
                    textMessage, curRect, curBut, curLab, curUse, sendM, mFrame, i
                ),
            )
            sentMessageLabel[0].configure(text=textToDisplay, text_color="#e81416")
            for button in buttonsOnScreen:
                button.configure(text_color="#e81416")
            for label in labelsOnScreen:
                label.configure(text_color="#e81416")
            userInputButton[0].configure(placeholder_text_color="#e81416")
            return
        if index == 1 or index == 7:
            for rect in currentRectanglesOnScreen:
                rect.frame.configure(border_color="#52796F", fg_color="#ffa500")
            index += 1
            mainFrame.after(
                25,
                lambda textMessage=textToDisplay, curRect=currentRectanglesOnScreen, curBut=buttonsOnScreen, curLab=labelsOnScreen, curUse=userInputButton, sendM=sentMessageLabel, mFrame=mainFrame, i=index: PerformRainbow(
                    textMessage, curRect, curBut, curLab, curUse, sendM, mFrame, i
                ),
            )
            sentMessageLabel[0].configure(text=textToDisplay, text_color="#ffa500")
            for button in buttonsOnScreen:
                button.configure(text_color="#ffa500")
            for label in labelsOnScreen:
                label.configure(text_color="#ffa500")
            userInputButton[0].configure(placeholder_text_color="#ffa500")
            return
        if index == 2 or index == 8:
            for rect in currentRectanglesOnScreen:
                rect.frame.configure(border_color="#52796F", fg_color="#faeb36")
            index += 1
            mainFrame.after(
                25,
                lambda textMessage=textToDisplay, curRect=currentRectanglesOnScreen, curBut=buttonsOnScreen, curLab=labelsOnScreen, curUse=userInputButton, sendM=sentMessageLabel, mFrame=mainFrame, i=index: PerformRainbow(
                    textMessage, curRect, curBut, curLab, curUse, sendM, mFrame, i
                ),
            )
            sentMessageLabel[0].configure(text=textToDisplay, text_color="#faeb36")
            for button in buttonsOnScreen:
                button.configure(text_color="#faeb36")
            for label in labelsOnScreen:
                label.configure(text_color="#faeb36")
            userInputButton[0].configure(placeholder_text_color="#faeb36")
            return
        if index == 3 or index == 9:
            for rect in currentRectanglesOnScreen:
                rect.frame.configure(border_color="#52796F", fg_color="#79c314")
            index += 1
            mainFrame.after(
                25,
                lambda textMessage=textToDisplay, curRect=currentRectanglesOnScreen, curBut=buttonsOnScreen, curLab=labelsOnScreen, curUse=userInputButton, sendM=sentMessageLabel, mFrame=mainFrame, i=index: PerformRainbow(
                    textMessage, curRect, curBut, curLab, curUse, sendM, mFrame, i
                ),
            )
            sentMessageLabel[0].configure(text=textToDisplay, text_color="#79c314")
            for button in buttonsOnScreen:
                button.configure(text_color="#79c314")
            for label in labelsOnScreen:
                label.configure(text_color="#79c314")
            userInputButton[0].configure(placeholder_text_color="#79c314")
            return
        if index == 4 or index == 10:
            for rect in currentRectanglesOnScreen:
                rect.frame.configure(border_color="#52796F", fg_color="#487de7")
            index += 1
            mainFrame.after(
                25,
                lambda textMessage=textToDisplay, curRect=currentRectanglesOnScreen, curBut=buttonsOnScreen, curLab=labelsOnScreen, curUse=userInputButton, sendM=sentMessageLabel, mFrame=mainFrame, i=index: PerformRainbow(
                    textMessage, curRect, curBut, curLab, curUse, sendM, mFrame, i
                ),
            )
            sentMessageLabel[0].configure(text=textToDisplay, text_color="#487de7")
            for button in buttonsOnScreen:
                button.configure(text_color="#487de7")
            for label in labelsOnScreen:
                label.configure(text_color="#487de7")
            userInputButton[0].configure(placeholder_text_color="#487de7")
            return
        if index == 5 or index == 11:
            for rect in currentRectanglesOnScreen:
                rect.frame.configure(border_color="#52796F", fg_color="#4b369d")
            index += 1
            mainFrame.after(
                25,
                lambda textMessage=textToDisplay, curRect=currentRectanglesOnScreen, curBut=buttonsOnScreen, curLab=labelsOnScreen, curUse=userInputButton, sendM=sentMessageLabel, mFrame=mainFrame, i=index: PerformRainbow(
                    textMessage, curRect, curBut, curLab, curUse, sendM, mFrame, i
                ),
            )
            sentMessageLabel[0].configure(text=textToDisplay, text_color="#4b369d")
            for button in buttonsOnScreen:
                button.configure(text_color="#4b369d")
            for label in labelsOnScreen:
                label.configure(text_color="#4b369d")
            userInputButton[0].configure(placeholder_text_color="#4b369d")
            return
        if index == 6 or index == 12:
            for rect in currentRectanglesOnScreen:
                rect.frame.configure(border_color="#52796F", fg_color="#70369d")
            index += 1
            mainFrame.after(
                25,
                lambda textMessage=textToDisplay, curRect=currentRectanglesOnScreen, curBut=buttonsOnScreen, curLab=labelsOnScreen, curUse=userInputButton, sendM=sentMessageLabel, mFrame=mainFrame, i=index: PerformRainbow(
                    textMessage, curRect, curBut, curLab, curUse, sendM, mFrame, i
                ),
            )
            sentMessageLabel[0].configure(text=textToDisplay, text_color="#70369d")
            for button in buttonsOnScreen:
                button.configure(text_color="#70369d")
            for label in labelsOnScreen:
                label.configure(text_color="#70369d")
            userInputButton[0].configure(placeholder_text_color="#70369d")
            return
