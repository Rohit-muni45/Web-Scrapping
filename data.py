from bs4 import BeautifulSoup
import json
import csv

# Read index.html file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with class="sg-col-inner"
divs = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v36g8q2u37vpji29sg9uhoxaczm s-latency-cf-section puis-card-border')

data = []

# Iterate through each div
for div in divs:
    # Try to find title
    title_span = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    title = title_span.text.strip() if title_span else ''

    # Try to find price
    price_span = div.find('span', class_='a-offscreen')
    price = price_span.text.strip() if price_span else ''

    # Try to find rating
    rating_span = div.find('span', class_='a-icon-alt')
    rating = rating_span.text.strip() if rating_span else ''

    # Append data to list
    data.append({'title': title, 'price': price, 'rating': rating})

# Write data to data.json
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

# Write data to Excel file
with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Price', 'Rating'])  # Write header
    for item in data:
        writer.writerow([item['title'], item['price'], item['rating']])
