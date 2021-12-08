from selenium import webdriver
from asyncio import constants
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''1. Перейти по ссылке на главную страницу сайта Netpeak (https://netpeak.ua/)
2. Нажать на кнопку "О нас" и в выпавшем списке нажать кнопку "Команда"
3. Нажать кнопку "Стать частью команды" и убедится что в новой вкладке открылась страница Работа в Нетпик
4. Убедится что на странице есть кнопка "Я хочу работать в Netpeak" и на нее можно кликнуть
5. Вернутся на предыдущую вкладку и нажать кнопку "Личный кабинет"
6. На странице личного кабинета заполнить Логин и Пароль случайными данными. 
7. Проверить что кнопка "Войти" не доступна
8. Отметить чекбокс "Авторизируясь, вы соглашаетесь с Политикой конфиденциальности"
9. Нажать на кнопку войти и проверить наличие нотификации о неправильном логине или пароле
10. Проверить что Логин и Пароль подсветились красным цветом '''
url = 'https://netpeak.ua/'
driver = webdriver.Chrome()
driver.get(url)
driver.set_window_position(1400, 0)
driver.maximize_window()
time.sleep(5)
# 2. Нажать на кнопку "О нас" и в выпавшем списке нажать кнопку "Команда"
button_about = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//li[@class="main-link"][3]'))).click()
print("opened about us")
button_team = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="links-box"]/a[@href="/team/"]'))).click()
print("clicked on team")
# 3. Нажать кнопку "Стать частью команды" и убедится что в новой вкладке открылась страница Работа в Нетпик

button_member = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//a[@class="tn-atom"]'))).click()
handle = driver.window_handles
try:
    driver.switch_to_window(handle[1])
except:
    print('not new tab')

print('opened in new tab')
# 4. Убедится что на странице есть кнопка "Я хочу работать в Netpeak" и на нее можно кликнуть
try:
    button_I_want_to_work = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="text-center agree-btn"]/a[@href="https://career.netpeak.group/hiring/"]')))
    button_I_want_to_work_click = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="text-center agree-btn"]/a[@href="https://career.netpeak.group/hiring/"]')))
except:
    print("not clickable")
# 5. Вернутся на предыдущую вкладку и нажать кнопку "Личный кабинет"
driver.switch_to.window(handle[0])
button_account = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//a[@class="custom-link"]'))).click()
print("opened personal account")
# 6. На странице личного кабинета заполнить Логин и Пароль случайными данными.
button_login = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@id="login"]')))
button_login.send_keys("Iwannaworkhere")
button_password = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys("uf2222222")
button_registration = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//span[@class="text ng-binding ng-scope"]')))
# 7. Проверить что кнопка "Войти" не доступна
verify = button_registration.get_property('disabled')
print(verify)
# 8. Отметить чекбокс "Авторизируясь, вы соглашаетесь с Политикой конфиденциальности"
check_box2 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[4]/div/md-checkbox/div[1]'))).click()
print('checkbox')
# 9. Нажать на кнопку войти и проверить наличие нотификации о неправильном логине или пароле
button_registration = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//span[@class="text ng-binding ng-scope"]'))).click()


def wait_alert_is_present(driver):
    return WebDriverWait(
        driver,
        constants.ux.MAX_ALERT_WAIT) \
        .until(EC.alert_is_present())


# 10. Проверить что Логин и Пароль подсветились красным цветом
red = 'rgba(255, 0, 0, 1)'
verify_login = driver.find_element_by_xpath('//input[@id="login"]')
assert verify_login.value_of_css_property("color") == red
verify_password = driver.find_element_by_xpath('//input[@type="password"]')
assert verify_password.value_of_css_property("color") == red

driver.close()
