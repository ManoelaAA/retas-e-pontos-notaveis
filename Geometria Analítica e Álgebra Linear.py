import math
import statistics
import sympy as sy
from sympy import Point, Segment, Line, Triangle
from sympy.geometry import intersection


print("Welcome.")
print("Please enter the coordinates in the X Y model with integers. \n")

# Create a tuple of coordinates from input and transform the type of str to int (string to number)
A = tuple(int(num) for num in input('Enter the coordiantes for A: ').split())
B = tuple(int(num) for num in input('Enter the coordiantes for B: ').split())
C = tuple(int(num) for num in input('Enter the coordiantes for C: ').split())
print("------------------------------------------------------------")


x, y = sy.symbols("x y")

# ------------------------------------------------------------   ------------------------------------------------------------ #

# Checks if the points correspond to a triangle
def valid_triangle(A, B, C):
    d1 = math.dist(A, B)
    d2 = math.dist(B, C)
    d3 = math.dist(C, A)
    return d1 + d2 > d3 and d2 + d3 > d1 and d3 + d1 > d2



if valid_triangle(A, B, C) == True:

    print("Is it a triangle?  " + str(valid_triangle(A, B, C)))
    print("------------------------------------------------------------")

    # ------------------------------------------------------------   ------------------------------------------------------------ #

    # Checks the type of the triangle
    def type_triangle(A, B, C):
        t = Triangle(Point(A), Point(B), Point(C))

        if t.is_equilateral() == True:
            return "equilateral"
        
        elif t.is_isosceles() == True:
            return "isosceles"
        
        elif t.is_scalene() ==True:
            return "scalene"
        
        else:
            "type not found"

    print("Your triangle is:  " + str(type_triangle(A, B, C)))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------   ------------------------------------------------------------ #

    # The length of the line segment
    def length_segment(A, B):
        d1 = math.dist(A, B)
        return (d1)
        
    print("Length of A to B:  " + str(length_segment(A, B)))
    print("Length of B to C:  " + str(length_segment(B, C)))
    print("Length of C to A:  " + str(length_segment(C, A)))
    print("------------------------------------------------------------")


    # ------------------------------------------------------------ 1 ------------------------------------------------------------ #

    # The midpoint of the line segment
    def midpoint(A, B):
        d1 = (math.dist(A, B))/2
        return (d1)

    mAB = midpoint(A, B)
    mBC = midpoint(B, C)
    mCA = midpoint(C, A)


    print("Midpoint distance of A to B:  " + str(mAB))
    print("Midpoint distance of B to C:  " + str(mBC))
    print("Midpoint distance of C to A:  " + str(mCA))
    print("------------------------------------------------------------")



    # The perpendicular bisector of this segment
    def p_bisector(A, B):
        b1 = Point(A)
        b2 = Point(B)

        s1 = Segment(b1, b2)
    
        perpendicularBisector = (s1.perpendicular_bisector().points[0])
        return perpendicularBisector


    pb1 = p_bisector(A, B)
    pb2 = p_bisector(B, C)
    pb3 = p_bisector(C, A)

    print("Perpendicular bisector of line of A to B:  " + str(pb1))
    print("Perpendicular bisector of line of B to C:  " + str(pb2))
    print("Perpendicular bisector of line of C to A:  " + str(pb3))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 2 ------------------------------------------------------------ #

    # Takes two points p and q and returns the equation of line that passes through those points
    def equation_line(A, B):
        s1 = Segment(A, B)

        l1 = Line(s1).equation()
        return l1
        
        
    print("Equation of line of A to B:  " + str(equation_line(A, B)))
    print("Equation of line of B to C:  " + str(equation_line(B, C)))
    print("Equation of line of C to A:  " + str(equation_line(C, A)))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 3 ------------------------------------------------------------ #

    # The perpendicular bisector of this segment
    def line_perpendicular_bisector(A, B):
        b1 = Point(A)
        b2 = Point(B)

        s1 = Segment(b1, b2)
    
        perpendicularBisector = (s1.perpendicular_bisector())
        return perpendicularBisector


    lb1 = line_perpendicular_bisector(A, B)
    lb2 = line_perpendicular_bisector(B, C)
    lb3 = line_perpendicular_bisector(C, A)

    eb1 = lb1.equation()
    eb2 = lb2.equation()
    eb3 = lb3.equation()

    print("Equation of perpendicular bisector of line of A to B:  " + str(eb1))
    print("Equation of perpendicular bisector of line of B to C:  " + str(eb2))
    print("Equation of perpendicular bisector of line of C to A:  " + str(eb3))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 4 ------------------------------------------------------------ #

    # The perpendicular bisector of this segment (line)
    def circumcenter(A, B, C):
        ax = A[0]
        ay = A[1]
        bx = B[0]
        by = B[1]
        cx = C[0]
        cy = C[1]
        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
        uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
        return (ux, uy)

    D = circumcenter(A, B, C)

    print("Circumcenter:  " + str(D))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 5 ------------------------------------------------------------ #

    # The length of the line segment
    print("Length of D to A:  " + str(length_segment(D, A)))
    print("Length of D to B:  " + str(length_segment(D, B)))
    print("Length of D to C:  " + str(length_segment(D, C)))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 6 ------------------------------------------------------------ #

    # The medians of the triangle
    A = Point(A)
    B = Point(B)
    C = Point(C)

    t = Triangle(A, B, C)

    m1 = t.medians[A]
    m2 = t.medians[B]
    m3 = t.medians[C]

    print("Coordenates of the median of A:  " + str(m1.points))
    print("Coordenates of the median of B:  " + str(m2.points))
    print("Coordenates of the median of C:  " + str(m3.points))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 7 ------------------------------------------------------------ #

    # Intersection of medians
    E = intersection(m1, m2, m3)[0]

    print("Intersection of medians:  " + str(E))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 8 ------------------------------------------------------------ #

    # The distance from E to the midpoint of each side of the triangle
    print("Length of E to pb1:  " + str(length_segment(E, pb1)))
    print("Length of E to pb2:  " + str(length_segment(E, pb2)))
    print("Length of E to pb3:  " + str(length_segment(E, pb3)))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 9 ------------------------------------------------------------ #

    # The distance from E to each vertex of the triangle
    print("Length of E to A:  " + str(length_segment(E, A)))
    print("Length of E to B:  " + str(length_segment(E, B)))
    print("Length of E to C:  " + str(length_segment(E, C)))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 10 ------------------------------------------------------------ #

    AB = Segment(A, B)
    AC = Segment(A, C)

    dp = 10
    dq = 0

    P = (0, 0)
    Q = (0, 0)

    print("Generating point on line... \n")

    # Checks if the points created are equidistant from point A
    while math.isclose(dp, dq, abs_tol = 0.02) == False:
        P = AB.random_point().n(4)
        Q = AC.random_point().n(4)

        dp = math.dist(P, A)
        dq = math.dist(Q, A)

    dpdq = round(statistics.median([dp, dq]), 7)

    print("Coordinates P:  " + str(P))
    print("Coordinates Q:  " + str(Q))
    print("Length of P to A and Q to A:  " + str(dpdq))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 11 ------------------------------------------------------------ #


    BA = Segment(B, A)
    BC = Segment(B, C)

    dr = 10
    ds = 0

    R = (0, 0)
    S = (0, 0)

    print("Generating point on line... \n")

    # Checks if the points created are equidistant from point B
    while math.isclose(dr, ds, abs_tol = 0.02) == False:
        R = BA.random_point().n(4)
        S = BC.random_point().n(4)

        dr = math.dist(R, B)
        ds = math.dist(S, B)

    drds = round(statistics.median([dr, ds]), 7)

    print("Coordinates R:  " + str(R))
    print("Coordinates S:  " + str(S))
    print("Length of R to B and S to B:  " + str(drds))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 12 ------------------------------------------------------------ #

    # The midpoint M of the segment P Q
    M = p_bisector(P, Q)

    print("Midpoint of P to Q:  " + str(M))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 13 ------------------------------------------------------------ #

    # The midpoint N of the segment R S
    N = p_bisector(R, S)

    print("Midpoint of R to S:  " + str(N))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 14 ------------------------------------------------------------ #

    # Returns the equation of line that passes through those points
    A = Point(A)
    M = Point(M)

    α = equation_line(A, M)

    print("Equation of line of A to M:  " + str(α))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 15 ------------------------------------------------------------ #

    # Returns the equation of line that passes through those points
    B = Point(B)
    N = Point(N)

    β = equation_line(B, N)

    print("Equation of line of B to N:  " + str(β))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 16 ------------------------------------------------------------ #

    # Intersection of α and β
    sα = Line(A, M)
    sβ = Line(B, N)


    I = intersection(sα, sβ)[0]

    print("Intersection of α and β:  " + str(I))
    print("------------------------------------------------------------")



    # ------------------------------------------------------------ 17 ------------------------------------------------------------ #




    # The distance from I to the three sides of the triangle
    print("Length of I to mAB:  " + str(length_segment(I, pb1)))
    print("Length of I to mBC:  " + str(length_segment(I, pb2)))
    print("Length of I to mCA:  " + str(length_segment(I, pb3)))
    print("------------------------------------------------------------")



# ------------------------------------------------------------  ------------------------------------------------------------ #

else: 
    print("Please enter valid coordinates.")