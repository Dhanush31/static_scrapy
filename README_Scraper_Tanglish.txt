
# 🧾 Web Scraping with Pagination (Tanglish Explanation)

## 📁 File Name: satic_main.py

### Overview:
This Python script scrapes data from multiple pages of a website using BeautifulSoup, requests, and pandas.

---

## 1️⃣ Import Statements

```python
import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
```

**Explanation:**
- `argparse` → Command line la input edukka use pannrom (like --url).
- `requests` → Webpage HTML download panna use agum.
- `BeautifulSoup` → HTML content la iruka data extract panna use agum.
- `pandas` → DataFrame create panni CSV la save panna use agum.
- `urljoin` → Base URL + relative path combine panna use agum.

---

## 2️⃣ Argument Parser Setup

```python
parser=argparse.ArgumentParser(description="scraping")
parser.add_argument("--url",required=True,help="enter the url ⛓️ ")
args=parser.parse_args()
```

**Explanation:**
- User la irundhu URL input edukka use agum.
- Example: `python satic_main.py --url https://quotes.toscrape.com/page/1/`
- `args.url` → Ithu command line la kudutha URL store pannum.

---

## 3️⃣ Initial Setup

```python
page_url="/pages/"
all_data=[]
url=args.url
```

**Explanation:**
- `all_data` → Empty list for storing scraped data.
- `url=args.url` → Starting page URL from user input.

---

## 4️⃣ While Loop

```python
while True:
```

**Explanation:**
- Infinite loop start agum.
- `break` varum varai run agum (till last page).

---

## 5️⃣ Request and Response Check

```python
response=requests.get(url)
if response.status_code!=200:
    print(f"webpage not respond--->>{response.status_code}")
    break
```

**Explanation:**
- Webpage request send pannum.
- If 200 illa (error), break pannum.

---

## 6️⃣ Parse HTML Content

```python
soup=BeautifulSoup(response.text,"html.parser")
```

**Explanation:**
- HTML content parse panna use agum for easy tag search.

---

## 7️⃣ Find All HTML Tags

```python
all_text=soup.find_all(True)
```

**Explanation:**
- `find_all(True)` → all HTML tags extract pannum (`div`, `p`, `span`, etc.).

---

## 8️⃣ Extract Tag Details

```python
for tag in all_text:
    tag_name=tag.name
    tag_text=tag.get_text(separator='/n',strip=True)
    all_data.append({"url":url,"tag":tag_name,"text":tag_text})
```

**Explanation:**
- `tag.name` → HTML tag name.
- `tag.get_text()` → Inside text clean ah edukum.
- Append data to list as dictionary.

---

## 9️⃣ Next Page Detection

```python
next_button=soup.find("li",class_="next")
```

**Explanation:**
- `next_button` la next page link iruka nu check pannum.

---

## 🔟 Move to Next Page

```python
if next_button and next_button.find("a"):
    next_link=next_button.find('a')["href"]
    url=urljoin(url,next_link)
else:
    break
```

**Explanation:**
- If next page link found → update URL → continue loop.
- Illana (last page reached) → break.

---

## 1️⃣1️⃣ Save to CSV

```python
df=pd.DataFrame(all_data)
df.to_csv("static_data.csv",index=False)
print("sucsussfully done")
```

**Explanation:**
- List of dictionaries convert to DataFrame.
- Save to `static_data.csv` file.

---

## ✅ Summary Flow

```
Start → Get Page → Extract Tags → Find Next → Go Next Page → Save Data → Done ✅
```

---

## 🧩 Output Example

| url | tag | text |
|-----|-----|------|
| https://quotes.toscrape.com/page/1/ | span | “The world as we have created it is a process of our thinking.” |
| https://quotes.toscrape.com/page/2/ | small | “Albert Einstein” |

---

💡 **Tip:** You can modify the `find_all()` or `get_text()` logic to collect only specific tags (like `h1`, `p`, etc.) for more focused scraping.

