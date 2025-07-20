import pytest
from pages.swag_labs import SwagLabs


def test_icon_existence(setup):
    driver = setup
    swag_labs_page = SwagLabs(driver)

    swag_labs_page.visit()

    assert swag_labs_page.exist_icon(), "Иконка не найдена на странице"


def test_username_field_existence(setup):
    driver = setup
    swag_labs_page = SwagLabs(driver)

    swag_labs_page.visit()

    assert swag_labs_page.exist_username_field(), "Поле имени не найдено на странице"


def test_password_field_existence(setup):
    driver = setup
    swag_labs_page = SwagLabs(driver)

    swag_labs_page.visit()

    assert swag_labs_page.exist_password_field(), "Поле пароля не найдено на странице"

