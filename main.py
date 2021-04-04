#!/usr/bin/env python

import os
from argparse import ArgumentParser
from datetime import datetime

from weasyprint import HTML

from requests_html import HTMLSession

SESSION = HTMLSession()
BASE_URL = "https://www.gktoday.in/current-affairs/category/{category}/page/{page_num}"


def get_page(url: str):
    return SESSION.get(url)


def parse_date(date: str):
    date = date.lstrip("Published: ")
    time_obj = datetime.strptime(date, "%B %d, %Y")
    return time_obj


def save_pdf(html_string, name, dated, category):
    article_date = parse_date(dated).strftime("%Y%m%d")
    path = "articles/{}/{}".format(category, article_date)
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = "{}/{}-{}.pdf".format(path, article_date, name.replace("/", "-"))
    HTML(string=html_string).write_pdf(file_name)
    print("written file", file_name)


def process_category(category: str, pages: int, page_start: int = 1):
    temp_args = {"category": category, "page_num": 1}
    for i in range(page_start, pages + 1):
        temp_args["page_num"] = i
        category_page = get_page(BASE_URL.format(**temp_args))
        titles = category_page.html.find("div.posts-listing > h1 > a")
        for title in titles:
            link = title.links.pop()
            article_page = get_page(link)
            article = article_page.html.find("div.inside_post", first=True)
            article_date = article.find("div.postmeta-primary > p", first=True).text
            save_pdf(article.html, title.text, article_date, category)
        print("processed page ", i)


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Parse and save as PDF range of pages from gktoday.in for category",
    )
    parser.add_argument(
        "category",
        help="Provide category for the website such as `environment-current-affairs`",
    )
    parser.add_argument("page_num", help="Page until which to parse", type=int)
    parser.add_argument(
        "--start",
        "-s",
        help="Start parsing from this page",
        type=int,
        default=1,
    )
    args = parser.parse_args()
    process_category(args.category, args.page_num, args.start)
