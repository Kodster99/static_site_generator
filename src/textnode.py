from enum import Enum

class TextType(Enum):
	NORMAL_TEXT = "text"
	BOLD_TEXT = "bold"
	ITALIC_TEXT = "italic"
	CODE_TEXT = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode():
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url
	
	def __eq__(self, other):
		return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)
			
		

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"
	
def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_list = []
	for node in old_nodes:
		if node.text_type != TextType.NORMAL_TEXT:
			new_list.append(node)
		if node.text_type == TextType.NORMAL_TEXT:
			segments = node.text.split(delimiter)
			for index, segment in enumerate(segments):
				if index % 2 == 0:
					new_list.append(TextNode(segment, TextType.NORMAL_TEXT))
				else:
					new_list.append(TextNode(segment, text_type))
	return new_list