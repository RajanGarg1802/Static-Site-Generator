import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_Children(self):
        node = HTMLNode("a", "Link to Google", None, {"href" : "https://www.google.com"})
        print(node.props_to_html())

    def test_none(self):
        node = HTMLNode()
        print(node.props_to_html())