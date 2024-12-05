import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
        tag="a",
        value="Click me!",
        children=None,
        props={"href": "https://google.com", "target": "_blank"}
    )
        assert node.props_to_html() == ' href="https://google.com" target="_blank"'

    def test_no_props(self):
        node = HTMLNode(
        tag="q",
        value="Click me!",
        children=None,
        props=None   
         )
        assert node.props_to_html() == ""

    def test_multiple_props(self):
        node = HTMLNode(
        tag="c",
        value="Goodbye",
        children=None,
        props={
            "href": "https://google.com", 
            "target": "_blank",
            "class": "link",
            "id": "main-link"
        }
    )
        assert node.props_to_html() == ' href="https://google.com" target="_blank" class="link" id="main-link"'

    def test_empty_props(self):
        node1 = HTMLNode(
        tag="g",
        value="Hello",
        children=None,
        props={}
        )
        assert node1.props_to_html() == ""

        node2 = HTMLNode(
        tag="g",
        value="Hello",
        children=None,
        props=None
        )
        assert node1.props_to_html() == ""


    def test_to_html(self):
        node = LeafNode(
        tag="a",
        value="Click me!",
        props={"href": "https://google.com", "target": "_blank"}
    )
        assert node.to_html() == '<a href="https://google.com" target="_blank">Click me!</a>'

    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(
                tag="a",
                value=None,
                props={"href": "https://google.com", "target": "_blank"}
            )
            node.to_html()


    def test_no_tag(self):
        node = LeafNode(
        tag=None,
        value="Click me!",
        props={"href": "https://google.com", "target": "_blank"}
    )
        assert node.to_html() == 'Click me!'

    def test_empty_props(self):
        node = LeafNode(
        tag="span",
        value="Just text",
        props={}
    )
        assert node.to_html() == '<span>Just text</span>'

    def test_minimal_node(self):
        node = LeafNode(
        tag="p",
        value="Simple paragraph"
    )
        assert node.to_html() == '<p>Simple paragraph</p>'