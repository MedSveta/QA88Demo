import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def hide_footer(driver):
    driver.execute_script("document.querySelector('footer').style.display='none'")


def scroll_down(self, steps: int = 10, pixels: int = 500, pause: float = 0.5) -> None:
    for _ in range(steps):
        ActionChains(self.driver).scroll_by_amount(0, pixels).perform()
        time.sleep(pause)

class TestSelectorsCss:
    def test_selectors_css(self, driver):
        time.sleep(2)
        # поиск по имени элемента By.TAG_NAME
        footer = driver.find_element(By.TAG_NAME, "footer")
        print(footer.tag_name)

        # поиск по имени элемента и его аттрибуту By.CSS_SELECTOR
        tools = driver.find_element(By.CSS_SELECTOR, "img[src='/assets/Toolsqa-DZdwt2ul.jpg']")
        print(tools.get_attribute('src'))

        driver.find_element(By.CSS_SELECTOR, "a[href='/elements']").click()
        time.sleep(2)

        driver.back()
        # по аттрибуту
        driver.find_element(By.CSS_SELECTOR, "[href='/elements']").click()
        time.sleep(2)

        # поиск по ID By.ID
        #driver.find_element(By.ID, "item-0").click()
        # driver.back()
        # поиск по CSS id через сокращенную запись #
        #driver.find_element(By.CSS_SELECTOR, "#item-0").click()
        # driver.find_element(By.CSS_SELECTOR, "li#item-0").click()
        # "item-0"
        # "#item-0"
        # "li#item-0"
        # "li[id='item-0']"
        # "[id='item-0']"
        # driver.back()

        # поиск по классу
        driver.find_element(By.CSS_SELECTOR, "a[class='router-link']").click()
        time.sleep(2)

        driver.back()

        driver.find_element(By.CSS_SELECTOR, "[class='router-link']").click()
        time.sleep(2)

        driver.back()
        driver.find_element(By.CLASS_NAME, "router-link").click()
        #driver.find_element(By.CLASS_NAME, "btn btn-light ").click() не правильно!! 2 класса
        #driver.find_element(By.CLASS_NAME, "btn").click()  правильно!! 1 класс
        time.sleep(2)

        driver.back()
        # поиск по Css по классу сокращенная форма записи '.'
        driver.find_element(By.CSS_SELECTOR, ".router-link").click()
        # "router-link"  By.CLASS_NAME
        # ".router-link" By.CSS_SELECTOR через сокращенную форму '.'
        # "a.router-link" By.CSS_SELECTOR tagname и через сокращенную форму '.'
        # "a[class='router-link']" By.CSS_SELECTOR  по  tagname и по аттрибуту
        # "[class='router-link']" By.CSS_SELECTOR  по аттрибуту
        time.sleep(2)

        # input#userName.mr-sm-2.form-control
        driver.find_element(By.CSS_SELECTOR, "input#userName.mr-sm-2.form-control").send_keys("Sveta")
        time.sleep(2)
        driver.back()

        # "div.element-list li:nth-child(5) a"        поиск по пятому ребенку у div
        driver.find_element(By.CSS_SELECTOR, "div.element-list li:nth-child(5) a").click()
        time.sleep(2)
        hide_footer(driver)
        scroll_down(driver)

        driver.find_element(By.CSS_SELECTOR, "div.element-list li:last-child a").click()
        time.sleep(2)
















