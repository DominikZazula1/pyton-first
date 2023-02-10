from dataclasses import dataclass
import requests as requests
from bs4 import BeautifulSoup


def is_title_containing_tag(tag):
    return tag.name == "h3" and tag.has_attr("class") and "title" in tag["class"] and "text--inter" in tag["class"]


def is_type_containing_tag(tag):
    return tag.name == "span" and tag.has_attr("class") and "top-label" in tag["class"]


@dataclass
class PostPreview:
    course_type: str
    title: str


class InfoShareAcademyParser:
    PAGE_URL = "https://infoshareacademy.com"

    def __init__(self):
        self.parsed_page = None
        self.last_post_index = 0
        self.found_post_previews = []

    def load_page_html(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.parsed_page = BeautifulSoup(response.text, features="html.parser")

    def parse_all_previews(self):
        type_tags = self.parsed_page.find_all(is_type_containing_tag)
        title_tags = self.parsed_page.find_all(is_title_containing_tag)
        for type_tag, title_tag in zip(type_tags, title_tags):
            post_preview = PostPreview(type_tag.string, title_tag.string)
            self.found_post_previews.append(post_preview)


def run_homework():
    parser = InfoShareAcademyParser()
    parser.load_page_html()
    parser.parse_all_previews()
    print(parser.found_post_previews)


if __name__ == '__main__':
    run_homework()
