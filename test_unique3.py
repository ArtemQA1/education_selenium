from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import unittest

 class TestAbs(unittest.TestCase):
  def test_unique(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        num_list = ['first', 'second', 'third']
        for num in num_list:
            element = browser.find_element(By.CSS_SELECTOR,".first_block .form-control.{}".format(num))
            element.send_keys("test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME,"h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        self.assertEqual("Congratulations! You have successfully registered!",welcome_text)


  def test_unique2(self):

    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_list = ['first', 'second', 'third']
    for num in num_list:
        element = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.{}".format(num))
        element.send_keys("test")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

    self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

  if __name__ == "__main__":
    unittest.main()