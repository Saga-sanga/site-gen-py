import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_values(self):
        node = HTMLNode("h1", "Click", None, {"class": "primary"})
        self.assertEqual(
            "HTMLNode(h1, Click, children: None, {'class': 'primary'})", repr(node)
        )

    def test_eq_props(self):
        node = HTMLNode(
            "h1", "Click", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )

    def test_eq_props2(self):
        node = HTMLNode("h1", "Click", None, {"href": "https://www.google.com"})
        self.assertEqual(' href="https://www.google.com"', node.props_to_html())


if __name__ == "__main__":
    unittest.main()
