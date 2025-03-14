# 🚀 Teacher Information Crawling System

This project is based on **Selenium + BeautifulSoup**, enabling automatic crawling of teacher information, including name, title, research field, contact details, etc., and storing the data in a CSV file.

## 💰 Updates
- **March 12, 2025, 12:10** >>> Added the HTML code of the main webpage of Chang'an University, the HTML code of the Faculty of Highway Teachers Information Database, and the HTML code of an individual teacher's homepage for users to analyze the website structure.
- **March 13, 2025, 9:09** >>> Modified the crawling logic function in `get_detail.py`, changing `soup_select_one` in the `get_text` function to `soup_select` to obtain all information under the entry.
- **March 14, 2025, 10:44** >>>Now available: Automatic breakpoint resumption, just run again to automatically read the last breakpoint and restart the crawl. Optimization: Change the append mode to create and initialize the column name when the output file does not exist

## 📌 **Features**
✅ **Automatically retrieve faculty homepage URLs** (crawled from the main website)  
✅ **Crawl all teacher homepages within faculties** (supports pagination)  
✅ **Extract detailed information from each teacher's homepage** (name, title, research direction, etc.)  
✅ **Save data to CSV with resume capability** (prevents overwriting existing data)  

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

### 1️⃣ Retrieve Faculty Homepage URLs  
Run the following command:  
```sh
python get_academies_url.py
```  
💡 **This script will:**  
   - Crawl the main website to extract URLs for faculty homepages  
   - Save them to `academies.db`  

### 2️⃣ Crawl Teacher Lists & Homepages  
Run the following command:  
```sh
python get_teachers_url.py
```  
💡 **This script will:**  
   - Read `academies.db` to get all faculty homepage URLs  
   - Extract teacher names, titles, and personal homepage URLs  
   - Store data in `teachers_data.csv`  

### 3️⃣ Extract Detailed Teacher Information  
Run the following command:  
```sh
python get_detail.py
```  
💡 **This script will:**  
   - Read `teachers_data.csv` to get teacher homepage URLs  
   - Access each teacher’s homepage to scrape detailed information (name, title, research field, publications, etc.)  
   - Save the extracted data to `teacher_details.csv`  

---

# 🔄 Resume Crawling  

If you want to resume crawling from a specific teacher, modify `get_detail.py`:  

```python
start_index = 100  # Start from the 101st record
```

💡 This allows you to continue scraping from a specific row without overwriting existing data!  

---

# 📊 Data Storage  

| Filename         | Data Content |  
|-----------------|--------------|  
| academies.db    | Faculty homepage URLs |  
| teachers_data.csv | Teacher names, titles, and homepage URLs |  
| teacher_details.csv | Detailed teacher information (name, title, research fields, publications, etc.) |  

---

# 📌 Contribution & Open Source  

💡 **Contributions Welcome!**  
   - Found a bug? Submit an **Issue**  
   - Want to improve the project? **Fork & submit a PR**  

📜 **License:** MIT.

