from selene import browser, be, have


def test_search_selene(browser_management):
    browser.open('https://google.com')
    browser.element('[name=q]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id=search]').should(
        have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_non_existent_value(browser_management):
    browser.open('https://google.com')

    non_existent_value = 'sesleksleklsek'

    browser.element('[name=q]').should(be.blank).type(non_existent_value).press_enter()
    browser.element('.card-section [role=heading]').should(
        have.text(f'По запросу {non_existent_value} ничего не найдено'))
