import math

def Spline_evaluation(x_in):
    temp = 0.0
    # coefficients
#    A = -7.6598400373530353E+00
      #   1.0000000000000002
    A = -7.657699326187228E+00
    B = 4.2173990876638285E+00
    C = -5.4348457135862027E-01
    D = 3.3511523878673163E-02

    temp = A + B*math.log(x_in) + C*math.pow(math.log(x_in), 2.0) + D*math.pow(math.log(x_in), 3.0)
    return temp
 
print(Spline_evaluation(20))print(Spline_evaluation(40))
print(Spline_evaluation(80))
print(Spline_evaluation(150))
print(Spline_evaluation(300))
print(Spline_evaluation(600))
print(Spline_evaluation(1200))
print(Spline_evaluation(2400))
print(Spline_evaluation(4000))
print(Spline_evaluation(6000))
print(Spline_evaluation(9000))
print(Spline_evaluation(13000))
print(Spline_evaluation(18000))
print(Spline_evaluation(24000))
print(Spline_evaluation(32000))
print(Spline_evaluation(42000))
print(Spline_evaluation(54000))
print(Spline_evaluation(68000))
print(Spline_evaluation(84000))
print(Spline_evaluation(100000))
