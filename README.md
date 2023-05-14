# Trace Crawler

The Trace Crawler is a Python script that allows you to crawl web pages and search for a specific trace within the page content. It provides an easy way to discover if a trace, such as a keyword or text snippet, is present on a website or a collection of URLs.

## Prerequisites

- Python 3.x: If you don't have Python installed, you can download it from the official Python website: https://www.python.org/downloads/

## Installation

1. Clone the repository or download the ZIP file.

2. Open a terminal or command prompt and navigate to the project directory.

3. Create a virtual environment (optional but recommended):

```python3 -m venv myenv```

Activate the virtual environment (Linux/Mac):
```source myenv/bin/activate``` 


Activate the virtual environment (Windows):
```myenv\Scripts\activate```




4. Install the required dependencies:

```pip install argparse requests beautifulsoup4```


## Usage

The basic usage of the crawler is as follows:

```python crawler.py [URL] [OPTIONS]```


- `URL` (optional): The starting URL to crawl. If not provided, the script will read URLs from the `urls.txt` file in the project directory.

### Options

- `-d, --depth`: Maximum crawl depth. Specifies how many levels deep the crawler should go. Default is 1, this means it will only crawl urls you provide and will not follow any links.
- `-t, --trace`: The trace to search for within the page content. Case-insensitive. Default is an empty string, which will search for all pages.
- `-a, --all-content`: Search for the trace within all content (including HTML tags, attributes, and JavaScript) instead of text-only. Default is False.
- `-h, --help`: Show the help message and usage instructions.

### Examples

1. Crawl a specific URL with default options:

```python crawler.py https://www.example.com```


2. Crawl URLs from the `urls.txt` file with a maximum depth of 4 and search for the trace "sometrace" within all content:

```python crawler.py -d 4 -t sometrace -a```


## License

This project is licensed under the MIT License. 


