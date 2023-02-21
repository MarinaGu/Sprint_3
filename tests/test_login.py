from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBurgers:
    def test_login(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys('bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text
        assert order == 'Оформить заказ'

    def test_login_lk(self, driver):
        driver.find_element(By.XPATH, ".//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys('bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text
        assert order == 'Оформить заказ'

    def test_login_reg_form(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys('bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text
        assert order == 'Оформить заказ'

    def test_login_rezet_pass_form(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys(
            'bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        order = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text
        assert order == 'Оформить заказ'