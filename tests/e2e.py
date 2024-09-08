from selenium import webdriver
from selenium.webdriver.common.by import By
url = "http://127.0.0.1:5000"


def test_scores_service(app_url):
    driver = webdriver.Chrome()
    name = ""
    try:
        driver.get(app_url)
        success = True
        score_element = driver.find_elements(By.XPATH, "//body//ul//li")
        for i in score_element:
            text = i.text.split(": ")
            name = text[0]
            score = int(text[1])
            if not 1 < score < 1000:
                success = False
                break
        return success
    except Exception as e:
        print(f"An error occurred: {e} in {name}")
        return False
    finally:
        # Close the browser
        driver.quit()


def main_function():
    result = test_scores_service()
    if result:
        return 0
    else:
        return -1
