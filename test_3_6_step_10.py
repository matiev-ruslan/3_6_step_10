
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_add_to_basket_button_on_page(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button

