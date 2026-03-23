import requests
import feedparser
from bs4 import BeautifulSoup

RSS_URL = "https://feeds.bbci.co.uk/news/rss.xml "
KEYWORD = "Iran"

def extract_article_content(article):
    title = article.get("title", "")
    link  = article.get("link" , "")
    article_text = fetch_article_text(link)
    result = {
            "title": title,
            "link": link,
            "preview": article_text[:80],
            "text": article_text
    }
    return result

def fetch_rss_feed(url):
    return feedparser.parse(url)

def fetch_article_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching article: {url}")
        return ""

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join(p.get_text() for p in paragraphs)
    return text

def filter_article(keyword, article):
    return keyword.lower() in article['text'].lower()

def fetch_article_links(article_URL):
####################################################################################################
########                                                                                    ########
####       CODE ABOVE IS SACRED; DO NOT ALTER LEST YOU UNLEASH ACCURSED UNUTTERABLE CHAOS       ####
########                                                                                    ########
####################################################################################################


    # STEP 1:
    # Use the `requests` library to `get` the news article.
    #
    # Remember you can:
    #   - Read and learn from existing parts of the script
    #   - Read the `requests` documentation
    #   - Read the `BeautifulSoup` documentation
    #   - Lookup information using a search engine
    #   - Email the instructor (last resort)


    # STEP 2:
    # Use the `BeautifulSoup` library to parse the news article
    # and then locate the "article" tag.


    # STEP 3:
    # Within the article tag, locate all the anchor ("a").
    # Anchor tags contain links.


    # STEP 4:
    # Get the URL of each anchor tag by accessing the 'href' attribute.


    # STEP 5:
    # return a list (possibly empty) of the links found in the article.


def check_for_relevance(keyword, link):

    # STEP 6:
    # Use the `requests` library to `get` the webpage that the article linked to.


    # STEP 7:
    # Use the `BeautifulSoup` library to parse the webpage.


    # STEP 8:
    # return True if and only if the keyword is found in the webpage.


####################################################################################################
########                                                                                    ########
####       CODE BELOW IS SACRED; DO NOT ALTER LEST YOU UNLEASH ACCURSED UNUTTERABLE CHAOS       ####
########                                                                                    ########
####################################################################################################

def main():
    feed = fetch_rss_feed(RSS_URL)
    entries = feed.entries

    articles = map(extract_article_content, entries)

    filtered_articles = list(filter(lambda x: filter_article(KEYWORD, x), articles))
    located_articles = len(filtered_articles)

    print(f"\n=== {located_articles} Articles containing keyword \"{KEYWORD}\" ===\n")

    first = True
    for article in filtered_articles:
        if not first:
            print("\n" + "-" * 80 + "\n")
        first = False

        print(f"Title:\t{article['title']}")
        print(f"Peek:\t{article['preview']}")
        print(f"URL:\t{article['link']}")

        links = fetch_article_links(article['link'])
        filtered_links = list(filter(lambda x: check_for_relevance(KEYWORD, x), links))

        if filtered_links:
            print(f"Relevant References:")
            for link in filtered_links:
                print(f"\t> {link}")


if __name__ == "__main__":
    main()
