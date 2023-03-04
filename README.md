# PyCapture
PyCapture app takes screenshots of the screen at regular intervals for a specified period of time.   

## Requirements   
**1.** Python 3.6 or higher   
**2.** PyQt5 library   

## Installation
**1.** Clone this repository   
**2.** Install the PyQt5 library by running the command ```pip install pyqt5```   

## Usage    
**1.** Run the command ```python app.py``` to start the application.   
**2.** Enter the time interval between screenshots in seconds and the duration of the screenshot capture in minutes.   
**3.** Enter the directory path where the screenshots will be saved.    
**4.** Click the "Start" button to start taking screenshots.    
**5.** Click the "End" button to stop the screenshot capture.   

## Code Overview    

### 1. Importing necessary modules:    
The first two lines of the code import the `sys` and `os` modules. These are standard Python modules used for system-level operations such as interacting with the file system and managing command-line arguments.   

The next two lines import classes from the **PyQt5 module**: `QtWidgets` and `uic`. QtWidgets provides a set of GUI elements such as **buttons**, **labels**, and **text fields**, while uic is a utility for loading UI files.    

Lastly, we import the `QTimer`, `Qt`, and `QPixmap` classes from `PyQt5.QtCore` and `PyQt5.QtGui`. QTimer is used for scheduling repetitive tasks, Qt contains various constants used for specifying event handling behavior, and QPixmap provides a way to work with images.      

### 2. Defining the Screenshots class:
The Screenshots class is a subclass of `QtWidgets.QMainWindow`. This means that it is a main window in a GUI application that contains a **menu bar**, **status bar**, and other **GUI elements**.    

The `__init__()` method initializes the object by calling the parent class's constructor and loading the UI file using the `uic.loadUi()` method.      

### 3. Defining the take_screenshot() method:
The take_screenshot() method is responsible for taking screenshots and saving them to the file system. It first captures a screenshot of the primary screen using `QtWidgets.QApplication.primaryScreen().grabWindow()`. It then retrieves the save path entered by the user in the input field and adds the filename to create the complete save path. The `pixmap.save()` method saves the screenshot to the specified path.    

### 4. Defining the start() method:
The start() method is called when the user clicks the Start button. It first validates the user's input and checks if a valid save path has been entered. If the inputs are valid, it disables the input fields and the Start button to prevent the user from changing the settings while the application is running.      

It then displays a message box to inform the user that the program is starting and starts a timer using `QTimer()`. The `QTimer.timeout.connect()` method connects the timer to the take_screenshot() method, so that it will take a screenshot every time the timer times out.    

If a total time interval has been specified, the start() method also starts a timer to stop the screenshot application after the specified time has elapsed. This is done using another `QTimer()` instance and the `QTimer.setSingleShot()` method. The stop() method is connected to the timeout signal of this timer.     

If any errors occur during this method, an error message is displayed to the user using a `QMessageBox()` instance.    

### 5. Defining the stop() method:    
The stop() method is called when the user clicks the End button or when the total time interval has elapsed. It stops the screenshot timer and the stop timer if they are running, enables the input fields and the Start button, and displays a message box to inform the user that the program has ended.    

If any errors occur during this method, an error message is displayed to the user using a `QMessageBox()` instance.    

### 6. Creating and showing the window:    
Finally, the `Screenshots()` instance is created and the window is displayed using the `window.show()` method. The application is started by calling `app.exec()` on the QApplication instance, and the program exits when the `sys.exit()` function is called.
