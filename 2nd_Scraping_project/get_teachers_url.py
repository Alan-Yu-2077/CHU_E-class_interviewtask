import sqlite3
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# ChromeDriver 路径
chrome_driver_path = "/your/path/to/chromedriver"

# 从 SQLite 读取所有学院 URL
def get_academy_urls():
    conn = sqlite3.connect("academies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM academies")
    urls = [row[0] for row in cursor.fetchall()]
    conn.close()
    return urls

# Selenium 配置
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 无头模式
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# **启动 WebDriver**
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# **CSV 文件路径**
csv_filename = "teachers_data.csv"

# **初始化 CSV 文件（写入表头）**
with open(csv_filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["教师信息", "个人主页"])  # 写入表头

# **获取学院 URL**
urls = get_academy_urls()
print(f"从数据库读取 {len(urls)} 个学院的 URL。")

# **爬取多个学院的教师信息**
all_teachers = []

for url in urls:
    print(f"\n正在爬取: {url}")
    
    driver.get(url)

    # **等待教师数据加载**
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "searchTea"))
        )
        print("教师数据已加载！")
    except:
        print("超时：教师数据未加载")
        continue  # 继续下一个 URL

    # **解析页面数据**
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # **查找教师列表**
    teacher_list = soup.select("#searchTea li")

    # **提取并整理数据**
    for teacher in teacher_list:
        text = teacher.get_text(strip=True)

        # **获取教师个人主页链接**
        link_tag = teacher.find("a")
        if link_tag and "href" in link_tag.attrs:
            link = link_tag["href"].strip()
            if not link.startswith("http"):
                link = url.rstrip("/") + "/" + link.lstrip("/")
        else:
            link = "无主页"

        all_teachers.append([text, link])

# **写入 CSV 文件**
with open(csv_filename, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(all_teachers)

print(f"\n所有数据已写入 {csv_filename}")

# **关闭 Selenium**
driver.quit()