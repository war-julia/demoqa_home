import pytest
from pages.swag_labs import SwagLabs


def test_icon_existence(setup):
    driver = setup
    swag_labs_page = SwagLabs(driver)

    swag_labs_page.visit()

    assert swag_labs_page.exist_icon(), "Иконка не найдена на странице"
