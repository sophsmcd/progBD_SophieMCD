class  Calculator:

    def sum(first, second):
        return map(lambda x, y: x+y, first, second)
    
    def subtract(first,second): 
        return map(lambda x,y: x-y, first,second)
    
    def multiply(first,second):
        return map(lambda x,y: x*y, first, second)
    
    def divide(first,second): 
        return map(lambda x,y: x/y, first,second)
    
    def exponent(first, second):
        return map(lambda x,y: x**y, first,second)

    def square(values):
        return list(map(lambda x: x**2, values))
 
    def sqrt(values):
        return list(map(lambda x: x**(1/2), values))
 
    def cube(values):
        return list(map(lambda x: x**3, values))

    def remainders(values):
        return filter(lambda x: x % 2 == 0, values)

    def min(values):
        return reduce(lambda a,b: a if (a<b) else b, values) 

print sum([13,15,16,17], [15,20,15,30])
print subtract([15,20,15,30], [13,15,16,17])
print multiply([13,15,16,17], [15,20,15,30])
print divide([10,20,30,40,50],[2,4,5,10,25])
print exponent([2,4,5,6],[2,2,2,2])
print square([2,4,5,6])
print sqrt([4,9,16,25])
print cube([3,9,15,25])
print remainders([2,5,4,6,7])
print min([3,6,9,12])

if __name__ == '__main__':
    Calculator()

