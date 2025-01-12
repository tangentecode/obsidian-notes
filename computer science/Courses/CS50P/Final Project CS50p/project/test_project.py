import sys
from PyQt6.QtWidgets import QApplication
import pytest
from unittest.mock import patch
from project import launchWindow, guide, github_repo


@pytest.fixture
def qt_app():
    app = QApplication(sys.argv)
    yield app
    app.quit()


def test_launchWindow(qt_app):
    from project import StartWindow  
    

    window = StartWindow()
    window.show()


    assert window is not None 
    assert window.isVisible() 


@patch('builtins.print') 
def test_guide(mock_print):
    """Test the guide function."""
    guide()
    mock_print.assert_called_once_with("[INFO] For a detailed guide look at the README file in the project directory")


@patch('builtins.print')  
def test_github_repo(mock_print):
    """Test the github_repo function."""
    github_repo()
    assert mock_print.call_count == 2
    mock_print.assert_any_call("[INFO] Take a look at the github repo for this project to downlad an portable executable of the game!")
    mock_print.assert_any_call("[INFO] Link: https://github.com/TangenteLakai/2048-Python-PyQt6-Project")