from selenium.webdriver.common.by import By
import time

link_main = 'https://phptravels.com/demo/'
link_cms = 'https://phptravels.net/api/admin/cms'
link_page_title = 'https://phptravels.net/api/Test-page'

''' Для запуска теста использовать в терминале команду: 
pytest test_front_web.py'''
def test_task_front_web(browser):
    browser.get(link_main)
    button = browser.find_element(By.CSS_SELECTOR, '[href="//www.phptravels.net/admin"].btn')
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    input_email = browser.find_element(By.CSS_SELECTOR, '.form-signin [name="email"]')
    input_email.send_keys("admin@phptravels.com")
    input_pass = browser.find_element(By.CSS_SELECTOR, '.form-signin [name="password"]')
    input_pass.send_keys("demoadmin")
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"] .ladda-label').click()
    time.sleep(2)
    browser.get(link_cms)
    browser.find_element(By.CSS_SELECTOR, '.add_button .btn').click()
    browser.find_element(By.CSS_SELECTOR, 'form [name="pagetitle"]').send_keys('Test page')
    browser.find_element(By.CSS_SELECTOR, 'form [name="pageslug"]').send_keys('Test-page')
    browser.find_element(By.CSS_SELECTOR, 'form [name="externalink"]').send_keys('https://phptravels.net/api/Test-page')
    browser.find_element(By.CSS_SELECTOR, 'form [name="page_icon"]').send_keys('Test1_icon')
    browser.find_element(By.CSS_SELECTOR, 'form [name="keywords"]').send_keys(
        'Test1_keywords,word1,2wo2rd2,Word3,WORD4,123123,!@1#aD')
    browser.find_element(By.CSS_SELECTOR, 'form [name="pagedesc"]').send_keys('Test1_description')
    button_source = browser.find_element(By.CSS_SELECTOR, '#cke_46.cke_button__source')
    time.sleep(1)
    button_source.click()
    browser.find_element(By.CSS_SELECTOR, '[title="Rich Text Editor, pagebody"]').send_keys('source_text')
    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, '.btn-lg').click()
    browser.get(link_cms)
    browser.find_element(By.XPATH,
                         '//td[text()="Test page"]')
    browser.get(link_page_title)
    assert browser.find_element(By.CSS_SELECTOR, '.sec__title_list').text == "Test page", 'имя не совпадает'
    assert browser.find_element(By.CSS_SELECTOR,
                                '[class="container mt-5 mb-5"]').text == "source_text", 'содержание не совпадает'
    browser.get(link_cms)
    browser.find_element(By.CSS_SELECTOR, 'table.xcrud-list tbody tr:first-child [title="DELETE"]').click()
    alert = browser.switch_to.alert
    alert.accept()
