import scrapy  
import csv  


class MoneySpider(scrapy.Spider):
    name = "moneyspider_csv"  
    page_count = 0  
    money_count = 1 
    start_urls = ["https://www.vcoins.com/en/coins/world-1945.aspx"]

    def start_requests(self):
        self.file = open('money.csv', 'w', newline='', encoding='UTF-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['Count', 'Name', 'Year', 'Price'])
        return [scrapy.Request(url=url) for url in self.start_urls]

 
    def parse(self, response):

        money_names = response.css("div.item-link a::text").extract()

        money_years = response.css("p.description a::text").extract()

        money_symbols = response.css("div.prices span.newitemsprice::text").extract()[::2]

        money_prices = response.css("div.prices span.newitemsprice::text").extract()[1::2]

        combined_prices = [money_symbols[i] + money_prices[i] for i in range(len(money_prices))]
    

        for i in range(len(money_names)):
            self.writer.writerow([self.money_count, money_names[i], money_years[i], combined_prices[i]])
            self.money_count += 1  
    
        
        next_page_url = response.css("div.pagination a::attr(href)").extract_first()
      
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            self.page_count += 1  
  
            if self.page_count != 10:
                yield scrapy.Request(url=absolute_next_page_url, callback=self.parse, dont_filter=True)
            else:
                self.file.close()  
