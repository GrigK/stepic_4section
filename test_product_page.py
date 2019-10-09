import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

# @pytest.mark.parametrize('link', ["offer0",
#                                   "offer1",
#                                   "offer2",
#                                   "offer3",
#                                   "offer4",
#                                   "offer5",
#                                   "offer6",
#                                   pytest.param("offer7", marks=pytest.mark.xfail),
#                                   "offer8",
#                                   "offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     uri = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=" + link
#     print(uri)
#     page = ProductPage(browser, uri)
#     page.open()
#     page.add_product_to_basket()


# link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link2)
#     page.open()
#     page.should_be_add_button()
#     page.add_product_to_basket()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link2)
#     page.open()
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link2)
#     page.open()
#     page.is_disappered_success_message()


# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn_basket()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


# @pytest.mark.login
# class TestLoginFromProductPage():
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self):
#         self.product = ProductFactory(title="Best book created by robot")
#         # создаем по апи
#         self.link = self.product.link
#         yield
#         # после этого ключевого слова начинается teardown
#         # выполнится после каждого теста в классе
#         # удаляем те данные, которые мы создали
#         self.product.delete()
#
#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
#
#     def test_guest_should_see_login_link(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста