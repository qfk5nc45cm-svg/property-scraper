# 🏠 Property Scraper Project

## 📌 Overview

This project is a Python web scraper that collects property listings from Property24. It extracts structured data such as price, location, number of bedrooms, bathrooms, parking spaces, and property size.

## 🌐 Data Source

The data is scraped from Property24:
https://www.property24.com

## ⚙️ Features Extracted

* Price
* Title / Description
* Location
* Bedrooms
* Bathrooms
* Parking spaces
* Property size

## 📊 Output

The scraped data is saved into a CSV file (`Properties.csv`) for further analysis.

## 🧰 Technologies Used

* Python
* BeautifulSoup (bs4)
* Requests
* CSV module
* LXML parser

## 🚀 How to Run

1. Install dependencies:

   ```
   pip install requests beautifulsoup4 lxml
   ```

2. Run the script:

   ```
   python scraper.py
   ```

## ⚠️ Disclaimer

This project is for educational purposes only.

