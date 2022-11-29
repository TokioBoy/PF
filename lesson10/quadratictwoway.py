import math 
def main(): 
    print("This program finds the real solutions to a quadratic\n") 
    a = float(input("Enter coefficient a: ")) 
    b = float(input("Enter coefficient b: ")) 
    c = float(input("Enter coefficient c: ")) 
    discrim = b * b - 4 * a * c
    if discrim > 0:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a) 
        root2 = (-b - discRoot) / (2 * a) 
        print("\nThe solutions are:", root1, root2)
    else:
        if discrim < 0:
            print("Equation has no real roots")
        else:
            if discrim == 0:
                root = -b / (2 * a)
                print("There is a double root", root)
main() 
input()
