from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBurgers:
    def test_designer_rolls(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys('bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[1]/div[2]/span"))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[1]/div[1]/span"))).click()

        rolls = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[2]/ul[1]/a[1]/p"))).text
        assert rolls == 'Флюоресцентная булка R2-D3'


    def test_designer_sauces(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys('bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[1]/div[2]/span"))).click()

        sauces = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[2]/ul[2]/a[1]/p"))).text
        assert sauces == 'Соус Spicy-X'

    def test_designer_fillings(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input[@name='name']").send_keys('bellkim@example.org')
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[1]/div[3]/span"))).click()

        fillings = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[2]/ul[3]/a[1]/p"))).text
        assert fillings == 'Мясо бессмертных моллюсков Protostomia'