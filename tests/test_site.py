from html.parser import HTMLParser
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://jakoda.ch/"
SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


class DocumentMetadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.canonical = None
        self.canonical_count = 0
        self.jsonld = []
        self._in_jsonld = False
        self._current_jsonld = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            name = attrs.get("name", "").lower()
            if name:
                self.meta.setdefault(name, []).append(attrs.get("content", ""))
        if tag == "link" and attrs.get("rel", "").lower() == "canonical":
            self.canonical_count += 1
            self.canonical = attrs.get("href")
        if tag == "script" and attrs.get("type", "").lower() == "application/ld+json":
            self._in_jsonld = True
            self._current_jsonld = []

    def handle_data(self, data):
        if self._in_jsonld:
            self._current_jsonld.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._in_jsonld:
            self.jsonld.append("".join(self._current_jsonld))
            self._in_jsonld = False
            self._current_jsonld = []


def parse_page(path):
    parser = DocumentMetadata()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def local_path_for_url(url):
    path = url.removeprefix(BASE_URL).strip("/")
    return ROOT / (path + "/index.html" if path else "index.html")


class SiteMetadataTests(unittest.TestCase):
    def test_every_demo_page_is_noindex(self):
        demo_pages = list((ROOT / "vorschlag").glob("*/index.html"))
        self.assertGreater(len(demo_pages), 0)
        for page in demo_pages:
            with self.subTest(page=page):
                robots = parse_page(page).meta.get("robots", [])
                self.assertEqual(len(robots), 1, "expected one robots meta tag")
                self.assertIn("noindex", robots[0].lower())

    def test_all_public_first_party_pages_have_canonical_metadata(self):
        pages = [
            ROOT / "index.html",
            ROOT / "privat/index.html",
            ROOT / "pc-reparatur/index.html",
            ROOT / "pc-einrichtung/index.html",
            ROOT / "unternehmen/index.html",
            ROOT / "ki-automation/index.html",
            ROOT / "ratgeber/index.html",
            ROOT / "impressum/index.html",
            ROOT / "datenschutz/index.html",
        ]
        for page in pages:
            with self.subTest(page=page):
                metadata = parse_page(page)
                self.assertEqual(metadata.canonical_count, 1)
                self.assertTrue(metadata.canonical)
                self.assertEqual(metadata.meta.get("robots"), ["index, follow"])

    def test_confirmed_experience_metrics_are_visible_on_homepage(self):
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("3’000+</b> betreute Kundinnen und Kunden", homepage)
        self.assertIn("&gt;97%</b> Kundenzufriedenheit", homepage)
        self.assertIn("Erfahrungs- und Zufriedenheitsangaben beziehen sich auf meine bisherige IT-Arbeit und Kundenprojekte", homepage)

    def test_json_ld_is_valid_json(self):
        for page in ROOT.glob("**/*.html"):
            for raw in parse_page(page).jsonld:
                with self.subTest(page=page):
                    json.loads(raw)

    def test_home_schema_has_no_unverified_rating_or_unconfirmed_hours(self):
        metadata = parse_page(ROOT / "index.html")
        business = json.loads(metadata.jsonld[0])
        self.assertNotIn("aggregateRating", business)
        self.assertNotIn("openingHoursSpecification", business)
        self.assertNotIn("geo", business)
        self.assertNotIn("address", business)

    def test_robots_and_sitemap_are_valid_and_sitemap_urls_exist(self):
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn("Sitemap: https://jakoda.ch/sitemap.xml", robots)
        tree = ET.parse(ROOT / "sitemap.xml")
        urls = [node.text for node in tree.findall("sm:url/sm:loc", SITEMAP_NS)]
        self.assertEqual(len(urls), len(set(urls)))
        for url in urls:
            with self.subTest(url=url):
                self.assertTrue(url.startswith(BASE_URL))
                self.assertTrue(local_path_for_url(url).is_file())
                page = local_path_for_url(url)
                metadata = parse_page(page)
                robots = metadata.meta.get("robots", [])
                self.assertEqual(len(robots), 1)
                self.assertNotIn("noindex", robots[0].lower())
                self.assertEqual(metadata.canonical_count, 1)
                self.assertEqual(metadata.canonical, url)


if __name__ == "__main__":
    unittest.main()
