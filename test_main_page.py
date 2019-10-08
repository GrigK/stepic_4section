from .pages.main_page import MainPage
from .pages.login_page import LoginPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_goto_login_page(browser):
    global link
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_product_page_add_to_busket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

"""
Рассмотрим страницу товара в интернет магазине http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/.

Тесты будут выглядеть примерно так:

def test_add_to_cart(browser):
    page = ProductPage(url="", browser)   # инициализируем объект Page Object
    page.open()                           # открываем страницу в браузере
    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart()            # жмем кнопку добавить в корзину 
    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом
"""
