# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals

class JSONPipeline(object):
    def __init__(self):
        self.files = {}
        self.exporters = {}
        dispatcher.connect(self.spider_opened, signal=signals.spider_opened)
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)

    def process_item(self, item, spider):
        item_kind = type(item).__name__
        self.exporters[item_kind].export_item(item)
        return item

    def spider_opened(self, spider):
        base_name = spider.start_urls[0].split("/")[-1]

        # bit of an ugly hack for WWDC 2011 (different URL formats)
        # who said scraping isn't a bit ugly anyway... :P
        if base_name == '':
            base_name = "wwdc2011"

        no_transcript_file = open('%s.json' % base_name, 'w+b')
        transcript_file = open('%s_transcript.json' % base_name, 'w+b')

        # create output files
        self.files['WWDCNoTranscriptItem'] = no_transcript_file
        self.files['WWDCItem'] = transcript_file

        # create exporters
        self.exporters['WWDCNoTranscriptItem'] = JsonItemExporter(no_transcript_file)
        self.exporters['WWDCItem'] = JsonItemExporter(transcript_file)

        # Start exporting
        [exporter.start_exporting() for exporter in self.exporters.values()]


    def spider_closed(self, spider):
        [exporter.finish_exporting() for exporter in self.exporters.values()]
        [f.close() for f in self.files.values()]

