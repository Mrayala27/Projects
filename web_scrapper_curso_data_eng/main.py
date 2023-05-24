import argparse
import logging

import news_page_objects as news
from common import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']
    text = 'Beginning scraper for:' + host
    logging.info(text)
    homepage = news.HomePage(news_site_uid, host)
    for link in homepage.article_links:
        print(link)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    new_sites_choices = list(config()['news_sites'].keys())
    parser.add_argument(
        'news_sites',
        help='The news sites that want to scrape',
        type=str,
        choices=new_sites_choices
    )

    args = parser.parse_args()
    _news_scraper(args.news_sites)