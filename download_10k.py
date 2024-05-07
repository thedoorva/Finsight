import requests

def get_10k_filings(ticker, cik):
    filings = []
    url = f"https://data.sec.gov/submissions/{cik}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'filings' in data:
            for entry in data['filings']:
                if entry.get('form') == '10-K':
                    filing_url = entry.get('linkToHtml')
                    filings.append(filing_url)
            print(f"Found {len(filings)} 10-K filings for {ticker}")
            return filings
        else:
            print(f"No 'filings' data found for {ticker}")
            return None
    else:
        print(f"Failed to fetch data for {ticker}. Status code: {response.status_code}")
        return None

def download_10k_filings(ticker):
    cik_map = {
        'JPM': '0000019617',
        'GS': '0000886982',
        'BLK': '0001364742'
    }
    cik = cik_map.get(ticker)
    if cik:
        filings = get_10k_filings(ticker, cik)
        if filings:
            for i, filing_url in enumerate(filings, start=1):
                filename = f"{ticker}_10K_{i}.html"
                response = requests.get(filing_url)
                if response.status_code == 200:
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded {filename}")
                else:
                    print(f"Failed to download {filename}. Status code: {response.status_code}")
    else:
        print(f"Invalid ticker: {ticker}")

# Prompt the user for a company ticker
ticker = input("Enter the ticker symbol of the company (e.g., JPM, GS, BLK): ")
download_10k_filings(ticker)
