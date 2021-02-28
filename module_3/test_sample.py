from selenium import webdriver
page_link = "http://selenium1py.pythonanywhere.com/ru/"

book = "The shellcoder's handbook"
catalogue_locator = "[href='/ru/catalogue/']"
title_of_book_locator = "[title=\"The shellcoder's handbook\"]" #не нашла пока как внести book в данный локатор
add_to_basket_locator = "button[value='Добавить в корзину']"

def test_add_to_basket():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(page_link)

        # Act
        browser.find_element_by_css_selector(catalogue_locator).click()
        browser.find_element_by_css_selector(title_of_book_locator).click()
        browser.find_element_by_css_selector(add_to_basket_locator).click()

        # Assert
        all_alerts = browser.find_element_by_id("messages")

        assert book in all_alerts.text, \
            f"Result page should contain record: \"\'{book}' был добавлен в вашу корзину\""

    finally:
        browser.quit()

if __name__ == "__main__":
    test_add_to_basket()
    print("All tests passed!")