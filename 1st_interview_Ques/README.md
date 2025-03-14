# 🚀 WeChat Article Scraping System

This project is based on **Selenium + BeautifulSoup**, enabling automatic crawling of the title and content from the provided WeChat article URLs.

## 📌 **Features**
✅ Crawl the content from the input WeChat article URLs

# Environment Setup (Compatible with Windows & macOS)

📌 **ChromeDriver Configuration Guide**

Since ChromeDriver must match the Google Chrome version and installation methods differ across operating systems (Windows/macOS/Linux), this guide explains how to install, configure, and modify the ChromeDriver path in the code.

📌 **What is ChromeDriver?**
- ChromeDriver is required for Selenium to control Google Chrome.
- The ChromeDriver version **must match** the Google Chrome version; otherwise, errors like `SessionNotCreatedException` may occur.

📌 **Installation Guide for Windows & macOS**

1️⃣ **Check Chrome Version**  
Before installing ChromeDriver, check your Google Chrome version:  
- **Windows:**  
  Enter `chrome://version/` in the Chrome address bar.  
  Example output: `Google Chrome 123.0.6312.86`  
- **macOS:**  
  Run in Terminal:  
  ```sh
  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
  ```

2️⃣ **Download ChromeDriver**  
- **Windows:** Use `webdriver-manager` for automatic installation:  
  ```sh
  pip install webdriver-manager
  ```  
- **macOS:** Install via Homebrew:  
  ```sh
  brew install chromedriver
  ```

3️⃣ **Find ChromeDriver Path**  
- **Windows:**  
  ```sh
  where chromedriver
  ```  
- **macOS:**  
  ```sh
  which chromedriver
  ```  

# Required Python Packages  

```sh
pip install selenium beautifulsoup4 requests pandas webdriver-manager
```

| Dependency        | Purpose                                      |  
|------------------|---------------------------------------------|  
| selenium         | Automates browser interactions for web scraping |  
| beautifulsoup4   | Parses HTML structure to extract information |  
| requests         | Sends HTTP requests (for pages accessible via requests) |  
| pandas          | Handles CSV data storage and management |  
| webdriver-manager | Manages ChromeDriver installation automatically |  

---

# 🚀 How to Run  

1️⃣ **Add the WeChat article URLs**  
   - Modify the `url-list` variable to include the WeChat article URLs you want to scrape.  

2️⃣ **Run the script**  
   ```sh
   python get_article.py
   ```  
   (or run it directly in your preferred code editor)

---

# 💰 Output
Each scraped article will be saved as a `.txt` file, named after the corresponding article title. The file will contain the full article text and be stored in the same directory.

---

# 📌 Contribution & Open Source  

💡 **Contributions Welcome!**  
   - Found a bug? Submit an **Issue**  
   - Want to improve the project? **Fork & submit a PR**  

📜 **License:** MIT.

