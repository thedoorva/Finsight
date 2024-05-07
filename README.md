# Finsight
This Finsight is a web application designed to perform text analysis on 10-K filings of various companies using Flask for the backend and JavaScript for the frontend. The backend retrieves 10-K filings data from the SEC website, while the frontend allows users to input a company ticker symbol and receive insights generated from the analysis.
10-K Analysis Tool
Description
This project is a web application that allows users to analyze 10-K filings of companies listed on the stock market. It consists of two main components: a Python backend built using Flask and a frontend interface created with HTML, CSS, and JavaScript.

Features
1. Download 10-K Filings: The backend component includes a script (download_10k.py) that allows users to download 10-K filings from the SEC website for companies such as JPMorgan Chase (JPM), Goldman Sachs (GS), and BlackRock (BLK).
2. Text Analysis: The backend analyzes the downloaded 10-K filings using natural language processing techniques to generate insights about emerging trends or strategic priorities in the filings. This analysis is performed using the Language Model API.
3. Web Interface: The frontend component provides a user-friendly interface where users can enter the ticker symbol of a company and click a button to analyze its 10-K filings. The interface displays the insights generated by the backend in real-time.

Task 1: Downloading 10-K Filings
Task Description
The first task involves selecting companies, downloading their 10-K filings from the SEC website, and automating the process using Python scripts.

Companies Selected
The following companies have been selected for analysis:

- JPMorgan Chase & Co. (Ticker: JPM)
- The Goldman Sachs Group, Inc. (Ticker: GS)
- BlackRock, Inc. (Ticker: BLK)

Python Script (download_10k.py)
The download_10k.py script is used to download 10-K filings for the selected companies from the SEC website.

```python
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
```

Steps to Run
Execute the download_10k.py script in a Python environment.
Enter the ticker symbol of the company when prompted.
The script will fetch and download the 10-K filings for the specified company.
Example Usage
Include screenshots or GIFs demonstrating how to run the script and the output obtained.

Task 2: Text Analysis
Task Description
The second task involves using a Flask backend and JavaScript frontend to perform text analysis on the downloaded 10-K filings and generate insights.

Backend Code (Flask)
The Flask backend (app.py) provides routes for analyzing the 10-K filings and serving the frontend interface.

```python
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
@app.route('/')
def index():
    # Render the HTML template for the front-end code
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Frontend Code (HTML, JavaScript)
The frontend interface (index.html) allows users to input company ticker symbols and trigger the analysis process.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>10-K Analysis</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
    
    <h1>10-K Analysis</h1>
    <label for="ticker">Enter the ticker symbol of the company (e.g., JPM, GS, BLK):</label>
    <input type="text" id="ticker" name="ticker">
    <button id="analyze-btn">Analyze</button>

    <div id="insights">
    </div>

    <script>
        $(document).ready(function() {
            $('#analyze-btn').click(function() {
                var ticker = $('#ticker').val();
                if (ticker.trim() === '') {
                    alert('Please enter a ticker symbol');
                    return;
                }
                
                $.ajax({
                    url: '/analyze', // Ensure that the URL matches the Flask route
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ 'ticker': ticker }),
                    success: function(response) {
                        if ('error' in response) {
                            alert(response['error']);
                        } else {
                            displayInsights(response);
                        }
                    },
                    error: function(xhr, status, error) {
                        alert('Failed to analyze 10-K filings');
                        console.error(error);
                    }
                });
            });

            function displayInsights(insights) {
                $('#insights').empty();
                $.each(insights, function(key, value) {
                    $('#insights').append(`<p><strong>${key}:</strong> ${value}</p>`);
                });
            }
        });
    </script>
</body>
</html>
```

Steps to Run
Run the Flask server by executing python app.py in the terminal.
Open a web browser and navigate to the specified URL (usually http://127.0.0.1:5000/).
Enter a company ticker symbol and click "Analyze" to generate insights.
Example Usage
Including screenshots demonstrating how to use the application and view the generated insights.
![alt text](WebPage.PNG)

Task 3: Simple App Deployment
Task Description
The third task involves deploying the Flask application on a platform or recording a local demo.

Deployment Method
For deployment, the application can be hosted on platforms such as AWS, or Google Cloud Platform. Alternatively, a local demo can be recorded.

Deployment Instructions
Deploy the Flask application to the chosen platform using the provided deployment guidelines.
Provide the deployment URL or a link to the local demo in the README.md file.
Example Deployment
Include screenshots or GIFs demonstrating the deployed application in action.

Author
Doorva Agrawal

Acknowledgments
The development of this project was made possible with the support and contributions of various individuals and resources. I  would like to express our gratitude to:

SEC EDGAR Database: For providing access to 10-K filings and financial reports.
Flask Framework: For enabling the development of the backend server for this application.
jQuery Library: For simplifying AJAX requests and DOM manipulation in the frontend code.
GitHub: For hosting the project repository and facilitating collaboration.
OpenAI GPT-3: For providing assistance and guidance during the development process.
Stack Overflow Community: For providing valuable insights and solutions to technical challenges.

I acknowledge and appreciate the contributions of all individuals and resources involved in the development and completion of this project.
