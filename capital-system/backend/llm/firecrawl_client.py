import os
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

firecrawl = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

def crawl_schemes(query: str):
    """
    Crawls public funding schemes related to startups.
    """
    result = firecrawl.search(
        query=query,
        limit=5,
        scrape_options={
            "formats": ["markdown"]
        }
    )

    schemes = []
    for item in result["data"]:
        schemes.append({
            "title": item.get("title"),
            "url": item.get("url"),
            "content": item.get("markdown", "")[:500]
        })

    return schemes


def crawl_competitor_strategy(competitor_url: str):
    """
    Crawls competitor website to extract funding strategy hints.
    """
    result = firecrawl.scrape(
        url=competitor_url,
        formats=["markdown"]
    )

    text = result.get("markdown", "").lower()

    strategies = []
    if "grant" in text:
        strategies.append("Uses government grants")
    if "loan" in text:
        strategies.append("Uses debt financing")
    if "accelerator" in text:
        strategies.append("Participates in accelerators")

    return strategies


def crawl_reviews(query: str):
    """
    Extracts negative sentiment / 1-star review pain points.
    """
    result = firecrawl.search(
        query=query,
        limit=5,
        scrape_options={"formats": ["markdown"]}
    )

    pain_points = []

    for item in result["data"]:
        text = item.get("markdown", "").lower()
        if "delay" in text:
            pain_points.append("Slow approval process")
        if "support" in text:
            pain_points.append("Poor customer support")
        if "hidden charges" in text:
            pain_points.append("Lack of pricing transparency")

    return list(set(pain_points))
