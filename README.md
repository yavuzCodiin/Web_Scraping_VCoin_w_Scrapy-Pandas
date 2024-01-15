# <ins>Web_Scraping_VCoin_w_Scrapy-Pandas</ins>

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/dd59eaf7-f44c-4b3d-beb8-bf270d30b4aa)

As an enthusiastic collector of antique coins, I have always been fascinated by the rich history each piece embodies. These coins are not only currency, but also links to our past. Some may have been used in times of war, others for everyday transactions like buying food, book, clothes or acquiring a new home. Each coin holds a story, a glimpse into the lives and times of those who once held them.

This is Part IV on Web Scraping if you want to see the first three here are links:
* [Web_Scraping_IMDB_Most_Popular_Movies](https://github.com/yavuzCodiin/Web_Scraping_IMDB_Most_Popular_Movies)
* [Web_Scraping_X_Feed_Selenium](https://github.com/yavuzCodiin/Web_Scraping_X_Feed_Selenium)
* [Web_Scraping_Practice_w_Instagram_and_GitHub](https://github.com/yavuzCodiin/Web_Scraping_Practice_w_Instagram_and_GitHub)

## <ins>Virtual Environment</ins>

### <ins>Pip Installation</ins>
```python
python get-pip.py
```
### <ins>Add Python to Path</ins>
You need to find your python executable location to add it to Path generally you can find it under C:\Python it is going to look like this:
```plain
C:\Users\USER\AppData\Local\Programs\Python
```
then you need to add find Edit the system environment variables click on Environment Variables and add this path to there.

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/b8d7cb07-54c5-4317-9b38-7f51dab9fe8f)

### <ins>Creating Virtual Environment</ins>
```python
python -m venv venv
```
When you create venv named virtual environment you will find Scripts folder in it and inside it there is file called activate this is batch file we will activate our environment with this

### <ins>Activating venv</ins>
```python
venv\Scripts\activate
```
Now we are ready to use our virtual environment.

If you face with “Execution_Policies” problem, you can run the following script on powershell:
```python
Set-ExecutionPolicy RemoteSigned
```
### <ins>Installing packages into venv</ins>
```python
python -m pip install "package-name"
```
That’s it we can install any package we want with any version we need without making our environment messier, or dealing with issues problems because of all other modules in the same environment etc.
### <ins>Deactivating venv</ins>
```python
deactivate
```
When we are done, we can simply close our virtual environment with deactivate.

You can check this documentation for more: [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html#)

Let’s install our packages:
```python
pip install Scrapy
pip install pandas
pip install numpy
```
## <ins>What is Scrapy?</ins>
Scrapy is a simply high-level web crawling and scraping framework that helps us to extract structured data from websites. It can be used for various purposes, including data mining, monitoring, and automated testing.

Documentation => [Scrapy 2.11 documentation — Scrapy 2.11.0 documentation](https://docs.scrapy.org/en/latest/#)

### <ins>Starting Project</ins>
```python
scrapy startproject "project_name"
```
![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/7017325c-7360-432c-9b17-42ed01d3f7f0)

After we started our project, our folder has files like settings.py where you can configure your spider settings, items.py, pipelines.py etc. and the most important one is spiders folder we will configure our spider and it will do what we ask for we can create different spiders for different jobs. To begin with I suggest you to check the documentation above it really helps for you to understand what’s going on.
```python
from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
```
You can find examples like this in the documentation, spider structure looks like this, the important thing is name must be unique you will use spider’s name to crawl data.

There is shortcut to start_requests method:
```python
from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
```
### <ins>Crawling with Scrapy</ins>
```python
scrapy crawl quotes #quetos spider will get into action

scrapy crawl quotes -o quotes.json #with this you can save data into json format
```
### <ins>Crawling via Scrapy Shell</ins>
```python
scrapy shell "url" #with this you can directly get the data to analyze in the shell
```
* from scrapy shell you can directly analyze to see output
```python
response.css("title::text").get()
# Output: 
'Quotes to Scrape'
```
That’s it for now for more information you can check documentation I gave above it is enough for you to understand deeper.

## <ins>What is Pandas?</ins>
Pandas is an open-source Python library that has changed the game in data analysis and manipulation. Think of pandas as Swiss Army knife. It’s powerful yet user-friendly, complex yet approachable, and it’s the tool for anyone looking to make sense of data.

With pandas, tasks like reading data from various sources, cleaning it to a usable format, exploring it to find trends, and even visualizing it for presentations are simplified.

Why pandas? Because it streamlines complex processes into one or two lines of code — processes that otherwise would have taken countless steps in traditional programming languages. It’s especially popular in academic research, finance, and commercial data analytics because of its ability to handle large datasets efficiently and intuitively.

### <ins>Installation</ins>

```python
pip install pandas
```
### <ins>Example from pandas documentation</ins>
```python
import pandas as pd
import numpy as np

df_exe = pd.DataFrame(
    {
        "One": 1.0,
        "Time data": pd.Timestamp("20130102"),
        "Series": pd.Series(1, index=list(range(4)), dtype="float32"),
        "Numpy Array": np.array([3] * 4, dtype="int32"),
        "Catalog": pd.Categorical(["Chair", "Tv", "Mirror", "Sofa"]),
        "F": "example",
    }
)

df_exe
```

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/46670c51-ce39-47d4-bd64-349ad91377e4)

```python
df_exe[df_exe["Catalog"]=="Mirror"]
```

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/d00b3281-0155-43bd-beb6-0f4764befa3e)

We will explore more with the project so for now we are done with it for detailed information you can check [pandas documentation](https://pandas.pydata.org/docs/index.html).

## <ins>Project Vcoin</ins>

### <ins>|Part 1: Getting the Data</ins>

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/59169b96-a037-4162-9b76-e6e755cfb925)

When I check the website I see the structure is like this and I decided to get the seller name, money, and price of it so I checked its html structure to see what to extract.

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/c76d2665-6ef7-40a2-8e15-72d8ab3bff68)

```python
scrapy shell "https://www.vcoins.com/en/coins/world-1945.aspx"
```

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/d2a7660c-0ec9-4b94-922c-826667c8eb64)

```python
response.css("div.item-link a::text").extract()
```

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/4ed5df42-0014-4561-a11b-3ef5fb83b584)

```python
response.css("p.description a::text").extract()
```
![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/87a751f0-e6a6-4b3b-8b1c-d22269668447)

```python
response.css("div.prices span.newitemsprice::text").extract()[::2]
```

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/a6779bbf-58f1-4c04-8855-4b14bc98dbfe)

```python
response.css("div.prices span.newitemsprice::text").extract()[1::2]
```

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/d06eaea9-ab5f-44ac-a07a-4cedfea3d53c)

These are data of one page, and I want my spider to search all the pages available and return the data so I will check pagination part on the bottom.

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/9dc6f485-66f4-44c0-9e4e-85b37dc3e391)

It will go until there is nothing. I first done this project with getting text output, then for csv(comma separated values) output for data analysis.

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/7f5875ae-942f-4a7f-9bd3-82e9e9fcb47b)

### <ins>| Importing Libraries</ins>
```python
import scrapy  # Import the scrapy library
import csv  # Import the csv library
```

### <ins>| __init__</ins>
```python
# Define a new spider class which inherits from scrapy.Spider.
class MoneySpider(scrapy.Spider):
    name = "moneyspider_csv"
    page_count = 0  
    money_count = 1 
    start_urls = ["https://www.vcoins.com/en/coins/world-1945.aspx"]
```

### <ins>| Start_request</ins>
```python
def start_requests(self):
        self.file = open('money.csv', 'w', newline='', encoding='UTF-8')  # Open a new CSV file in write mode.
        self.writer = csv.writer(self.file)  # Create a CSV writer object.
        self.writer.writerow(['Count', 'Seller', 'Money', 'Price'])  # Write the header row in the CSV file.
        return [scrapy.Request(url=url) for url in self.start_urls]  # Return a list of scrapy.Request objects for each URL.
```

### <ins>| parse</ins>
```python
    # This method processes the response from each URL
    def parse(self, response):
        # Extract the names
        money_names = response.css("div.item-link a::text").extract()
        # Extract the years
        money_years = response.css("p.description a::text").extract()
        # Extract the currency symbols
        money_symbols = response.css("div.prices span.newitemsprice::text").extract()[::2]
        # Extract the prices
        money_prices = response.css("div.prices span.newitemsprice::text").extract()[1::2]
        # Combine the currency symbols and prices
        combined_prices = [money_symbols[i] + money_prices[i] for i in range(len(money_prices))]
```

### <ins>| </ins>
```python
        # Loop through the extracted items and write each to a row in the CSV file.
        for i in range(len(money_names)):
            self.writer.writerow([self.money_count, money_names[i], money_years[i], combined_prices[i]])
            self.money_count += 1
```
```python
    # Extract the URL for the next page
        next_page_url = response.css("div.pagination a::attr(href)").extract_first()
        # If there is a URL for the next page, construct the full URL and continue scraping.
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            self.page_count += 1

            if self.page_count != 10:
                yield scrapy.Request(url=absolute_next_page_url, callback=self.parse, dont_filter=True)
            else:
                self.file.close()
```

### <ins>| Output</ins>

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/253e1713-3d4d-423d-a31c-95ba8ecf4a2d)

### <ins>|Part 2: Data Analysis</ins>
We successfully extracted the csv data, now it is time for us to analyze.

```python
import pandas as pd
import numpy as np

test = pd.read_csv("money.csv",index_col="Count")
test
```

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/b506f5a5-eb1b-4efb-9faa-17906dafbbd2)


```python
test.shape
test.info()
test.describe()
```
![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/a3f76669-3f46-4722-b88b-8915ff753654)


```python
test.isnull().sum()
```
![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/760ceaa1-4c73-4a0a-8681-a8c846709cb2)


```python
test.drop_duplicates().sort_values(by="Price",ascending=False).head(25)
```

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/7d0b3c9f-8a9c-4f37-b015-448abbfd5788)


```python
# Regular expression(Regex) pattern to match 2, 3, or 4 consecutive digits.
pattern = r'(\b\d{4}\b|\b\d{3}\b|\b\d{2}\b)'

test['Extracted_Year'] = test['Money'].str.extract(pattern, expand=False)

test['Extracted_Year'] = pd.to_numeric(test['Extracted_Year'], errors='coerce').fillna(-1).astype(int)

test.drop_duplicates().sort_values(by='Extracted_Year',ascending=False).head(60)
```
![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/878b8464-641c-4ff6-be5e-92cea3b696aa)


```python
def clean_price(price):
    price = price.replace('US$', '').replace('€', '').replace('£', '').replace('NOK', '')
    price = price.replace(',', '').replace('.', '')
    price = price.strip()
    return price

# Apply the cleaning function to Price Column
test['Price'] = test['Price'].apply(clean_price)
test['Price'] = pd.to_numeric(test['Price'], errors='coerce')
test[["Money", "Price"]].drop_duplicates().sort_values(by="Price", ascending=False).head(40)
```
* This is not correct thing to do but I wanted to show you clean process I haven’t decide how to correctly sort my values because there are different currencies.

![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/da21cb14-108c-418d-8141-c0bb1355f483)

```python
test[test["Money"].apply(lambda x : x.startswith("Elizabeth"))]

test[test["Seller"].apply(lambda x : x.startswith("Sovereign"))]
```
![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/7fcfa411-759f-42eb-96ce-d7b912dcb69b)

```python
test[test["Money"].isin(["Elizabeth II 1966 Gillick Sovereign MS64"])]
```
![image](https://github.com/yavuzCodiin/Web_Scraping_VCoin_w_Scrapy-Pandas/assets/82445309/c467532c-683f-4d34-9ed8-71fa7e3c7220)

If you want to understand this in a more simpler language you can check my Medium writing published on `Level Up Coding`

LINK => https://levelup.gitconnected.com/web-scraping-series-part-iv-world-coins-with-scrapy-data-analysis-with-pandas-6222bb8d6aa7






