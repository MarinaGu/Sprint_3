from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBurgers:
    def test_lk(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys('bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 3)

        current_url = driver.current_url
        assert 'account' in current_url

    def test_lk_on_design(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys('bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//p[contains(text(),'Конструктор')]"))).click()

        order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text
        assert order == 'Оформить заказ'

    def test_lk_on_logo(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys('bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 3)

        driver.find_element(By.XPATH, ".//header/nav[1]/div[1]/a[1]/*[1]").click()

        order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text
        assert order == 'Оформить заказ'

    def test_log_out(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys('bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 3)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Выход']"))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

        current_url = driver.current_url
        assert 'login' in current_url