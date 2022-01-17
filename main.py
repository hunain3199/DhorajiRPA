import scrapy

class OlxSpider(scrapy.Spider):
 name='olx'
 start_urls = ['https://www.olx.com.pk/']

 def parse(self, response):
    all_url = response.xpath("//a[@class='_7d3f8c9a']/@href")
    for i in all_url:
        myurl = "https://www.olx.com.pk" + i.extract()
        yield scrapy.Request(url= myurl, callback=self.parse2)

 def parse2(self, response):
     prod_link = response.xpath("//div[@class='_44525bac']/a/@href")
     for j in prod_link:
         url_prod = "https://www.olx.com.pk" + j.extract()
         yield scrapy.Request(url=url_prod, callback=self.parse3)


 def parse3(self, response):
     all_product_link = response.xpath("//div[@class='ee2b0479']/a/@href")
     for a in all_product_link:
         print(a)
        # all_link ="https://www.olx.com.pk" + a.extract()
        # yield{
        #     'all links ' : a.extract()
        # }
         # yield scrapy.Request(url=all_link, callback=self.parse_product)

 # def parse_product(self, response):
 #     product_name = response.xpath("//h1[@class='a38b8112']/text()").get()
 #     product_price = response.xpath("//span[@class='_56dab877']/text()").get()
 #     yield{
 #         'Product Name': product_name,
 #         'Product Price': product_price
 #     }

