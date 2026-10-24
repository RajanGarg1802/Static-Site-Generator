import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):    
        nodeFirst = TextNode("This is first node", TextType.ITALIC)
        nodeSecond = TextNode("This is second node", TextType.ITALIC)
        self.assertNotEqual(nodeFirst, nodeSecond)

    def test_whoknows(self):
        nodeA = TextNode("A", TextType.LINK, None)
        nodeB = TextNode("A", TextType.LINK)
        self.assertNotEqual(nodeA, nodeB)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_anchor(self):
        node = TextNode("This is an anchor node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is an anchor node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

if __name__ == "__main__":
    unittest.main()