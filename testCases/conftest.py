# pytest_addoption allows the user to pass the --browser argument when running the tests from the command line.
# browser fixture retrieves the value of the --browser argument and provides it to the setup fixture.
# setup fixture uses the value of browser to initialize the correct WebDriver (Chrome or Firefox) and returns it to the test functions that depend on it.


import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver = webdriver.Firefox()
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):     #this will get the value from CLI/hooks
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):    #this will return the browser value to setup method
    return request.config.getoption('--browser')

##################### PyTest HTML Report #####################

# it is hook for adding environment info to HTML Report

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Manas'
#
# #it is hook for delete/modify environment info to html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     if 'Java_HOME' in metadata:
#         metadata.pop('Java_HOME',None)
#     if 'Plugins' in metadata:
#         metadata.pop('Plugins',None)
#
# # If you want to add the ability to specify the report location in your pytest configuration:
# def pytest_configure(config):
#     config.option.htmlpath = 'report.html'


# ==============================================================

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Manas'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

