from manim import *

#vector1 = [1,2]

class vector(VectorScene):
	def construct(self):
		
		plane = self.add_plane(animate=True).add_coordinates()
		
		vector1 = self.add_vector([1,2],color = YELLOW)
		label1 = self.get_vector_label(vector = vector1, label ="\\vec{v}", at_tip = True)
		self.label_vector(vector = vector1,label = label1)
		#vector1 = np.array([1,2])
		#self.write_vector_coordinates(vector = vector1)
		#self.vector_to_coords(vector = vector1)
		#self.coords_to_vector(vector = vector1)
		#vector2 = self.add_vector([3,1],color = BLUE)
		#self.write_vector_coordinates(vector = vector2)

class TipTail_Addition(Scene):
	def construct(self):

		plane = NumberPlane(x_range = [-5,5,1],y_range = [-5,5,1],x_length = 10,y_length = 10)
		plane.add_coordinates()

		#The two vectors to add:
		v1 = np.array([3,-0.5])
		v2 = np.array([-2,3])
		vector1 = Line(start = plane.coords_to_point(0,0), end = plane.coords_to_point(v1[0],v1[1]), stroke_color = YELLOW).add_tip()
		vector1_name = MathTex("\\vec{v}").next_to(vector1, RIGHT, buff=0.1).set_color(YELLOW)
		vector2 = Line(start = plane.coords_to_point(0,0), end=plane.coords_to_point(v2[0],v2[1]), stroke_color = RED).add_tip()
		vector2_name = MathTex("\\vec{u}").next_to(vector2, LEFT, buff=0.1).set_color(RED)
		#What they add-up to:
		v3 = v1+v2
		vector3 = Line(start = plane.coords_to_point(0,0), end=plane.coords_to_point(v3[0],v3[1]), stroke_color = GREEN).add_tip()
		vector3_name = MathTex("\\vec{w} = \\vec{v}+\\vec{u}").next_to(vector3, LEFT, buff = 0.1).set_color(GREEN)
		
		#Where to place vector2:
		vector2_prime = Line(start = plane.coords_to_point(v1[0],v1[1]), end=plane.coords_to_point(v3[0],v3[1]), stroke_color = RED).add_tip()

	
		#stuff = VGroup(plane, vector1)

		self.play(DrawBorderThenFill(plane), run_time = 1)
		self.wait()
		self.play(GrowFromPoint(vector1, point = vector1.get_start()), Write(vector1_name), run_time = 2)
		self.wait()
		self.play(GrowFromPoint(vector2, point = vector2.get_start()), Write(vector2_name), run_time = 2)
		self.wait()
		self.play(Transform(vector2,vector2_prime), vector2_name.animate.next_to(vector2_prime,UP,buff=0.1), run_time = 2)
		self.wait()
		self.play(GrowFromPoint(vector3, point = vector3.get_start()), Write(vector3_name), run_time = 2)
		self.wait()


		
class basis(VectorScene):
	def construct(self):
		plane = self.add_plane(animate=True).add_coordinates()
		plane.add_coordinates()

		basis = self.get_basis_vectors()
		basis_labels = self.get_basis_vector_labels()
		for b,label in zip(basis,basis_labels):
			self.label_vector(vector = b, label = label)
			self.add_vector(vector = b)

		vector1 = self.add_vector([1,2],color = YELLOW)
		self.write_vector_coordinates(vector = vector1)
		#label1 = self.get_vector_label(vector = vector1, label = "\\vec{v}")
		#self.label_vector(vector = vector1, label = label1)

