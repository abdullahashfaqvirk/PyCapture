import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap


class Screenshots(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi("app.ui", self)

        # Initialize screenshot_timer and stop_timer as None
        self.screenshot_timer = None
        self.stop_timer = None

        # Connect the Start and End buttons to the respective functions
        self.button1.clicked.connect(self.start)
        self.button2.clicked.connect(self.stop)
        self.counter = 1

        self.setFixedSize(self.size())

    # Define the function for taking screenshots
    def take_screenshot(self):
        try:
            pixmap = QtWidgets.QApplication.primaryScreen().grabWindow(QtWidgets.QApplication.desktop().winId())
            save_path = self.input3.text()
            if not save_path:
                raise ValueError('Save path is empty')
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            save_path += f'/screenshot_{self.counter}.png'
            pixmap.save(save_path)
            self.counter += 1
        except Exception as e:
            self.handle_error("Error taking screenshot", str(e))

    # Define the function for starting the screenshot application
    def start(self):
        try:
            save_path = self.input3.text()
            if not save_path:
                raise ValueError('Save path is empty')
            # Validate the inputs
            time_interval = self.input1.text()
            if not time_interval.isdigit() or int(time_interval) <= 0:
                raise ValueError('Invalid time interval')
            total_interval = self.input2.text()
            if total_interval.lower() == 'true':
                total_interval = -1
            elif not total_interval.isdigit() or int(total_interval) <= 0:
                raise ValueError('Invalid total interval')
            else:
                total_interval = int(total_interval)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            # Disable the input fields and Start button
            self.input1.setEnabled(False)
            self.input2.setEnabled(False)
            self.input3.setEnabled(False)
            self.button1.setEnabled(False)
            # Display the start message
            start_message = QtWidgets.QMessageBox(self)
            start_message.setStyleSheet("color: white; font-size: 12px;")
            start_message.setIcon(QtWidgets.QMessageBox.Icon.Information)
            start_message.setText('Program is starting...')
            start_message.setWindowTitle('Starting')
            start_message.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            start_message.show()
            # Start the timer for taking screenshots
            self.screenshot_timer = QTimer()
            self.screenshot_timer.timeout.connect(self.take_screenshot)
            self.screenshot_timer.start(int(time_interval) * 1000)
            # Start the timer for stopping the screenshot application
            if total_interval != -1:
                self.stop_timer = QTimer()
                self.stop_timer.setSingleShot(True)
                self.stop_timer.timeout.connect(self.stop)
                self.stop_timer.start(total_interval * 60000)
        except Exception as e:
            error_message = QtWidgets.QMessageBox(self)
            error_message.setStyleSheet("color: white; font-size: 12px;")
            error_message.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            error_message.setText(f"Error starting application: {str(e)}")
            error_message.setWindowTitle('Error')
            error_message.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            error_message.show()

    def stop(self):
        try:
            # Stop the screenshot timer
            if self.screenshot_timer is not None:
                self.screenshot_timer.stop()

            # Stop the stop timer
            if self.stop_timer is not None:
                self.stop_timer.stop()

            # Enable the input fields and Start button
            self.input1.setEnabled(True)
            self.input2.setEnabled(True)
            self.input3.setEnabled(True)
            self.button1.setEnabled(True)

            # Display the end message
            end_message = QtWidgets.QMessageBox(self)
            end_message.setStyleSheet("color: white; font-size: 12px;")
            end_message.setIcon(QtWidgets.QMessageBox.Icon.Information)
            end_message.setText('Program has ended.')
            end_message.setWindowTitle('Ending')
            end_message.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            end_message.show()
        except Exception as e:
            # Handle the error and display a message box to the user
            error_message = QtWidgets.QMessageBox(self)
            error_message.setStyleSheet("color: white; font-size: 12px;")
            error_message.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            error_message.setText('An error occurred while stopping the application. Please try again or contact support.')
            error_message.setWindowTitle('Error')
            error_message.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            error_message.show()

            
if __name__ == "__main__":
    # Create the Screenshots instance and display the window
    app = QtWidgets.QApplication(sys.argv)
    window = Screenshots()
    window.show()
    sys.exit(app.exec())
