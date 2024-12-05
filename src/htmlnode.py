

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
        elif self.tag is None:
            return self.value
       
        items = []
        for key, value in self.props.items():
            formatted = f'{key}="{value}"'
            items.append(formatted)
        
        attributes_string = self.props_to_html()
            
        return f"<{self.tag}{attributes_string}>{self.value}</{self.tag}>"



            