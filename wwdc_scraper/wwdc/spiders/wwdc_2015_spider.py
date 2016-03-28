import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wwdc.items import WWDCItem
from w3lib.html import remove_tags

class WWDC2015Spider(CrawlSpider):
    name = "wwdc2015"
    allowed_domains = ["developer.apple.com"]
    start_urls = [
            "https://developer.apple.com/videos/wwdc2015/"
            ]

    # Follow links to all the sessions
    rules = (
            Rule(LinkExtractor(allow='https://developer.apple.com/videos/play/wwdc2015/[0-9]+/+$'),
                'process_links', follow=True,
                ),
            )

    def process_links(self, response):
        # tags, title, abstract & code
        blob = response.xpath("//li[contains(@class, 'details') and contains(@class, 'supplement')]")
        session = WWDCItem()
        session['title'] = remove_tags(blob[0].xpath('h3/text()')[0].extract())
        session['abstract'] = remove_tags(blob[0].xpath('p/text()')[0].extract())
        details = remove_tags(blob[0].xpath('p/text()')[1].extract())
        tags = re.split('-', details)[2] # tags are comma separated at index 2
        tags = [tag.strip() for tag in tags.split(',')]
        session['tags'] = tags
        code = re.split('-', details)[1] # code is in the format WWDC [0-9]+ at index 1
        code = re.search('\d+', code) # match the numeric Session code
        session['code'] = code.group(0)
        session['year'] = 2015

        # resources blob
        blob = response.xpath("//li[contains(@class, 'supplement') and contains(@class, 'resources')]")
        video_blob = blob.xpath("//ul[contains(@class, 'options')]/li/a/@href")
        video_hd = video_blob[0].extract()
        video_sd = video_blob[1].extract()
        session['hd_video'] = video_hd
        session['sd_video'] = video_sd
        slides_blob = blob.xpath("//li[contains(@class, 'document')]/a/@href")
        slides = slides_blob[0].extract()
        session['slides'] = slides

        # phrases blob
        session['transcript'] = []
        something = response.selector.xpath("//li[contains(@class, 'supplement') and contains(@class, 'transcript')]")
        sentences =  something.xpath("//span[contains(@class, 'sentence')]")

        for i, sentence in enumerate(sentences):
            text = sentence.xpath('span/text()')
            start = sentence.xpath('span/@data-start')
            end = sentence.xpath('span/@data-end')
            phrase = {'start' : start.extract()[0], 'end' : end.extract()[0], 'text' : text.extract()[0].replace(' \n', '')}
            session['transcript'].append(phrase)

        yield session

