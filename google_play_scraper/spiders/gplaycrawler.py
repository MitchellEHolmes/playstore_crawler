from google_play_scraper.items import GooglePlayScraperItem
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider
import scrapy


class MySpider(CrawlSpider):
    name = "gplay"
    allowed_domains = ["play.google.com"]
    start_urls = ["https://play.google.com/store/apps"]
    # Rules define what links scrapy is allowed to reach for on a website
    rules = [
        Rule(LinkExtractor(allow=(r'apps',)), follow=True, callback='parse_link')
    ]

    count = 0
    MAX_COUNT = 100

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_link(self, response):
        hxs = Selector(response)
        titles = hxs.select('/html')
        items = []
        for title in titles:
            item = GooglePlayScraperItem()
            item["Link"] = title.xpath('head/link[5]/@href').extract()
            item["Item_name"] = title.xpath('//*[@class="document-title"]/div/text()').extract()
            item["Updated"] = title.xpath('//*[@itemprop="datePublished"]/text()').extract()
            item["Author"] = title.xpath('//*[@itemprop="author"]/a/span/text()').extract()
            item["Filesize"] = title.xpath('//*[@itemprop="fileSize"]/text()').extract()
            item["Downloads"] = title.xpath('//*[@itemprop="numDownloads"]/text()').extract()
            item["Version"] = title.xpath('//*[@itemprop="softwareVersion"]/text()').extract()
            item["Compatibility"] = title.xpath('//*[@itemprop="softwareVersion"]/text()').extract()
            item["Content_rating"] = title.xpath('//*[@itemprop="contentRating"]/text()').extract()
            item["Author_link"] = title.xpath('//*[@class="dev-link"]/@href').extract()
            item["Genre"] = title.xpath('//*[@itemprop="genre"]/text()').extract()
            item["Price"] = title.xpath('//*[@class="price buy id-track-click"]/span[2]/text()').extract()
            item["Rating_value"] = title.xpath('//*[@class="score"]/text()').extract()
            item["Review_number"] = title.xpath('//*[@class="reviews-num"]/text()').extract()
            item["Description"] = title.xpath('//*[@class="id-app-orig-desc"]//text()').extract()
            item["IAP"] = title.xpath('//*[@class="inapp-msg"]/text()').extract()
            item["Developer_badge"] = title.xpath('//*[@class="badge-title"]//text()').extract()
            item["Physical_address"] = title.xpath('//*[@class="content physical-address"]/text()').extract()
            item["Video_URL"] = title.xpath('//*[@class="play-action-container"]/@data-video-url').extract()
            item["Developer_ID"] = title.xpath('//*[@itemprop="author"]/a/@href').extract()
            item["Num_Five_Star_Reviews"] = title.xpath(
                '//*[@class="rating-bar-container five"]/span[3]/text()').extract()
            item["Num_Four_Star_Reviews"] = title.xpath(
                '//*[@class="rating-bar-container four"]/span[3]/text()').extract()
            item["Num_Three_Star_Reviews"] = title.xpath(
                '//*[@class="rating-bar-container three"]/span[3]/text()').extract()
            item["Num_Two_Star_Reviews"] = title.xpath(
                '//*[@class="rating-bar-container two"]/span[3]/text()').extract()
            item["Num_One_Star_Reviews"] = title.xpath(
                '//*[@class="rating-bar-container one"]/span[3]/text()').extract()
            item['Reviews'] = title.xpath('//*[@class="review-title"]//text()').extract()

            items.append(item)
            self.count += 1
            if self.count == self.MAX_COUNT:
                raise CloseSpider('Max Pages Reached')
        return items
