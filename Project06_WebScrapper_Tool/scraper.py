import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    
    # Send a request to the website
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the quote boxes on the page
        quote_elements = soup.find_all('div', class_='quote')
        
        # Open a CSV file to save the data
        with open('scraped_quotes.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Quote", "Author"]) # Header row
            
            for element in quote_elements:
                text = element.find('span', class_='text').get_text()
                author = element.find('small', class_='author').get_text()
                writer.writerow([text, author])
                
        print("Success! Data has been saved to scraped_quotes.csv")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_quotes()