import unittest
from textnode import TextNode, TextType

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
        
if __name__ == "__main__":
    unittest.main()