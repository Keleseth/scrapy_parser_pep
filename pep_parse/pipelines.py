import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import (
    BASE_DIR,
    CSV_STATUS_HEADERS,
    DATE_FORMAT,
    OUTPUT_STATUS_RESULTS,
    RESULTS_DIR,
)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True, parents=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime(DATE_FORMAT)
        output_file = (
            self.results_dir / OUTPUT_STATUS_RESULTS.format(now, 'csv')
        )

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            data = (
                CSV_STATUS_HEADERS,
                *self.status_count.items(),
                ('Total', sum(self.status_count.values()))
            )
            writer.writerows(data)
