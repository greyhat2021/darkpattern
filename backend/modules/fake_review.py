import requests
from bs4 import BeautifulSoup
import json
from nltk.sentiment import SentimentIntensityAnalyzer
from urllib.parse import urljoin

def analyze_reviews(product_url):
    def get_total_pages(url):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            page_div = soup.find('div', class_='_2MImiq _1Qnn1K')

            if page_div:
                span_inside_div = page_div.find('span')

                if span_inside_div:
                    total_pages_text = span_inside_div.text[10:].replace(',', '')
                    total_pages = int(total_pages_text)
                    return total_pages
                else:
                    print("Span inside div not found.")
                    return 0
            else:
                print("Div not found.")
                return 0

        else:
            print(f"Error: {response.status_code}")
            return 0

    def scrape_reviews_for_all_pages(base_url, total_pages, review_class, star_class, title_class, upvote_class, downvote_class, username_class):
        reviews_data = []
        count = 1
        for page_number in range(1, total_pages + 1):
            page_url = f"{base_url}&page={page_number}"
            print(f"Scraping data from page {page_number}...")

            response = requests.get(page_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                reviews_on_page = soup.find_all('div', class_=review_class)
                stars_on_page = soup.find_all('div', class_=star_class)
                titles_on_page = soup.find_all('p', class_=title_class)
                upvotes_on_page = soup.find_all('div', class_=upvote_class)
                downvotes_on_page = soup.find_all('div', class_=downvote_class)
                username_on_page = soup.find_all('p', class_=username_class)

                min_length = min(len(reviews_on_page), len(stars_on_page), len(titles_on_page), len(upvotes_on_page), len(downvotes_on_page), len(username_on_page))

                for i in range(min_length):
                    review_text = reviews_on_page[i].text.strip().replace("READ MORE", "")
                    star_text = stars_on_page[i].text.strip()
                    title_text = titles_on_page[i].text.strip()
                    upvote_text = upvotes_on_page[i].find('span', class_='_3c3Px5').text.strip()
                    downvote_text = downvotes_on_page[i].find('span', class_='_3c3Px5').text.strip()
                    user_text = username_on_page[i].text.strip()

                    review_data = {
                        "id": count,
                        "User Name": user_text,
                        "Star Rating": star_text,
                        "Title": title_text,
                        "Review": review_text,
                        "Upvote": upvote_text,
                        "Downvote": downvote_text,
                        "Response": None  # Placeholder for response
                    }

                    if upvote_text != downvote_text:
                        reviews_data.append(review_data)
                        count = count + 1

            else:
                print(f"Error: {response.status_code}")

        return reviews_data

    def analyze_sentiment(text):
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(text)

        if sentiment_scores['compound'] >= 0.0:
            return 'Positive'
        else:
            return 'Negative'

    def get_overall_sentiment(review_text):
        return analyze_sentiment(review_text)

    def merge_scrape_and_sentiment_analysis(base_url, review_class, star_class, title_class, upvote_class, downvote_class, username_class):
        total_pages = get_total_pages(base_url)

        if total_pages > 0:
            print(f"Total Pages: {total_pages}")
            all_reviews_data = scrape_reviews_for_all_pages(base_url, total_pages, review_class, star_class, title_class, upvote_class, downvote_class, username_class)

            with open('reviews_data.json', 'w', encoding='utf-8') as json_file:
                json.dump(all_reviews_data, json_file, ensure_ascii=False, indent=2)

            print("Reviews data written to 'reviews_data.json' file.")

            legitimate_positive = 0
            fake_positive = 0
            legitimate_negative = 0
            fake_negative = 0

            with open('reviews_data.json', 'r', encoding='utf-8') as json_file:
                reviews = json.load(json_file)

            for idx, review_data in enumerate(reviews, start=1):
                review_text = review_data["Review"]
                upvotes = int(review_data["Upvote"])
                downvotes = int(review_data["Downvote"])

                overall_sentiment = get_overall_sentiment(review_text)

                if upvotes > downvotes and overall_sentiment == 'Positive':
                    review_data["Response"] = "Legitimate Positive Review"
                    legitimate_positive += 1
                elif downvotes > upvotes and overall_sentiment == 'Positive':
                    review_data["Response"] = "Fake Positive Review"
                    fake_positive += 1
                elif upvotes > downvotes and overall_sentiment == 'Negative':
                    review_data["Response"] = "Legitimate Negative Review"
                    legitimate_negative += 1
                elif downvotes > upvotes and overall_sentiment == 'Negative':
                    review_data["Response"] = "Fake Negative Review"
                    fake_negative += 1
                else:
                    review_data["Response"] = "Undetermined Review"

            print("Total Legitimate Positive Reviews:", legitimate_positive)
            print("Total Fake Positive Reviews:", fake_positive)
            print("Total Legitimate Negative Reviews:", legitimate_negative)
            print("Total Fake Negative Reviews:", fake_negative)

            # Returning scraped data as a dictionary
            return {"reviews_data": all_reviews_data, "legitimate_positive": legitimate_positive, "fake_positive": fake_positive, "legitimate_negative": legitimate_negative, "fake_negative": fake_negative}

    def scrape_and_construct_url(base_url, relative_url):
        full_url = urljoin(base_url, relative_url)
        print(f"Constructed Full URL: {full_url}")
        return full_url

    def get_review_page_url(url):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            target_div = soup.find('div', class_='col JOpGWq')

            if target_div:
                anchor_element = target_div.find('a', recursive=False)

                if anchor_element:
                    anchor_href = anchor_element.get('href')

                    print(f"Found anchor tag inside div: {anchor_href}")
                    full_url = scrape_and_construct_url(url, anchor_href)
                    return str(full_url)
                else:
                    print("No anchor tag found inside the div.")
            else:
                print("Div with class 'col JOpGWq' not found.")
        else:
            print(f"Error: {response.status_code}")

        return None

    predefined_url = get_review_page_url(product_url)
    review_class_to_find = 't-ZTKy'
    star_class_to_find = '_3LWZlK _1BLPMq'
    title_class_to_find = '_2-N8zT'
    upvote_class_to_find = '_1LmwT9'
    downvote_class_to_find = '_1LmwT9 pkR4jH'
    username_class_to_find = '_2sc7ZR _2V5EHH'

    return merge_scrape_and_sentiment_analysis(predefined_url, review_class_to_find, star_class_to_find, title_class_to_find, upvote_class_to_find, downvote_class_to_find, username_class_to_find)