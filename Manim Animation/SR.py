from manim import *

class Minkowski_2D(Scene):
    def construct(self):
        axes = Axes(x_range = [-11,11],y_range = [-11,11], x_length = 6, y_length = 6, tips = True)
        
        labels = axes.get_axis_labels(x_label = "x", y_label = "t")
        
        self.play(DrawBorderThenFill(axes), run_time = 2)
        self.add(labels)
        self.wait()

class Minkowski_3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        
        i = MathTex("x")
        j = MathTex("y")
        k = MathTex("t")
        x_label = axes.get_x_axis_label(i)
        y_label = axes.get_y_axis_label(j)
        z_label = axes.get_z_axis_label(k)
        labels = [x_label,y_label,z_label]

        self.play(DrawBorderThenFill(axes),run_time = 2)
        self.add(*labels)
        self.wait()

class CircularMotion(ThreeDScene):
    def construct(self):
        #Draw 2D axes
        axes = ThreeDAxes(x_length = 10,y_length = 10)
        i = MathTex("x")
        j = MathTex("y")
        x_label = axes.get_x_axis_label(i)
        y_label = axes.get_y_axis_label(j)
        self.play(DrawBorderThenFill(axes), run_time = 2)
        self.play(Write(x_label),Write(y_label))
        self.wait()

        # def dot_position(mobject):
        #     mobject.set_value(dot.get_center()[0]).set_color(BLUE)
        #     mobject.next_to(dot)

        dot = Dot([2,0,0]).set_color(BLUE)
        #label = DecimalNumber()
        # label.add_updater(dot_position)
        self.add(dot)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))
        self.move_camera(phi=65*DEGREES, theta = -45*DEGREES)
        self.begin_ambient_camera_rotation(rate = 0.2)
        
        k = MathTex("t")
        z_label = axes.get_z_axis_label(k)

        self.play(Write(z_label))
        self.wait()

        graph = ParametricFunction(lambda t : np.array([2*np.cos(t),2*np.sin(t),t/2]),t_range = [0,2*np.pi]).set_color(BLUE)
        self.play(Create(graph),run_time = 5)

        
        self.wait(5)
        
class LorentzTransforms(Scene):
    def construct(self):
        range = 11
        axes = Axes(x_range = [-range,range],y_range = [-range,range], x_length = 6, y_length = 6, tips = True)
        axes.shift(LEFT*3)
        
        labels = axes.get_axis_labels(x_label = "x", y_label = "t")
        
        self.play(DrawBorderThenFill(axes), run_time = 2)
        self.add(labels)
        self.wait()

        transforms_tex = MathTex("\\begin{cases} & t^\\prime = \\gamma(v) \\left(t - \\frac{vx}{c^2}\\right) \\\\ & x^\\prime = \\gamma (x-vt) \\end{cases}")
        self.play(Write(transforms_tex.next_to(axes, direction = np.array([2,0,0]))))

        v_list = np.array([0,0.1,0.5,0.75,0,-0.1,-0.5]) #/c , with c = 1
        gamma_list = 1/np.sqrt(1-v_list**2)

        v = v_list[0]
        gamma = gamma_list[0]
        #[x',t'] = [y(x-vt),y(t-vx)], y = gamma
        t_prime = Line(start = axes.coords_to_point(0,0), end = axes.coords_to_point(range*gamma*(-v*1),range*gamma*(1)), stroke_color = BLUE).add_tip() # t=1,x=0
        x_prime = Line(start = axes.coords_to_point(0,0), end = axes.coords_to_point(range*gamma*(1),range*gamma*(-v*1)), stroke_color = BLUE).add_tip() # t=0,x=1
        x_label = MathTex("x^\\prime").next_to(x_prime).set_color(BLUE)
        t_label = MathTex("t^\\prime").next_to(t_prime).set_color(BLUE)

        v_label = MathTex("\\gamma(v)=\\gamma("+str(v)+")="+str(gamma)).next_to(axes,np.array([1.5,0.01,0]))
        self.play(Write(v_label), run_time=1)
        
        for v,gamma in zip(v_list,gamma_list):
            t_prime_new = Line(start = axes.coords_to_point(0,0), end = axes.coords_to_point(range*gamma*(-v*1),range*gamma*(1)), stroke_color = BLUE).add_tip() # t=1,x=0
            x_prime_new = Line(start = axes.coords_to_point(0,0), end = axes.coords_to_point(range*gamma*(1),range*gamma*(-v*1)), stroke_color = BLUE).add_tip() # t=0,x=1
            x_label_new = MathTex("x^\\prime").next_to(x_prime_new).set_color(BLUE)
            t_label_new = MathTex("t^\\prime").next_to(t_prime_new).set_color(BLUE)
            
            v_label_new = MathTex("\\gamma(v)=\\gamma("+str(v)+")="+str(gamma)).next_to(axes,np.array([1.5,0.01,0]))
            
            self.play(Transform(v_label,v_label_new),
                    Transform(t_prime,t_prime_new),
                    Transform(x_prime,x_prime_new),
                    Transform(x_label,x_label_new),
                    Transform(t_label,t_label_new),run_time = 2)

            self.wait()