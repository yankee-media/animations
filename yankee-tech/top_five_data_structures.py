from manim import *

class Lists(Scene):

    def construct(self):

        blocks = [
            Square(),
            Square(),
            Square(),
            Square(),
            Square(),
            Square()
        ]

        self.play(Create(blocks[1]))

