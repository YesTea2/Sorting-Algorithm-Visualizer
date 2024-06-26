# Sorting Algorithm Visualizer - a Python application using CustomTkinter

An application that displays multiple sorting algorithms visually on the screen by manipulating the data of rectangles

This also includes using a Binary Search to look up individual values after sorting the data.

Created for CS162 spring term 2024 at Linn-Benton Community College

Packages needed:
    CustomTkinter build > 0.3
    Random 

*** Notes ***

    While the merge sort option does work and will eventually display the data sorted properly, I was unable to find a solution to have it
    display each step without breaking how the merge sort operates, instead there is a print statement kept inside this function so it can be
    seen that it is running a merge sort. 
    
    The merge sort also presented a problem with not being able to find a good way to 
    have a condition to check when it's finished, once you click the merge sort
    DO NOT CLICK any other buttons until the GUI updates with the sorted data otherwise, it will break the application.
    
    All of the other sorting options have fail-safes to prevent the user from clicking anything 
    while the sorting is happening, but the merge sort toggles the bools off the second it's clicked instead of when it's finished.

![alt text](https://github.com/YesTea2/CS162-Project-6/blob/main/Screenshots/Selection2.gif)

![alt text](https://github.com/YesTea2/CS162-Project-6/blob/main/Screenshots/shot2.png)
![alt text](https://github.com/YesTea2/CS162-Project-6/blob/main/Screenshots/shot3.png)
![alt text](https://github.com/YesTea2/CS162-Project-6/blob/main/Screenshots/shot4.png)
Screenshot showing the merge sort working
![alt text](https://github.com/YesTea2/CS162-Project-6/blob/main/Screenshots/shot5.png)
