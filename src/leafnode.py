from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None):
       super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All Leaf Nodes must have a value")

        if self.tag is None:
            return self.value

        ans = f'<{self.tag}'
        if self.props:
            for key, val in self.props.items():
                ans = ans + ' ' + key + '="' + val + '"'
        ans = ans + '>' + self.value + f'</{self.tag}>'

        return ans

    def __repr__(self):
        print(f"Tag: {self.tag}")
        print(f"Value: {self.value}")
        print(f"Attributes: {self.props}")