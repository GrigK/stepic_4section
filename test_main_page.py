from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
link = "http://selenium1py.pythonanywhere.com/"

# def test_guest_should_see_login_link(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_goto_login_page(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()

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


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Гость открывает главную страницу
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_btn_basket()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
