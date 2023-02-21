from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

faker = Faker()

class TestBurgers:
    def test_registration(self, driver):
        name = faker.name()
        email = faker.email()
        #проходим регистрацию
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//a[contains(text(),'Зарегистрироваться')]"))).click()
        driver.find_element(By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[1]/div/div/input[@name='name']").send_keys(name)
        driver.find_element(By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input[@name='name']").send_keys(email)
        driver.find_element(By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[3]/div/div/input[@name='Пароль']").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]").click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

        #проверяем что регистрация прошла успешно - переход на страницу авторизации
        current_url = driver.current_url
        assert 'login' in current_url



    def test_reg_not_correct_pass(self, driver):
        name = faker.name()
        email = faker.email()
        # проходим регистрацию
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//a[contains(text(),'Зарегистрироваться')]"))).click()
        WebDriverWait(driver, 3)

        driver.find_element(By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[1]/div/div/input[@name='name']").send_keys(name)
        driver.find_element(By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input[@name='name']").send_keys(email)
        driver.find_element(By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[3]/div/div/input[@name='Пароль']").send_keys('1234')
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 3)

        not_corr_pass = driver.find_element(By.XPATH, ".//form/fieldset[3]/div/p[@class='input__error text_type_main-default']").text
        assert not_corr_pass == 'Некорректный пароль'

