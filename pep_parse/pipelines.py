
import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import (
    OUTPUT_STATUS_RESULTS,
    DATE_FORMAT,
    BASE_DIR,
    RESULTS_DIR,
    CSV_STATUS_HEADERS
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime(DATE_FORMAT)
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True, parents=True)
        output_file = results_dir / OUTPUT_STATUS_RESULTS.format(now, 'csv')

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(CSV_STATUS_HEADERS)
            writer.writerows(self.status_count.items())
            writer.writerow(
                ['Total', sum(self.status_count.values())]
            )
