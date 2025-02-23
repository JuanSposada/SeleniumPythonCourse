import pytest
from selenium import webdriver


#@pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    #browser = request.param  #Es en singular "param" no "params" tenerlo encuenta
    print(f"creating {browser} Driver")
    if browser == 'chrome':
        my_driver = webdriver.Chrome()
    elif browser == 'firefox':
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"expected 'chrome' or 'firefox', but got {browser}, is not supported")
    #my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} Driver")
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )