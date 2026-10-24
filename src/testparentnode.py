import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_first = LeafNode("b", "firstChild")
        grandchild = LeafNode("span", "grandchild")
        child_second = ParentNode("div", [grandchild])
        parent_node = ParentNode("p", [child_first, child_second])
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>firstChild</b><div><span>grandchild</span></div></p>",
        )
