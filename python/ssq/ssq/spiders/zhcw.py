import scrapy


class ZhcwSpider(scrapy.Spider):
    name = "zhcw"
    allowed_domains = ["zhcw.com"]
    start_urls = [
        "http://kaijiang.zhcw.com/zhcw/html/ssq/list.html",
    ]

    def parse(self, response):
        table = response.css("table.wqhgt")
        tr_list = table.css("tr")[2:-1]
        for tr in tr_list:
            yield {
                "date": tr.css("td::text")[0].extract(),
                "seq": tr.css("td::text")[1].extract(),
                "nums": [
                    tr.css("td em::text")[0].extract(),
                    tr.css("td em::text")[1].extract(),
                    tr.css("td em::text")[2].extract(),
                    tr.css("td em::text")[3].extract(),
                    tr.css("td em::text")[4].extract(),
                    tr.css("td em::text")[5].extract(),
                    tr.css("td em::text")[6].extract()
                ],
            }
        next_page = table.css("tr")[-1].css("td strong")[4].css("a::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
