from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None= None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode needs a tag")
        if self.children is None:
            raise ValueError("ParentNode needs children nodes")
        ans = f"<{self.tag}>"
        for child in self.children:
            to_append = child.to_html()
            ans = ans + to_append
        return ans + f"</{self.tag}>"