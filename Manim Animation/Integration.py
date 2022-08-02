from curses.textpad import rectangle
from manim import *

class Work_ex(Scene):
    def construct(self):   
        plane = NumberPlane(x_range = [-10,10],y_range = [-10,10],x_length = 20,y_length = 20)
        plane.add_coordinates()

        graph1 = plane.plot(lambda x : 1, x_range = [0,2], color = GREEN)
        #graph2 = plane.plot(lambda x : -1, x_range = [0,10])

        area1 = plane.get_area(graph = graph1, x_range = [0,2], color = GREEN)
        #area2 = plane.get_area(graph = graph2, x_range = [0,10], color = YELLOW)

        self.play(DrawBorderThenFill(plane), run_time = 1)
        self.wait()
        self.play(Create(graph1), run_time = 1)
        #self.play(Create(graph2), run_time = 1)
        self.wait()
        self.play(FadeIn(area1))#,FadeIn(area2))
        self.wait()

class Work_ex2(Scene):
    def construct(self):   
        plane = NumberPlane(x_range = [-10,10],y_range = [-10,10],x_length = 20,y_length = 20)
        plane.add_coordinates()

        graph1 = plane.plot(lambda x : x, x_range = [0,2], color = GREEN)
        #graph2 = plane.plot(lambda x : -1, x_range = [0,10])

        area1 = plane.get_area(graph = graph1, x_range = [0,2], color = GREEN)
        #area2 = plane.get_area(graph = graph2, x_range = [0,10], color = YELLOW)

        self.play(DrawBorderThenFill(plane), run_time = 1)
        self.wait()
        self.play(Create(graph1), run_time = 1)
        #self.play(Create(graph2), run_time = 1)
        self.wait()
        self.play(FadeIn(area1))#,FadeIn(area2))
        self.wait()

class Work_ex3(Scene):
    def construct(self):   
        plane = NumberPlane(x_range = [-5,5],y_range = [-5,5],x_length = 10,y_length = 10)
        plane.add_coordinates()

        graph1 = plane.plot(lambda x : 0.5*x*3 + 1, x_range = [0,2], color = GREEN)
        #graph2 = plane.plot(lambda x : -1, x_range = [0,10])

        area1 = plane.get_area(graph = graph1, x_range = [0,2], color = GREEN)
        #area2 = plane.get_area(graph = graph2, x_range = [0,10], color = YELLOW)

        self.play(DrawBorderThenFill(plane), run_time = 1)
        self.wait()
        self.play(Create(graph1), run_time = 1)
        #self.play(Create(graph2), run_time = 1)
        self.wait()
        self.play(FadeIn(area1))#,FadeIn(area2))
        self.wait()


class RiemannSum(Scene):
    def construct(self):   
        plane = NumberPlane(x_range = [-10,10],y_range = [-10,10],x_length = 20,y_length = 20)
        plane.add_coordinates()

        c = 0
        f = 2.5
        sigma = 3
        A = 4
        graph = plane.plot(lambda x : A * np.exp(-(x+c)**2 / sigma**2)*np.sin(f*(x+c)), x_range = [-10,10], color = GREEN)
        label = MathTex("f(x) = 4e^{-\\frac{x^2}{3^2} } \\sin{2.5 \\cdot x}").next_to(4,UP).set_color(GREEN)
        #label = MathTex("f(x)").next_to(4,UP).set_color(GREEN)
        
        dx_list = [1,0.5,0.3, 0.1,0.05,0.01]
        rectangles = VGroup(
            *[
                plane.get_riemann_rectangles(
                    graph = graph,
                    x_range = [-10,10],
                    stroke_width = 0.1,
                    stroke_color = BLUE,
                    dx = dx,
                    input_sample_type = "center")
                    for dx in dx_list
            ]
        )


        self.play(DrawBorderThenFill(plane), run_time = 1)
        self.wait()
        self.play(Create(graph), Write(label), run_time = 1)
        self.wait()
        
        first_area = rectangles[0]
        for k in range(1,len(dx_list)):
            new_area = rectangles[k]
            self.play(Transform(first_area,new_area), run_time = 2)
            self.wait()

        self.wait()
        