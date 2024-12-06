from textnode import TextType, TextNode

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        if props is None:
            props = {}
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""
        items = []
        for key, value in self.props.items():
            formatted = f' {key}="{value}"'
            items.append(formatted)
        return "".join(items)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        if props is None:
            props = {}
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return self.value
       
        items = []
        for key, value in self.props.items():
            formatted = f'{key}="{value}"'
            items.append(formatted)
        
        attributes_string = self.props_to_html()
            
        return f"<{self.tag}{attributes_string}>{self.value}</{self.tag}>"



class ParentNode(HTMLNode):
    def __init__(self, children, tag, props=None):
        if not tag or not children:
            raise ValueError("Tag and children cannot be None or empty!")
        # Initialize using the parent class's constructor
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Node needs a tag!")
        if not self.children:
            raise ValueError("Node needs children!")
        
        # Convert children to HTML recursively and concatenate
        children_html = ''.join(
            child.to_html() if child.tag else child.value 
            for child in self.children
                )
        return f"<{self.tag}>{children_html}</{self.tag}>"
    

def text_node_to_html_node(text_node):
    if text_node is None or not isinstance(text_node, TextNode):
        raise Exception("Must be a text type!")
    if text_node.text_type == TextType.NORMAL_TEXT:
        return LeafNode(text_node.text)
    if text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode(text_node.text, "b")
    if text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode(text_node.text, "i")
    if text_node.text_type == TextType.CODE_TEXT:
        return LeafNode(text_node.text, "code")
    if text_node.text_type == TextType.IMAGE:
        props = {
        "src": text_node.url,
        "alt": text_node.text
        }
        return LeafNode("", "img", props)
    if text_node.text_type == TextType.LINK:
        props = {
            "href": text_node.url
        }
        return LeafNode(text_node.text, "a", props)
    else:
        raise Exception("Couldn't find valid text type!")