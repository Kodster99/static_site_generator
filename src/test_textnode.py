import unittest
import os

from textnode import split_nodes_delimiter, TextNode, TextType

print("Current directory:", os.getcwd())

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a different text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
   
    def test_diff_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_diff_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a link", TextType.LINK, "https://google.com.au")
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a link", TextType.LINK, None)
        node2 = TextNode("This is a link", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_simple_split(self):
         node = TextNode("Text with a **bold** word", TextType.NORMAL_TEXT)

         new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

         expected_output = [
             TextNode("Text with a ", TextType.NORMAL_TEXT),
             TextNode("bold", TextType.BOLD_TEXT),
             TextNode(" word", TextType.NORMAL_TEXT)
         ]
         self.assertEqual(new_nodes, expected_output)
    


if __name__ == "__main__":
    unittest.main()