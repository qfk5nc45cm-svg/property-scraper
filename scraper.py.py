from bs4 import BeautifulSoup
import requests, lxml, time, csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

base_url = 'https://www.property24.com/for-sale/advanced-search/results?sp=cid%3d100%2c1%26s%3d5992%26al%3d19%26hp%3dTrue&PropertyCategory=House%2cApartmentOrFlat%2cTownhouse%2cVacantLandOrPlot%2cFarm%2cCommercial%2cIndustrial&Page={page}'

def housing():
    with open(r'C:\Users\Admin\OneDrive - Sol Plaatje University\Documents\SOL PLAATJE UNIVERSITY\PYCHARM MISC PROJECTS\Properties.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)                                                         
        writer.writerow(['Price', 'Title', 'Location', 'Bedrooms', 'Bathrooms', 'Parking', 'Size'])

        for page in range(1, 24):                                                      
            print(f'Scraping page {page}...')

            html_text = requests.get(base_url.format(page=page), headers=headers).text
            soup = BeautifulSoup(html_text, 'lxml')
            listings = soup.find_all('div', class_='p24_information')

            if not listings:
                print(f'No listings found on page {page}, stopping.')
                break

            for listing in listings:                                                   
                price       = listing.find('div', class_='p24_price')
                description = listing.find('div', class_='p24_description')
                location    = listing.find('span', class_='p24_location')
                bedrooms    = listing.find('span', title='Bedrooms')
                bathrooms   = listing.find('span', title='Bathrooms')
                parking     = listing.find('span', title='Parking Spaces')
                size        = listing.find('span', class_='p24_size')

                 
                price_strings  = list(price.stripped_strings) if price else []
                price_text     = ' '.join(price_strings[:2]) if price_strings and price_strings[0] == 'From' else (price_strings[0] if price_strings else 'N/A')
                desc_text      = ' '.join(description.find(text=True, recursive=False).split()) if description else 'N/A'
                location_text  = location.text.strip() if location else 'N/A'
                bedrooms_text  = bedrooms.find('span').text.strip() if bedrooms else 'N/A'
                bathrooms_text = bathrooms.find('span').text.strip() if bathrooms else 'N/A'
                parking_text   = parking.find('span').text.strip() if parking else 'N/A'
                size_text      = size.find('span').text.strip() if size else 'N/A'

                writer.writerow([price_text, desc_text, location_text, bedrooms_text, bathrooms_text, parking_text, size_text]) 

            time.sleep(2)                                                              

    print('Done! Saved to Properties.csv')

housing()             
#icons = listings[0].find('div', class_='p24_icons')
#print(icons.prettify())