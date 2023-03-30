import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from google_drive_scrape_apartments import google_drive

def get_apartment_data(base_url, page_number):
    if page_number == 1:
        url = base_url
    else:
        url = f"{base_url}{page_number}/"
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    apartments = []
    
    for listing in soup.find_all('article', class_='placard'):
        apt_link = listing.find('a', class_='property-link')
        apt_url = apt_link['href'] if apt_link else None
        apt_name = apt_link.get('aria-label', None) if apt_link else None
        apt_phone_link = listing.find('a', class_='js-phone');
        apt_phone = apt_phone_link.span if apt_phone_link and apt_phone_link.span else None
        apt_phone_number = apt_phone.get_text(strip=True) if apt_phone else None
        
        if apt_url:
            apartments.append({
                'name': apt_name,
                'url': apt_url,
                'phone': apt_phone_number
            })

    return apartments
print("Starting program")
url = 'https://www.apartments.com/st-george-ut/'
number_of_pages = 7
apartments = [];
for page_number in range(1, number_of_pages + 1):
    print(f"--- Page {page_number} ---")
    apartments += get_apartment_data(url, page_number)
# Create a new Google Sheet and write the data to it
sheet_name = 'Apartments.com St. George UT Sales Sheet'
google_drive(apartments, sheet_name)

