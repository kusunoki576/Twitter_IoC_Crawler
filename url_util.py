from typing import List
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options

from re_util import extract_hash



def get_web_text(url: str) -> str:
    try:
        re = requests.get(url, timeout=(3.0, 7.5))
    except Exception as ex:
        return str(ex)

    user_agent = 'Chrome/100.0.4896.127'
    options = Options() # webdriver.chrome.options
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument(f'--user-agent={user_agent}')
    chrome_service = service.Service(executable_path='YOUR PATH')
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.set_page_load_timeout(10)
    driver.get(url)
    result = driver.page_source.encode('utf-8')
    driver.quit()
    soup=BeautifulSoup(result,"html.parser")

    return soup.get_text(" ")


def extract_hash_from_urls(urls: List[str]) -> List[str]:
    web_texts:List[str] = []
    for url in urls:
        web_texts.append(get_web_text(url))
    
    hashes:List[str] = []
    for web_text in web_texts:
        hashes.extend(extract_hash(web_text))

    return hashes   