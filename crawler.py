import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Create the argument parser
parser = argparse.ArgumentParser(description='Web Crawler')

# Add the command-line options
parser.add_argument('url', nargs='?', default='urls.txt',
                    help='URL or file path containing the list of URLs (default: urls.txt)')
parser.add_argument('-d', '--depth', type=int, default=1,
                    help='maximum depth of crawl (default: 1)')
parser.add_argument('-t', '--trace', default='trace to find',
                    help='trace to search for in the web pages (default: "trace to find")')
parser.add_argument('-a', '--all', action='store_true',
                    help='search for the trace in all content (default: False)')

# Parse the command-line arguments
args = parser.parse_args()

# Assign the values to variables
url_source = args.url
max_crawl_depth = args.depth
trace_to_find = args.trace
search_all_content = args.all

# Read the URLs from the file if the source is urls.txt
if url_source == 'urls.txt':
    with open(url_source, 'r') as file:
        urls = file.readlines()
else:
    # Use the specified URL as a single item list
    urls = [url_source]


def crawl(url, domain, trace, found_file, log_file, max_depth, current_depth=1, visited_urls=None, search_all_content=False):
    if visited_urls is None:
        visited_urls = set()

    try:
        if not url.startswith(('http://', 'https://')):
            return

        parsed_url = urlparse(url)
        if parsed_url.netloc != domain:
            return

        if url in visited_urls:
            return

        visited_urls.add(url)
        log_file.write("Crawled URL: {}\n".format(url))

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        content = response.text if search_all_content else soup.get_text()

        if trace.lower() in content.lower():
            print("Trace found on page: {}".format(url))
            found_file.write("Trace found at: {}\n".format(url))

        if current_depth < max_depth:
            # Find all anchor tags on the page
            anchors = soup.find_all('a')

            for anchor in anchors:
                next_url = anchor.get('href')
                absolute_url = urljoin(url, next_url)
                crawl(absolute_url, domain, trace, found_file, log_file, max_depth, current_depth + 1, visited_urls,
                      search_all_content)

    except KeyboardInterrupt:
        print("Program interrupted by the user.")
        found_file.close()
        log_file.close()
        exit()


def main():
    with open('found.txt', 'w') as found_file, open('log.txt', 'w', encoding='utf-8') as log_file:
        for url in urls:
            url = url.strip()
            domain = urlparse(url).netloc
            crawl(url, domain, trace_to_find, found_file, log_file, max_crawl_depth, search_all_content=search_all_content)


if __name__ == '__main__':
    main()
