class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list[HTMLNode] | None = None, props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not yet implemented")

    def props_to_html(self):
        if not self.props:
            return None
        ans = ""
        for key in self.props:
            ans = ans + " " +  key + "=" + self.props[key]
        return ans

    def __repr__(self):
        print(f"Tag: {self.tag}")
        print(f"Value: {self.value}")
        print(f"Children: {self.children}")
        print(f"Attributes: {self.props}")


    