from dataclasses import dataclass
import requests as requests


@dataclass
class PostPreview:
    course_type: str
    title: str


class InfoShareAcademyParser:
    PAGE_URL = "https://infoshareacademy.com"

    def __init__(self):
        self.page_html = None
        self.last_post_index = 0
        self.found_post_previews = []

    def load_page_html(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.page_html = response.text

    def parse_all_previews(self):
        while True:
            try:
                self.search_for_next_post_preview()
            except ValueError:
                return

    def search_for_next_post_preview(self):
        course_type, course_type_index = self._find_publish_date()
        title, title_index = self._find_title(course_type_index)
        self.last_post_index = title_index
        self.found_post_previews.append(PostPreview(course_type, title))

    def _find_publish_date(self):
        span_marker_begin = self.page_html.index('<span class="top-label">', self.last_post_index) \
                            + len('<span class="top-label">')
        span_marker_end = self.page_html.index("</span>", span_marker_begin)
        return self.page_html[span_marker_begin:span_marker_end], span_marker_end + len('</span>')

    def _find_title(self, publish_date_index):
        title_open = self.page_html.index('<h3 class="title text--inter">', publish_date_index) \
                     + len('<h3 class="title text--inter">')
        title_close = self.page_html.index("</h3>", title_open)
        return self.page_html[title_open:title_close], title_close + len('</h3>')


def run_homework():
    parser = InfoShareAcademyParser()
    parser.load_page_html()
    parser.parse_all_previews()
    print(parser.found_post_previews)


if __name__ == '__main__':
    run_homework()
