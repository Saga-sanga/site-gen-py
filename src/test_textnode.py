import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_content(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_diff_url(self):
        node = TextNode("Click now", TextType.LINK, "https://www.google.com")
        node2 = TextNode("Click now", TextType.LINK, "https:www.amazon.com")
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("Click now", TextType.LINK, "https://www.google.com")
        node2 = TextNode("Click now", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a test node", TextType.BOLD, "https://recksonk.in")
        self.assertEqual(
            "TextNode(This is a test node, bold, https://recksonk.in)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
