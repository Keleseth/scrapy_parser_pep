# Парсер документации PEP на основе фреймворка Scrapy

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scrapy](https://img.shields.io/badge/Scrapy-FF6347?style=for-the-badge&logo=python&logoColor=white)
![Twisted](https://img.shields.io/badge/Twisted-6A5ACD?style=for-the-badge&logo=twilio&logoColor=white)
![cssselect](https://img.shields.io/badge/cssselect-FFD700?style=for-the-badge&logo=css3&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)


## Описание
Проект предназначен для сбора и анализа данных из документации Python Enhancement Proposals (PEP). С его помощью можно получить актуальную информацию о статусах всех существующих PEP, а также сформировать сводку с количеством PEP в каждом статусе.


## Установка

1. Клонируйте репозиторий и перейдите в папку с проектом:
```bash
git clone <repository-url>
```
```bash
cd <project-repository>
```


2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

Запустите "паука" парсера "scrapy crawl pep"

### Примеры

Получить статьи из раздела "Что нового":
```bash
cd scrapy_parser_pep
scrapy crawl pep
```

Результат парсинга сохраняется по умолчанию в папку results в корневой папке проекта в csv формате.

Проект разработан Келесидисом Александром. GitHub: [Keleseth](https://github.com/Keleseth)
