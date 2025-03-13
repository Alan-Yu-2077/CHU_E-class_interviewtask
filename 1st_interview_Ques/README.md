# 🚀 教师信息爬取系统

本项目基于 **Selenium + BeautifulSoup** 实现，能够自动爬取输入的公众号文章的url内的标题与内容
## 📌 **功能**
✅ 对输入的公众号Url进行内容爬取


# 环境配置 **Windows 和 macOS 通用
📌 ChromeDriver 配置完整指南

由于 ChromeDriver 版本与 Google Chrome 浏览器 需要匹配，且不同操作系统（Windows/macOS/Linux）的安装方式不同，我们需要详细讲解 如何安装、配置和在代码中修改 ChromeDriver 路径。

📌 什么是 ChromeDriver？
	•	ChromeDriver 是 Selenium 控制 Google Chrome 所需的驱动程序。
	•	你必须确保 ChromeDriver 版本 和 Google Chrome 版本 一致，否则可能会报错 SessionNotCreatedException。

📌 Windows & macOS 的安装方法

1️⃣ 检查 Chrome 版本
在安装 ChromeDriver 之前，先检查你的 Google Chrome 版本：
	•	Windows：
        在 Chrome 地址栏输入： chrome://version/
        你会看到类似：
        Google Chrome 版本 123.0.6312.86
	•	macOS：
        /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version

2️⃣ 下载 ChromeDriver

//windows：
    直接使用 webdriver-manager 自动安装适配版本：pip install webdriver-manager
//mac：
    在终端使用 brew install chromedriver

查找自己的chromdriver路径，后续修改代码：
//windows：
    where chromedriver
//mac：
    which chromedriver

# 运行程序需要下载的python工具包：
  pip install selenium beautifulsoup4 requests pandas webdriver-manager
  依赖包	        作用
selenium	       控制浏览器，用于自动化爬取网页数据
beautifulsoup4	   解析 HTML 结构，提取网页中的信息
requests	       发送 HTTP 请求，如果部分页面可以用 requests 直接访问
pandas	           处理 CSV 数据，存储和管理爬取的数据
webdriver-manager  自动下载和管理 ChromeDriver，避免手动安装

# 🚀 如何运行
 在url-list变量中添加自己想爬取的公众号url
 python get_article.py (或者直接在编译平台运行该文件)

# 💰 你将获得
以你提供的公众号url对应的公众号文章标题命名的txt文件，文件内包含该文章的文本内容
文件将直接储存于该文件夹分支内


# 📌贡献 & 开源

💡 欢迎参与贡献！
	•	如果发现问题，请提交 Issue
	•	你可以 Fork 项目并提交 PR

📜 License: MIT