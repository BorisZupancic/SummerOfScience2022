import math
from manim import *

class Signal(Scene):
    def construct(self):
        plane = NumberPlane(x_range = [-10,10], y_range = [-5,5], x_length = 20, y_length = 6)
        
        f = 10
        A1 = 5
        A2 = 3
        graph = plane.plot(lambda x : (A1*np.exp(-(x+5)**2)+A2*np.exp(-(x-3)**2 / 2**2))*np.sin(f*x)).set_color(BLUE)

        self.play(DrawBorderThenFill(plane),run_time = 1)
        self.wait()
        self.play(Create(graph),run_time = 2)
        self.wait()

class sine(Scene):
    def construct(self):
        plane = NumberPlane(x_range = [-10,10], y_range = [-5,5], x_length = 20, y_length = 6)
        plane.shift(DOWN)
        plane.add_coordinates()

        self.play(DrawBorderThenFill(plane))


        f_list = [1,2,5,0.9,0.5]
        graph = plane.plot(lambda x : np.sin(f_list[0]*x)).set_color(BLUE)
        label = MathTex("\\sin("+f"{f_list[0]}"+"x)").next_to(plane,UP)

        self.play(Create(graph),Write(label),run_time = 2)
        self.wait()
        for f in f_list[1:]:
            graph_new  = plane.plot(lambda x : np.sin(f*x)).set_color(BLUE)
            label_new = MathTex("\\sin("+f"{f}"+"x)").next_to(plane,UP)

            self.play(Transform(graph,graph_new, path_func = straight_path()),
                    Transform(label,label_new),
                    run_time = 2)
            self.wait()

        A_list = [1,3,0.5]
        for A in A_list:
            graph_new  = plane.plot(lambda x : A*np.sin(x)).set_color(BLUE)
            label_new = MathTex(f"{A}\\sin(x)").next_to(plane,UP)

            self.play(Transform(graph,graph_new, path_func = straight_path()),
                    Transform(label,label_new),
                    run_time = 2)
            self.wait()

        phase_list = np.pi*np.array([0,0.5,1,2,-0.5])
        for phase_shift in phase_list:
            graph_new  = plane.plot(lambda x : np.sin(x+phase_shift)).set_color(BLUE)
            label_new = MathTex(f"\\sin(x+ ({phase_shift/np.pi})\\pi)").next_to(plane,UP)

            self.play(Transform(graph,graph_new, path_func = straight_path()),
                    Transform(label,label_new),
                    run_time = 2)
            self.wait()

class square_wave(Scene):
    def construct(self):
        plane = NumberPlane(x_range = [-5,5], y_range = [-2,2], x_length = 20, y_length = 6)
        self.play(DrawBorderThenFill(plane))
        
        f = 0.5
        k_list = [i for i in range(1,20)]
        
        partial_graph = plane.plot(function = lambda x : (4/np.pi)*np.sin(f*x*2*np.pi*(-1))/(-1)).set_color(RED)
        #self.play(Create(partial_graph))
        
        i = 0
        for k in k_list:
            #Draw the element in the sequence
            func_new = lambda x : (4/np.pi)*np.sin(f*x*2*np.pi*(2*k-1))/(2*k-1)
            
            graph_new = plane.plot(function=func_new).set_color(RED)
            self.play(Create(graph_new),run_time = 1)

            partial_series = lambda x : np.sum([(4/np.pi)*np.sin(f*x*2*np.pi*(2*k-1))/(2*k-1) for k in k_list[0:i+1]])
            partial_graph_new = plane.plot(function=partial_series).set_color(WHITE)

            self.play(ReplacementTransform(graph_new,partial_graph_new), ReplacementTransform(partial_graph,partial_graph_new), run_time=1)

            i += 1    
        self.wait(1)
        
