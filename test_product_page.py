from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_product_page_add_to_busket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_button()
    page.add_product_to_basket()
