import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# ChromeDriver 环境配置 路径 ，更换为你的chromedriver路径
chrome_driver_path = "/your/path/to/chromedriver"

# 读取教师个人主页URL文件
input_csv = "teachers_data.csv"
output_csv = "teacher_details.csv"

# 针对上一次IP封禁，从第几条数据开始爬取，默认为从0开始爬取（索引从 0 开始，第一条数据是 0，第二条是 1，以此类推）
start_index = 1268  

# Selenium 工具包配置
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 无头模式
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# 启动 WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 读取教师主页 URL，从 `start_index` 开始
teacher_urls = []
with open(input_csv, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # 跳过表头
    teacher_urls = [row[1] for i, row in enumerate(reader) if i >= start_index]  # 只读取指定位置后的数据

print(f"从第 {start_index + 1} 条数据开始爬取，共 {len(teacher_urls)} 条数据。")

# 追加模式写入 CSV，不覆盖已有数据，方便在IP封禁后手动更换IP并进行
with open(output_csv, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

# 爬取每个教师主页
counter = 0
for url in teacher_urls:
    print(f"正在爬取: {url}")

    # 随机延迟
    time.sleep(random.uniform(1, 2))

    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "news_title"))
        )
    except Exception as e:
        print(f"跳过 {url}，发生错误: {e}")
        continue  # 跳过错误页面，继续爬取

    #  使用beautifulsoup工具包 解析 HTML
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 提取信息
    def get_text(selector):
        elements = soup.select(selector)
        return "\n".join([e.text.strip() for e in elements]) if elements else "无"

    # 基本信息
    name = get_text(".news_title")
    title = get_text(".tip0")
    college = get_text(".tip1")
    gender = get_text("li:-soup-contains('性别') .txt")
    birth_date = get_text("li:-soup-contains('出生年月') .txt")
    degree = get_text("li:-soup-contains('学位') .txt")
    education = get_text("li:-soup-contains('学历') .txt")
    university = get_text("li:-soup-contains('毕业院校') .txt")
    phone = get_text("li:-soup-contains('联系电话') .txt")
    email = get_text("li:-soup-contains('电子邮箱') .txt")
    address = get_text("li:-soup-contains('通讯地址') .txt")

    # 详细信息
    research_area = get_text(".maincon:has(h3:-soup-contains('研究领域')) .con p")
    courses = get_text(".maincon:has(h3:-soup-contains('开授课程')) .con p")
    projects = get_text(".maincon:has(h3:-soup-contains('科研项目')) .con p")
    papers = get_text(".maincon:has(h3:-soup-contains('论文')) .con p")
    awards = get_text(".maincon:has(h3:-soup-contains('荣誉奖励')) .con p")
    work_experience = get_text(".maincon:has(h3:-soup-contains('工作经历')) .con p")

    # 追加数据到 CSV
    with open(output_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, title, college, gender, birth_date, degree, education,
                         university, phone, email, address, research_area, courses, 
                         projects, papers, awards, work_experience, url])

    print(f"成功爬取: {name}")

    # 每 50 次重启 Selenium ，释放内存提高效率
    counter += 1
    if counter % 50 == 0:
        print("重启 Selenium 以释放资源...")
        driver.quit()
        driver = webdriver.Chrome(service=service, options=options)

# 关闭浏览器
driver.quit()
print("\n所有教师信息已追加到 `teacher_details.csv`！")

# 当爬取过程遇到大量报错时为IP连续访问被封禁，结束进程，更换IP ，并从上次中断的地方开始爬取