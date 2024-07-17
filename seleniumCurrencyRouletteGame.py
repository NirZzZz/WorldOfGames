from selenium import webdriver
import random

difficulty = int(input("Please choose a difficulty level for the CurrencyRoulette game: "))


def get_money_interval(driver, generated_number, _difficulty):
    url = ('https://www.google.com/search?q=usd+to+ils&oq=usd'
           '+to+ils&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDIyNzdqMG'
           'o3qAIAsAIA&sourceid=chrome&ie=UTF-8')
    xpath_usd = '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/div/div[1]/input'
    xpath_ils = '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/div/div[2]/input'
    driver.get(url)
    usd_box = driver.find_element(by="xpath", value=xpath_usd)
    usd_box.clear()
    usd_box.send_keys("1")
    ils_box = driver.find_element(by="xpath", value=xpath_ils)
    conversion_rate = float(ils_box.get_attribute("value"))
    total = (generated_number * conversion_rate)
    upper_bound = (total + (5 - _difficulty))
    lower_bound = (total - (5 - _difficulty))
    return upper_bound, lower_bound


def get_guess_from_user():
    generated_number = random.randint(1, 101)
    print(f"{generated_number} USD")
    guess = float(input('guess how much is it in ILS: '))
    return guess, generated_number


def play():
    guess, generated_number = get_guess_from_user()
    driver = webdriver.Chrome()
    upper_bound, lower_bound = get_money_interval(driver, generated_number, difficulty)
    if upper_bound >= guess >= lower_bound:
        print("good")
        return True
    else:
        print("bad")
        return False


play()
