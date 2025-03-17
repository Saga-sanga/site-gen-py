from textnode import TextNode, TextType


def main():
    text_node = TextNode("Some random anchor", TextType.LINK, "https://sanga.net")
    print(text_node)


main()
