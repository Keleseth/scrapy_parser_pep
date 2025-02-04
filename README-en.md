# PEP Documentation Parser Based on Scrapy Framework

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scrapy](https://img.shields.io/badge/Scrapy-FF6347?style=for-the-badge&logo=python&logoColor=white)
![Twisted](https://img.shields.io/badge/Twisted-6A5ACD?style=for-the-badge&logo=twilio&logoColor=white)
![cssselect](https://img.shields.io/badge/cssselect-FFD700?style=for-the-badge&logo=css3&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

## Description
The project is designed for collecting and analyzing data from Python Enhancement Proposals (PEP) documentation. It allows you to obtain up-to-date information about the statuses of all existing PEPs and generate a summary of the number of PEPs in each status.

## Installation

1. Clone the repository and navigate to the project folder:
    ```bash
    git clone <repository-url>
    ```
    ```bash
    cd <project-repository>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the parser "spider" using the command:

```bash
cd scrapy_parser_pep
scrapy crawl pep
```

The parsing result is saved by default to the results folder in the project root folder in csv format.

Project developed by Alexander Kelesidis. GitHub: [Keleseth](https://github.com/Keleseth)