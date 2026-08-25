# Quotes Web Scraper & Data Analysis

A lightweight Python project that scrapes quote data from [Quotes to Scrape](https://quotes.toscrape.com/) and performs basic data analysis and visualization.

## 📌 Features

- **Web Scraping (`main.py`)**:
  - Scrapes quote text, author names, and tags.
  - Automatically navigates through paginated pages.
  - Includes a rate-limiting delay between requests.
  - Exports data into `quotes.csv`.

- **Data Analysis (`analysis.py`)**:
  - Analyzes top authors and tag distributions using Pandas.
  - Displays statistical answers in the console.
  - Plots bar charts using Matplotlib for top authors and tags.

## 🛠️ Prerequisites & Installation

Install the required Python packages:

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

## 🚀 Usage

1. **Run the Scraper**:
   ```bash
   python main.py
   ```
   Generates `quotes.csv`.

2. **Run the Analysis**:
   ```bash
   python analysis.py
   ```
   Prints data insights and displays bar charts.

## 📁 File Structure

```
├── main.py        # Web scraper script
├── analysis.py    # Data analysis & visualization script
├── quotes.csv     # Output dataset
└── README.md      # Project documentation
```
