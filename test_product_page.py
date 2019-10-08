import pytest
from .pages.product_page import ProductPage


# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.parametrize('link', ["offer0",
                                  "offer1",
                                  "offer2",
                                  "offer3",
                                  "offer4",
                                  "offer5",
                                  "offer6",
                                  pytest.param("offer7", marks=pytest.mark.xfail),
                                  "offer8",
                                  "offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    uri = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=" + link
    print(uri)
    page = ProductPage(browser, uri)
    page.open()
    page.add_product_to_basket()
