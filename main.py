#WRITE YOUR CODE IN THIS FILE
def countA (x):
    numA = 0
    for i in range(0, len (x)):
        if x[i] == "a":
            numA = numA + 1
    return numA


countA ("cat")
countA ("dog")
countA ("armadillo")
countA ("astronaut")
