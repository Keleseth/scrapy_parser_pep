import scrapy

from pep_parse.exceptions import PatternMatchError
from pep_parse.items import PepParseItem
from pep_parse.settings import (
    LINK_TO_PEP_SELECTOR,
    PEP_ITEM_KEYS,
    PEP_STATUS_SELECTOR,
    PEP_TITLE_SELECTOR,
    TITLE_PATTERN,
)
from pep_parse.utils import extract_text_with_pattern


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for pep_link in response.css(LINK_TO_PEP_SELECTOR):
            yield response.follow(
                pep_link,
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        try:
            number, name = extract_text_with_pattern(
                TITLE_PATTERN,
                response.css(PEP_TITLE_SELECTOR).get()
            )
        except PatternMatchError as error:
            self.logger.error(str(error))
            return

        status = response.xpath(PEP_STATUS_SELECTOR).get().strip()
        data = dict(
            zip(
                PEP_ITEM_KEYS,
                (number, name, status)
            )
        )
        yield PepParseItem(data)
