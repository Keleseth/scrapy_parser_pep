# PEP Documentation Parser Based on Scrapy Framework

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