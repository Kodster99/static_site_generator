import unittest

from htmlnode import HTMLNode


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
