from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = "/your/path/to/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


url_list = [
    "https://mp.weixin.qq.com/s/hP9CaBIpOjRr0YVacpZYpQ",
    "https://mp.weixin.qq.com/s/RaoD_j451_aAztDzHfFzqA",
    "https://mp.weixin.qq.com/s/mOyUy7oGNa3lux9pgnAfRg",
    "https://mp.weixin.qq.com/s/TxBhDL2zvHrDbWwx05CmVw",
    "https://mp.weixin.qq.com/s/dz-smznEKTu27DqUX-8mzw",
    "https://mp.weixin.qq.com/s/bFyW0Vqj-FHyxTJ3FtoUsg"
]

for url in url_list:
    driver.get(url)
    time.sleep(3)

    try:
        title = driver.find_element(By.TAG_NAME, "h1").text.strip()
        content = driver.find_element(By.CLASS_NAME, "rich_media_content").text.strip()

        file_name = title.replace(" ", "_") + ".txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"{title}\n\n{content}")

        print(f"文章已保存为 {file_name}")
        
    except Exception as e:
        print(f"爬取失败: {url}, 错误: {e}")


driver.quit()