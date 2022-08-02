from manim import *

class position_line(Scene):
    def construct(self):

        # dot1 = Dot([-3,0,0])
        # dot2 = Dot([3,0,0])
        real_line = NumberLine(x_range = [-10,10,1],
                            length = 15,
                            include_numbers = True).set_color(ORANGE)

        x = 3
        point = real_line.number_to_point(x)
        dot = Dot(point).set_color(ORANGE)
        label = MathTex("|x\\rangle = |"+str(x)+"\\rangle").next_to(dot,UP).set_color(ORANGE)

        self.add(real_line)
        self.wait(2)
        self.add(dot)
        self.play(Write(label),run_time = 1)
        self.wait(2)

class continuous_position_line(Scene):
    def construct(self):

        real_line = NumberLine(x_range = [-10,10,1],
                            length = 15).set_color(ORANGE)

        x_list = [2,-1.5,np.pi,np.e]

        x = x_list[0]
        point = real_line.number_to_point(x)
        dot = Dot(point).set_color(ORANGE)
        label = MathTex("|x\\rangle = |"+str(x)+"\\rangle").next_to(dot,UP).set_color(ORANGE)

        self.add(real_line)
        for x in x_list:

            point_new = real_line.number_to_point(x)
            dot_new = Dot(point_new).set_color(ORANGE)
            label_new = MathTex("|x\\rangle = |"+str(x)+"\\rangle").next_to(dot_new,UP).set_color(ORANGE)

            self.play(Transform(dot,dot_new),Transform(label,label_new),run_time = 1.5)
            self.wait()
            
class norm_squared(Scene):
    def construct(self):
        plane1 = NumberPlane(x_range = [-10,10,1], y_range = [-5,5,1], x_length = 6, y_length = 2.5)
        plane1.shift(np.array([-4.5,1.5,0]))

        plane2 = NumberPlane(x_range = [-10,10,1], y_range = [-5,5,1], x_length = 6, y_length = 2.5)
        plane2.shift(np.array([-4.5,-1.5,0]))

        c = 0
        f = 2.5
        sigma = 3
        A = 4
        
        graph1 = plane1.plot(lambda x : A * np.exp(-(x+c)**2 / sigma**2)*np.cos(f*(x+c)), x_range = [-10,10], color = RED)
        label1 = MathTex("Re\\{\\psi(x)\\}").next_to(graph1,UP).set_color(RED)
        
        graph2 = plane2.plot(lambda x : A * np.exp(-(x+c)**2 / sigma**2)*np.sin(f*(x+c)), x_range = [-10,10], color = BLUE)
        label2 = MathTex("Im\\{\\psi(x)\\}").next_to(graph2,DOWN).set_color(BLUE)
        
        #brace = BraceBetweenPoints(point_1 = graph1.get_center(), point_2 = graph2.get_center() )
        brace = Brace(VGroup(label1,label2,graph1,graph2),RIGHT)
        
        plane3 = NumberPlane(x_range = [-10,10,1], y_range = [-5,5,1], x_length = 6, y_length = 4)
        plane3.shift(np.array([4.5,0,0]))
        graph3 = plane3.plot(lambda x : A * np.exp(-2*(x+c)**2 / sigma**2),x_range=[-10,10], color = ORANGE)
        label3 = MathTex("|\\psi(x)|^2").next_to(graph3,LEFT).set_color(ORANGE)
        
        self.play(DrawBorderThenFill(plane1), DrawBorderThenFill(plane2), run_time = 2)
        #self.wait()
        self.play(Create(graph1),Write(label1), 
                Create(graph2), Write(label2),
                run_time = 1.5)
        self.wait()
        self.add(brace)
        self.wait()
        self.play(DrawBorderThenFill(plane3), run_time = 2)
        self.play(Create(graph3),Write(label3),
                run_time = 2)
        self.wait()
