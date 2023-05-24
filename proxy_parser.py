from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://proxy6.net/"

# Настройка опций
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537."
                     "36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
options.add_argument("--disable-bink-features=AutomationControlled")

# Путь до файла драйвера
driver = webdriver.Chrome(
    executable_path="Domconnect/chromedriver",
    options=options
)

try:
    driver.get(url)  # Обращение к сайту

    login_win = driver.find_element(by=By.CLASS_NAME, value="icon-login")
    login_win.click()  # Нажатие на кнопку "Войти"
    time.sleep(1)

    # Ввод Email(указан на прямую в коде)
    driver.find_element(by=By.CSS_SELECTOR, value="#form-login > div:nth-child(1) > div > input["
                                                  "type=email]").send_keys("demo-tt1@inet-yar.ru")
    time.sleep(2)

    # Ввод пароля(указан на прямую в коде)
    driver.find_element(by=By.CSS_SELECTOR, value="#login-password").send_keys("rNCV14la")
    time.sleep(3)

    # Предупреждение пользователя
    print("Решите reCAPTCHA, у Вас есть 60 секунд!\nВход произойдёт автоматически.")
    time.sleep(60)

    # Нажатие на кнопку "Войти" в форме
    driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div/div[2]/form/div[7]/button").click()
    time.sleep(5)

    # Получение данных из таблицы
    IP_port_first = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[2]/table/tbody/tr["
                                                  "2]/td[3]/ul/li[1]/div[2]/b").text
    time.sleep(2)
    IP_port_second = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[2]/table/tbody/tr["
                                                   "3]/td[3]/ul/li[1]/div[2]/b").text
    time.sleep(2)
    expiration_date_first = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div["
                                                          "2]/table/tbody/tr[2]/td[3]/ul/li[6]/div[2]").text
    time.sleep(2)
    expiration_date_second = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div["
                                                           "2]/table/tbody/tr[3]/td[3]/ul/li[6]/div[2]").text
    time.sleep(2)

    # Вывод данных
    print(IP_port_first, "-", expiration_date_first)
    print(IP_port_second, "-", expiration_date_second)
    time.sleep(5)


except Exception as ex:
    # Вывод о состояний
    print(ex)
finally:
    driver.close()  # Закрыть текущее существующее окно
    driver.quit()  # Закрыть окно экземпляра веб-драйвера
