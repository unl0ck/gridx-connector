import requests
from bs4 import BeautifulSoup

THREAD_URL = "https://community.developer.gridx.de/t/gridx-api-documentation/213"


def get_latest_json_url():
    r = requests.get(THREAD_URL)
    soup = BeautifulSoup(r.text, "html.parser")

    for a in soup.find_all("a"):
        href = a.get("href", "")
        if href.endswith(".json"):
            return href

    raise Exception("Keine JSON URL gefunden")


def download():
    url = get_latest_json_url()
    print("Gefunden:", url)

    data = requests.get(url).json()
    return data


if __name__ == "__main__":
    api = download()
