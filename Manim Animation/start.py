from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
        
class CoordinateSystemExample(Scene):
    def construct(self):
        axes = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-1, 10),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-2, 2, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            height=6,
            width=10,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        self.add(axes)

        # Axes descends from the CoordinateSystem class, meaning
        # you can call call axes.coords_to_point, abbreviated to
        # axes.c2p, to associate a set of coordinates with a point,
        # like so:
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
        self.wait()

        # Similarly, you can call axes.point_to_coords, or axes.p2c
        # print(axes.p2c(dot.get_center()))

        # We can draw lines from the axes to better mark the coordinates
        # of a given point.
        # Here, the always_redraw command means that on each new frame
        # the lines will be redrawn
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.play(dot.animate.move_to(axes.c2p(3, -2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(1, 1)))
        self.wait()

        # If we tie the dot to a particular set of coordinates, notice
        # that as we move the axes around it respects the coordinate
        # system defined by them.
        f_always(dot.move_to, lambda: axes.c2p(1, 1))
        self.play(
            axes.animate.scale(0.75).to_corner(UL),
            run_time=2,
        )
        self.wait()
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))

        # Other coordinate systems you can play around with include
        # ThreeDAxes, NumberPlane, and ComplexPlane.