class basis3D(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
		
		i = Arrow3D(start = axes.coords_to_point(0,0,0), end = axes.coords_to_point(1,0,0),color = RED)
		j = Arrow3D(start = axes.coords_to_point(0,0,0), end = axes.coords_to_point(0,1,0),color = GREEN)
		k = Arrow3D(start = axes.coords_to_point(0,0,0), end = axes.coords_to_point(0,0,1),color = BLUE)

		i_label = MathTex("\\hat{i}").next_to(i)
		j_label = MathTex("\\hat{j}").next_to(j)
		k_label = MathTex("\\hat{k}").next_to(k)

		self.add(axes)
		self.add(i,j,k,i_label,j_label,k_label)
		self.wait()

class VectorFromBasis(VectorScene):
	def construct(self):
		plane = self.add_plane(animate=True).add_coordinates()
		plane.add_coordinates()

		basis = self.get_basis_vectors()
		basis_labels = self.get_basis_vector_labels()
		for b,label,color in zip(basis,basis_labels,[GREEN,RED]):
			self.label_vector(vector = b, label = label)
			self.add_vector(vector = b,color = color)

		#set up coordinates of vector:
		v = [1,2]

		basis0_prime = Line(start = plane.coords_to_point(0,0), end = plane.coords_to_point(v[0],0), color = GREEN).add_tip(tip_length = 0.25*v[0]**0.5, tip_width = 0.25*v[0]**0.5)
		basis0_prime_label = MathTex(f"{v[0]}"+"\\hat{\\imath}").next_to(basis0_prime).set_color(GREEN)
		
		basis1_prime = Line(start = plane.coords_to_point(0,0), end = plane.coords_to_point(0,v[1]), color = RED).add_tip(tip_length = 0.25*v[1]**0.5, tip_width = 0.25*v[1]**0.5)
		basis1_prime_label = MathTex(f"{v[1]}"+"\\hat{\\jmath}").next_to(basis1_prime, LEFT).set_color(RED)

		self.play(Transform(basis[0],basis0_prime), 
				Transform(basis_labels[0],basis0_prime_label), 
				Transform(basis[1],basis1_prime),
				Transform(basis_labels[1],basis1_prime_label), run_time = 1)
		self.wait()

		vector1 = self.add_vector(v,color = YELLOW)
		self.write_vector_coordinates(vector = vector1)

		#Draw the dotted lines from basis:
		line_i = Line(start = plane.coords_to_point(v[0],0), end = plane.coords_to_point(v[0],v[1]))
		line_j = Line(start = plane.coords_to_point(0,v[1]), end = plane.coords_to_point(v[0],v[1]))
		self.play(GrowFromPoint(line_i,point = line_i.get_start()), GrowFromPoint(line_j,point = line_j.get_start()))
		#vect1 = self.add_vector([1,2],color = YELLOW)
		#self.coords_to_vector(vector = vect1)

		
class LinearCombinations(Scene):
	def construct(self):
		#Create the plane
		plane = NumberPlane(x_range = (-15,15,1),y_range = (-15,15,1),x_length = 30,y_length = 30)
		#plane.add_coordinates()
		
		def vector(v,direction,color,label):
			vector = Line(start = plane.coords_to_point(0,0), end = plane.coords_to_point(v[0],v[1]), stroke_color = color).add_tip()
			vector_name = MathTex("\\vec{"+label+"}").next_to(vector, direction, buff=0.1).set_color(color)
			return vector, vector_name

		#List of scalar multipliers for vectors:
		v1_list = [1,2,-3,4] 
		v2_list = [1,0.5,2,-1]

		#The two vectors to for the basis:
		v1 = np.array([3,2])/2
		v2 = np.array([-4,1])/2


		#Set up the Linear Combinations to go through
		vector1_group = [vector(scale*v1,RIGHT,YELLOW,f"{scale}v") for scale in v1_list]
		vector2_group = [vector(scale*v2,LEFT,RED,f"{scale}u") for scale in v2_list]
		
		vector3_group = [vector(scale1*v1+scale2*v2,RIGHT,GREEN, "w") for scale1,scale2 in zip(v1_list,v2_list)]
		
		#Draw the dotted lines from basis:
		def connecting_lines(vect1,vect2):
			vect3 = vect1+vect2

			line_v1 = Line(start = plane.coords_to_point(vect1[0],vect1[1]), end = plane.coords_to_point(vect3[0],vect3[1]))
			line_v2 = Line(start = plane.coords_to_point(vect2[0],vect2[1]), end = plane.coords_to_point(vect3[0],vect3[1]))
			#self.play(GrowFromPoint(line_i,point = line_i.get_start()), GrowFromPoint(line_j,point = line_j.get_start()))
			return line_v1,line_v2

		lines_group = [
			[connecting_lines(scale1*v1,scale2*v2)[0],connecting_lines(scale1*v1,scale2*v2)[1]] 
			for scale1,scale2 in zip(v1_list,v2_list)
		]

		print(lines_group)
		line1_group = [lines[0] for lines in lines_group]
		line2_group = [lines[1] for lines in lines_group]

		print(line1_group)
		print(line2_group)


		#ANIMATE:
		#1. Draw Plane
		self.play(DrawBorderThenFill(plane), run_time = 1)
		self.wait()
		
		#2. Draw initial v1,v2,v3
		vect1,vect2,vect3,line1,line2 = [vector1_group[0],vector2_group[0],vector3_group[0],line1_group[0],line2_group[0]]
		self.play(GrowFromPoint(vect1[0], point = vect1[0].get_start()), Write(vect1[1]),
				GrowFromPoint(vect2[0], point = vect2[0].get_start()), Write(vect2[1]), 
				GrowFromPoint(vect3[0], point = vect3[0].get_start()), Write(vect3[1]), 
				
				run_time = 1.5)

		self.play(GrowFromPoint(line1,point = line1.get_start()),
				GrowFromPoint(line2,point = line2.get_start()),
				run_time = 2)
		self.wait()

		#3. Transform through the others
		for k in range(1,len(vector1_group)):
			vect1_new,vect2_new,vect3_new,line1_new,line2_new = [vector1_group[k],
															vector2_group[k],
															vector3_group[k],
															line1_group[k],
															line2_group[k]
															]

			self.play(Transform(vect1[0], vect1_new[0]), Transform(vect1[1],vect1_new[1]),
					 Transform(vect2[0], vect2_new[0]), Transform(vect2[1],vect2_new[1]),
					 Transform(vect3[0], vect3_new[0]), Transform(vect3[1],vect3_new[1]),
					 Transform(line1,line1_new),
					 Transform(line2,line2_new),
					run_time = 2)
			self.wait()

			# vect1 = vect1_new
			# vect2 = vect2_new
			# vect3 = vect3_new
			# line1
	
		self.wait()
			