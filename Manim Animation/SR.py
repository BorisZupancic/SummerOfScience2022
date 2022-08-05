from manim import *

class Minkowski_2D(Scene):
    def construct(self):
        axes = Axes(x_range = [-11,11],y_range = [-11,11], x_length = 6, y_length = 6, tips = True)
        
        labels = axes.get_axis_labels(x_label = "x", y_label = "t")
        
        self.play(DrawBorderThenFill(axes), run_time = 2)
        self.add(labels)
        self.wait()

class InertialTransport_2D(Scene):
    def construct(self):
        x_max = 4
        y_max = 3
        axes = Axes(x_range = [-3*x_max,3*x_max],y_range = [-3*y_max,3*y_max], x_length = 2*x_max, y_length = 2*y_max, tips = True)
        
        labels = axes.get_axis_labels(x_label = "x", y_label = "t")
        
        v1 = np.array([3,4])
        vector1 = Line(start = axes.coords_to_point(0,0), end = axes.coords_to_point(v1[0],v1[1]), stroke_color = BLUE).add_tip()
		
        graph = axes.plot(function = lambda x : (v1[1]/v1[0])*x,x_range = [-11,11]).set_color(BLUE)

        self.play(DrawBorderThenFill(axes), run_time = 2)
        self.add(labels)
        self.wait()
        self.play(GrowFromPoint(vector1, point = vector1.get_start()), run_time = 1)
        self.wait()
        self.play(Transform(vector1,graph), run_time = 2)
        self.wait(5)

class ParallelTransport_2D(Scene):
    def construct(self):
        x_max = 4
        y_max = 3
        axes = Axes(x_range = [-2*x_max,2*x_max],y_range = [-5*y_max,5*y_max], x_length = 3*x_max, y_length = 2*y_max, tips = True)
        
        labels = axes.get_axis_labels(x_label = "x", y_label = "t")
        
        f = lambda x : 0.05*x**3-0.5*x**2
        x_init = -4
        x_fin = 8
        v1 = np.array([-3,4])
        
        vector1 = Line(start = axes.coords_to_point(x_init,f(x_init)), end = axes.coords_to_point(v1[0]+x_init,v1[1]+f(x_init)), stroke_color = RED).add_tip()
		
        vector2 = Line(start = axes.coords_to_point(x_fin,f(x_fin)), end = axes.coords_to_point(v1[0]+x_fin,v1[1]+f(x_fin)), stroke_color = RED).add_tip()
		
        graph = axes.plot(function = f,x_range = [-11,11]).set_color(BLUE)
        #Path to move along:
        #shifted horizontally by v1[0]/2, vertically by v1[1]/2
        path = axes.plot(function = lambda x : 0.05*(x-v1[0]/2)**3-0.5*(x-v1[0]/2)**2 + v1[1]/2,x_range = [x_init+v1[0]/2,x_fin+v1[0]/2]).set_color(BLUE)

        self.play(DrawBorderThenFill(axes), run_time = 2)
        self.play(Write(labels))
        self.wait()
        self.play(Create(graph))
        self.wait()
        self.play(GrowFromPoint(vector1, point = vector1.get_start()), run_time = 1)
        self.wait()
        self.play(MoveAlongPath(vector1,path,run_time=2))
        self.wait(5)


class Multi_InertTrans_2D(Scene):
    def construct(self):
        x_max = 4
        y_max = 3
        axes = Axes(x_range = [-3*x_max,3*x_max],y_range = [-3*y_max,3*y_max], x_length = 2*x_max, y_length = 2*y_max, tips = True)
        
        labels = axes.get_axis_labels(x_label = "x", y_label = "t")
        self.play(DrawBorderThenFill(axes), run_time = 2)
        self.add(labels)
        self.wait()
        
        
        v1 = np.array([3,4])
        vector1 = Line(start = axes.coords_to_point(0,0), end = axes.coords_to_point(v1[0],v1[1]), stroke_color = BLUE).add_tip()
        graph1= axes.plot(function = lambda x : (v1[1]/v1[0])*x,x_range = [-11,11]).set_color(BLUE)

        v2 = np.array([1,7])
        vector2 = Line(start = axes.coords_to_point(0,0), end = axes.coords_to_point(v2[0],v2[1]), stroke_color = RED).add_tip()
        graph2 = axes.plot(function = lambda x : (v2[1]/v2[0])*x,x_range = [-11,11]).set_color(RED)

        v3 = np.array([-3,6])
        vector3 = Line(start = axes.coords_to_point(0,0), end = axes.coords_to_point(v3[0],v3[1]), stroke_color = GREEN).add_tip()
        graph3 = axes.plot(function = lambda x : (v3[1]/v3[0])*x,x_range = [-11,11]).set_color(GREEN)

        v4 = np.array([-2,-6])
        vector4 = Line(start = axes.coords_to_point(0,0), end = axes.coords_to_point(v4[0],v4[1]), stroke_color = YELLOW).add_tip()
        graph4 = axes.plot(function = lambda x : (v4[1]/v4[0])*x,x_range = [-11,11]).set_color(YELLOW)
        
        self.play(GrowFromPoint(vector1, point = vector1.get_start()), 
                GrowFromPoint(vector2, point = vector2.get_start()),
                GrowFromPoint(vector3, point = vector3.get_start()),
                GrowFromPoint(vector4, point = vector4.get_start()),run_time = 1)
        self.wait()
        self.play(Transform(vector1,graph1),
                Transform(vector2,graph2),
                Transform(vector3,graph3),
                Transform(vector4,graph4), run_time = 2)
            
        self.wait(5)
        

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