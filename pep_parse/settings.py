from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]


ROBOTSTXT_OBEY = True

# Форматы
OUTPUT_FORMATS = {
    'csv': 'csv',
    'json': 'json',
    'xml': 'xml',
    'feedexport': 'feed',
}
OUTPUT_FORMAT = OUTPUT_FORMATS['csv']
DATE_FORMAT = ('%Y-%m-%d_%H-%M-%S')

# Поля объекта PepParseItem
PEP_ITEM_KEYS = [
    'number',
    'name',
    'status'
]

# Файлы результатов парсинга и путь к ним.
PEP_FILE_NAME = 'pep_%(time)s'
OUTPUT_PEP_RESULTS = f'{RESULTS_DIR}/{PEP_FILE_NAME}.{OUTPUT_FORMAT}'
OUTPUT_STATUS_RESULTS = 'status_summary_{}.{}'

FEEDS = {
    OUTPUT_PEP_RESULTS: {
        'format': OUTPUT_FORMAT,
        'fields': PEP_ITEM_KEYS,
        'overwrite': True
    }
}

# регулярное выражение для поиска и извлечения номера и названия PEP
TITLE_PATTERN = r'PEP (\d+)\s*[-–]\s*(.+)'

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

# Заголовки csv файла со сводкой по статусам PEP
CSV_STATUS_HEADERS = ('Статус', 'Количество')

# logger
LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(exist_ok=True)
LOG_FILE = BASE_DIR / LOGS_DIR / 'pep_logs'
LOG_LEVEL = 'ERROR'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

# Селекторы css и xpath
LINK_TO_PEP_SELECTOR = 'tbody tr a[href^="pep-"]'
PEP_TITLE_SELECTOR = 'h1.page-title::text'
PEP_STATUS_SELECTOR = (
    '//dt[contains(text(), "Status")]/following-sibling::dd[1]/abbr/text()'
)
