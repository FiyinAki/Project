number = input (n)
num = int (number)
n = 0
Sum = 0
minimum = number
while (number != -1)
      n = n + 1
     if (minimum >= number)
     minimum = number
    Sum += n
    num = input (num)
if ( num == 0):
    print("Minimum = -1 \ nAverage = -1")
    else:
        print ("The number of inputs are " + str(n) + ".")
        print ("The minimum number is " + str(minimum)+ ".")
        print ("The summation of all numbers is " + str(Sum) + ".")
        print ("Average is " + str(Sum / n))
