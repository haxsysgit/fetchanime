
# Anime Fetch API

This is a Python script that can be used to search and download anime episodes from [animepahe](https://animepahe.com/). It uses the `requests`, `beautifulsoup4`, and `selenium` libraries to interact with the website and scrape relevant data.

## Prerequisites

- Python 3.x
- The `requests`, `beautifulsoup4`, `selenium`, and `chromedriver_autoinstaller` Python libraries. You can install them by running:

  ```shell
  pip install requests beautifulsoup4 selenium chromedriver_autoinstaller
  ```

## Usage

To use the script, run it in your terminal using the following command:

```shell
python fetchanime.py [-h] [-b BROWSER] [-s SEARCH] [-sh SEARCH_HIDDEN] [-i INDEX] [-sd SINGLE_DOWNLOAD] [-md MULTI_DOWNLOAD_OPTIMIZED] [-mdv MULTI_DOWNLOAD_VERBOSE] [-a ABOUT] [-ad AUTODRIVER]
```

Here are the available options:

- `-h`, `--help`: show the help message and exit
- `-b`, `--browser`: choose the browser to use (`chrome` or `firefox`). If omitted, the script will use `chrome` by default. Use `ff` for a GUI Firefox window.
- `-s`, `--search`: search for an anime using a keyword. The script will display a list of matching results.
- `-sh`, `--search_hidden`: search for an anime using its name and index. This option is less verbose than the regular search.
- `-i`, `--index`: choose an anime from the search results by its index.
- `-sd`, `--single_download`: download a single episode of an anime by its number.
- `-md`, `--multi_download_optimized`: download multiple episodes of an anime at once using a faster, optimized method. Specify a comma-separated string of episode numbers to download.
- `-mdv`, `--multi_download_verbose`: download multiple episodes of an anime at once and show a verbose output. Specify a comma-separated string of episode numbers to download.
- `-a`, `--about`: display an overview of the chosen anime.
- `-ad`, `--autodriver`: automatically download and install the correct version of the `chromedriver` executable if it's not found on your system.

## Example Usage

Here are some example commands to run the script:

- Search for an anime: `python fetchanime.py --search "jujutsu kaisen"`
- Choose an anime from the search results: `python fetchanime.py --search "jujutsu kaisen" --index 0`
- Download a single episode: `python fetchanime.py --search "jujutsu kaisen" --single_download 1`
- Download multiple episodes (optimized): `python fetchanime.py --search "jujutsu kaisen" --multi_download_optimized "1,2,3"`
- Download multiple episodes (verbose): `python fetchanime.py --search "jujutsu kaisen" --multi_download_verbose "1,2,3"`
- Get an overview of an anime: `python fetchanime.py --search "jujutsu kaisen" --index 0 --about`

## Acknowledgments

This script was created by [insert your name here] using the following resources:

- [4anime.to](https://4anime.to/)
- [Python Requests library](https://requests.readthedocs.io/)
- [Beautiful Soup 4 library](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)