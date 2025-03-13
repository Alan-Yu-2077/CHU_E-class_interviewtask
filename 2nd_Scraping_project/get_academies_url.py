import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# ChromeDriver 路径
chrome_driver_path = "/your/path/to/chromedriver"

# **目标主网站**
main_url = "https://js.chd.edu.cn/"

# **Selenium 配置**
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 无头模式
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# **启动 WebDriver**
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# **访问主网站**
driver.get(main_url)

# **等待学院数据加载**
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "deptLists_w14"))  # 确保学院列表加载完毕
    )
    print("学院数据已加载！")
except:
    print("超时：学院数据未加载")
    driver.quit()
    exit()

# **解析页面数据**
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# **查找学院列表**
academy_list = soup.select("#deptLists_w14 li a")

# **数据库存储**
conn = sqlite3.connect("academies.db")
cursor = conn.cursor()

# **创建表格（如果不存在）**
cursor.execute('''
    CREATE TABLE IF NOT EXISTS academies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        url TEXT
    )
''')

# **插入数据**
for academy in academy_list:
    name = academy.get_text(strip=True)
    url = academy["href"].strip()

    # **拼接完整 URL**
    if not url.startswith("http"):
        url = main_url.rstrip("/") + "/" + url.lstrip("/")

    cursor.execute("INSERT INTO academies (name, url) VALUES (?, ?)", (name, url))
    print(f"已添加学院: {name} - {url}")

# **提交更改并关闭数据库**
conn.commit()
conn.close()

print("\n所有学院数据已存入 academies.db 数据库！")