class square_wave2(Scene):
    def construct(self):
        plane = NumberPlane(x_range = [-5,5], y_range = [-5,5], x_length = 20, y_length = 6)
        self.play(DrawBorderThenFill(plane))
        
        f = 0.5
        k_list = [i for i in range(1,41)]
        colors = [RED_A,BLUE_A,GREEN_A,YELLOW_A,PURPLE_A,
                RED_A,BLUE_A,GREEN_A,YELLOW_A,PURPLE_A,
                RED_A,BLUE_A,GREEN_A,YELLOW_A,PURPLE_A,
                RED_A,BLUE_A,GREEN_A,YELLOW_A,PURPLE_A,
                RED_A,BLUE_A,GREEN_A,YELLOW_A,PURPLE_A,
                RED_A,BLUE_A,GREEN_A,YELLOW_A,PURPLE_A,
                RED_A,BLUE_A,GREEN_A,YELLOW_A,PURPLE_A,
                RED_A,BLUE_A,GREEN_A,YELLOW_A,PURPLE_A]

        #graph = plane.plot(function = lambda x : (4/np.pi)*np.sin(f*x*2*np.pi*(-1))/(-1)).set_color(RED)
        #self.play(Create(graph))
        
        group = []

        for k,c in zip(k_list,colors):
            #Draw the element in the sequence
            func = lambda x : (4/np.pi)*np.sin(f*x*2*np.pi*(2*k-1))/(2*k-1)
            
            graph= plane.plot(function=func).set_color(c)
            self.play(Create(graph),run_time = 1)

            group.append(graph)
            

        partial_series = lambda x : np.sum([(4/np.pi)*np.sin(f*x*2*np.pi*(2*k-1))/(2*k-1) for k in k_list])
        partial_graph = plane.plot(function=partial_series).set_color(WHITE)

        self.wait(1)
        self.play(*[Transform(thing,partial_graph) for thing in group],run_time = 1)

class square_wave3(Scene):
    def construct(self):
        plane = NumberPlane(x_range = [-5,5], y_range = [-5,5], x_length = 20, y_length = 6)
        self.play(DrawBorderThenFill(plane))
        
        f = 0.5
        k_list = [i for i in range(1,10000)]

        partial_series = lambda x : np.sum([(4/np.pi)*np.sin(f*x*2*np.pi*(2*k-1))/(2*k-1) for k in k_list])
        partial_graph = plane.plot(function=partial_series).set_color(WHITE)

        self.play(Create(partial_graph,run_time = 1))
        self.wait(2)

class sawtooth(Scene):
    def construct(self):
        text ="f(x) = -\\frac{2}{\\pi} \\sum_{k=1}^{\\infty} \\frac{(-1)^k}{k}\\sin(2\\pi k x)"
        text = MathTex(text).set_color(ORANGE)

        self.play(Write(text), run_time = 2)
        self.wait()

        plane = NumberPlane(x_range = [-5,5], y_range = [-3,3], x_length = 20, y_length = 6)
        self.play(Transform(text,plane),run_time = 2)
        
        N=100
        k_list = [i for i in range(1,N+1)]

        group = []
        for k in k_list:
            func = lambda x : -(2/np.pi)*((-1)**k / k)*np.sin(2*np.pi*k*x)
            func_graph = plane.plot(function = func)
            group.append(func_graph)
        
        self.play(*[Create(graph) for graph in group],run_time=1)
        self.wait()

        final_graph = plane.plot(function = lambda x: np.sum([-(2/np.pi)*((-1)**k / k)*np.sin(2*np.pi*k*x) for k in k_list] ))
        self.play(*[Transform(graph,final_graph) for graph in group])
        self.wait()

class Gaussian(Scene):
    def construct(self):
        plane = NumberPlane(x_range = [-5,5], y_range = [-3,3], x_length = 20, y_length = 6)
        self.play(DrawBorderThenFill(plane))
            
        N=100
        n_list = [i for i in range(1,N+1)]
        

class sine_taylor(Scene):
    def construct(self):
        plane = NumberPlane(x_range = [-8*np.pi,8*np.pi], y_range = [-5,5], x_length = 20, y_length = 6)
        self.play(DrawBorderThenFill(plane))
        
        N=100
        n_list = [i for i in range(0,N+1)]
        factors = [( ((-1)**nn) / math.factorial(2*nn + 1)) for nn in n_list]
        
        group = []
        for n in n_list:
            func = lambda x : np.sum( [factor*x**(2*nn+1) for nn,factor in zip(n_list[0:n],factors[0:n])] )
            func_graph = plane.plot(function = func).set_color(RED)

            group.append(func_graph)

        graph = group[0]
        self.play(Create(graph),run_time=1)
        for graph_new in group:
            self.play(Transform(graph,graph_new), run_time = 1)
        self.wait(3)
            

