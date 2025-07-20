from pages.swag_labs import SwagLabs

def test_check_icon(browser):




    demo_home_page = SwagLabs(browser)
    demo_home_page.visit()
    time.sleep(3)
    demo_home_page.click_on_the_icon()
    time.sleep(3)
    assert demo_home_page.equal_url()
    assert demo_home_page.exist_icon()
