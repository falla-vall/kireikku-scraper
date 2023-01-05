import undetected_chromedriver as uc

from typing import Union

from bs4 import BeautifulSoup
from fastapi import APIRouter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from app.models.schemas.scraper import ScraperUrl

def scrap_url(url: str, css_selector: Union[str, None] = None ) -> ScraperUrl:
    try:
        driver = uc.Chrome()
        driver.get(url)
        if css_selector:
            wait = WebDriverWait(driver, 10)
            passed_page = wait.until(
                EC.visibility_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        css_selector,
                    )
                )
            )
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        prettied = soup.prettify()
        return {
            "is_success": True,
            "data": prettied
        }
    except TimeoutException:
        return {
            "is_success": False,
            "error": "Timeout: Retrieving url took too long"
        }
    except BaseException as e:
        return {
            "is_success": False,
            "error": "An exception occurred: {}".format(e)
        }

