from manim import *

class DrawTeX(Scene):
    def construct(self):

        #print("Write something")
        text ="|\\psi\\rangle = \\alpha |0\\rangle + \\beta |1\\rangle"
        text = MathTex(text).set_color(ORANGE)

        self.play(Write(text), run_time = 2)
        self.wait()
