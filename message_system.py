import customtkinter as ctk

curMainFrame = []
messageLabel = []

def CreateMessageFrame(mainFrame):
    """ Creates the label used for displaying the current action to the user """
    # Creating a new label, its text is blank
    messageInput = ctk.CTkLabel(master=mainFrame, text="", text_color="white", font=("Great Vibes", 30))
    # Packing it to the screen
    messageInput.pack(side="top", pady=(0,25), expand=False)
    # Adding it to its list
    curMainFrame.append(mainFrame)
    messageLabel.append(messageInput)
    
def DisplayMessage(textToDisplay:str):
    """ Updates the text prompt with the given text and displays it to the screen
        Arguments:
            str(textToDisplay): The string for the text to display to the user
    """
    # Setting the text on the label to the passed in string
    messageLabel[0].configure(text=textToDisplay)
    # Updating the label
    #sentMessageLabel[0].update_idletasks()
    # After a little more than 2 seconds, resetting the label to be blank
    curMainFrame[0].after(2200, ClearMessageInput)
    


def ClearMessageInput():
    """ Erases any messages on the text prompt """
    # Setting the text on the label to be blank
    messageLabel[0].configure(text="")
    # Updating the label
    #sentMessageLabel[0].update_idletasks()