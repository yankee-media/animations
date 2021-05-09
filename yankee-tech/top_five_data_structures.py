from manim import *
from common import generic_object_symbol


class Lists(Scene):

    def construct(self):

        object_symbol = Text(generic_object_symbol)
        blocks = [
            Square(side_length=1.25).move_to(LEFT * 3),
            Square(side_length=1.25),
            Square(side_length=1.25),
            Square(side_length=1.25),
            Square(side_length=1.25)
        ]

        for idx, block in enumerate(blocks[1:]):
            block.next_to(blocks[idx])

        self.play(*[Create(block) for block in blocks])
        self.wait(2)


class LinkedLists(Scene):

    def construct(self):

        blocks = [
            Square(),
            Square(),
            Square(),
            Square(),
            Square(),
            Square()
        ]


class BinaryTrees(Scene):

    def construct(self):

        blocks = [
            Circle(),
            Circle(),
            Circle(),
            Circle(),
            Circle(),
            Circle()
        ]


class Graphs(Scene):

    def construct(self):

        blocks = [
            Circle(),
            Circle(),
            Circle(),
            Circle(),
            Circle(),
            Circle()
        ]


class HashTables(Scene):

    def construct(self):
        pass

