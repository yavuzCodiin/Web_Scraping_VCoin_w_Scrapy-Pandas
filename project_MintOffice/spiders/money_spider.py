import scrapy


class MoneySpider(scrapy.Spider):
    name = "moneyspider"
    page_count = 0
    money_count = 1
    file = open("money.txt","a",encoding = "UTF-8")
    start_urls = [
        "https://www.vcoins.com/en/coins/world-1945.aspx"
    ]


    def parse(self, response):
        money_names = response.css("div.item-link a::text").extract()
        money_years = response.css("p.description a::text").extract()
        money_symbols = response.css("div.prices span.newitemsprice::text").extract()[::2]
        money_prices = response.css("div.prices span.newitemsprice::text").extract()[1::2]
        combined_prices = [money_symbols[i] + money_prices[i] for i in range(len(money_prices))]
    
        for i in range(len(money_names)):
            yield {
                "name": money_names[i],
                "year": money_years[i],
                "price": combined_prices[i],
            }
            self.file.write("---------------------------------------------------------------------\n")
            self.file.write(f"{self.money_count}\n")
            self.file.write(f"Name: {money_names[i]}\n")
            self.file.write(f"Year: {money_years[i]}\n")
            self.file.write(f"Price: {combined_prices[i]}\n")
            self.file.write("---------------------------------------------------------------------\n")
            self.money_count += 1
    
        next_page_url = response.css("div.pagination a::attr(href)").extract_first()
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            self.page_count += 1
            if self.page_count != 10:
                yield scrapy.Request(url=absolute_next_page_url, callback=self.parse, dont_filter=True)
            else:
                self.file.close()



