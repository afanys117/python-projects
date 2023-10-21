import urllib.request
import re

def crawl_website(url):
    visited_links = set()
    links_to_visit = [url]
    emails = set()
    phone_numbers = set()

    while links_to_visit:
        current_url = links_to_visit.pop()

        if current_url in visited_links:
            continue

        try:
            response = urllib.request.urlopen(current_url)
            html = response.read().decode('utf-8')
            visited_links.add(current_url)

            # Extract email addresses
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            found_emails = re.findall(email_pattern, html)
            emails.update(found_emails)

            # Extract phone numbers (simple example)
            phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
            found_phone_numbers = re.findall(phone_pattern, html)
            phone_numbers.update(found_phone_numbers)

            # Extract links on the current page
            # link_pattern = r'href=["\'](https?://.*?)(?=["\'])'
            # found_links = re.findall(link_pattern, html)
            # links_to_visit.extend(found_links)

        except Exception as e:
            print(f"Error crawling {current_url}: {str(e)}")

    return emails, phone_numbers

if __name__ == '__main__':
    target_url = 'https://example.com'  # Replace with the URL of the website you want to crawl
    crawled_emails, crawled_phone_numbers = crawl_website(target_url)

    print("Crawled Emails:")
    for email in crawled_emails:
        print(email)

    print("\nCrawled Phone Numbers:")
    for phone_number in crawled_phone_numbers:
        print(phone_number)
