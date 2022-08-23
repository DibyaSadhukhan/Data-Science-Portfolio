import  math
import numpy as np

class Exponential:
  #takes the Xtrain and Ytrain as parameter
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def mul(self,A,B):
        #function takes two arguments the series X and series Y and returns 1 series mul
        #(the multipication of the individual elements of the two provided series)
        #function to multiple individual elements of two series
        Mul=[]
        if len(A)!=len(B):
        #if the lens dont match it gives an error
            return -1
        else:
            for i in range(0,len(A)):
                Mul.append(A[i]*B[i])
            return Mul
  
    def fit_value_Exp(self):
        """
        function takes two arguments the series X and series Y and returns the unknown variables 
        a and b of the curve y=ab^x
        function to fit the curve y=ab^x
        """
        if (len(self.X)==len(self.Y)):
            #finding the value of n,ΣX,ΣY,ΣXY and Σ(X^2)
            n=len(self.X)
            sum_X=sum(self.X)
            sum_Y= sum(np.log(self.Y))
            #print(np.log(Y))
            sum_XY = sum(self.mul(self.X,np.log(self.Y)))
            sum_Xsqr=sum(self.mul(self.X,self.X))
            #from the equation ΣY=nA+BΣX 
            #and ΣXY=AΣX+BΣ(X^2) we solve for B by substitution
            B= (n*sum_XY - sum_X*sum_Y)/(n*sum_Xsqr- sum_X*sum_X)
            A= (sum_Y-(B*sum_X))/n
            #since Y,A and B are just the natural log of the unknoen variables a and b we have to return the antilog 
            return math.exp(A),math.exp(B)
        else:
            return -1
    def predict(self,Xtest):
        """
        function takes three argument the unknown variables a and b from the eqn y=ab^x 
        and the series of independent variable x  
        and returns the series y which is the dependent variable from the curve y=ab^x
        funtion to predict the data from the graph
        """
        a,b=self.fit_value_Exp()
        y=[]
        for i in range(0,len(Xtest)):
            #finding the value of y from the equation y=a(b^x)
            y.append(a*(b**(Xtest[i])))
        return y
    
