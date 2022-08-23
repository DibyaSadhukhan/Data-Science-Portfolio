from numpy import linalg
class Parabolic:
  #takes the Xtrain and Ytrain as parameter
  def __init__(self, X,Y):
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
  def Parabola_Curve_fit(self):
    #this function takes in two series the indepent variable and the dependent variable as np arrays 
    #and returns (a,b,c) the three unkown variables in the equation y=ax^2+bx+c
    #finding the value of n,ΣX,ΣY,ΣXY,Σ(X^2),Σ(X^3),Σ(X^4),Σ(X^2*Y)
    sol=[] # list to store the value of a,b,c
    n=len(self.X)
    sum_X=sum(self.X)
    sum_Y= sum(self.Y)
    sum_XY = sum(self.mul(self.X,self.Y))
    sum_Xsqr=sum(self.mul(self.X,self.X))
    sum_XsqrY=sum(self.mul(self.mul(self.X,self.X),self.Y))             
    sum_Xcub=sum(self.mul(self.mul(self.X,self.X),self.X))
    sum_Xtet=sum(self.mul(self.mul(self.mul(self.X,self.X),self.X),self.X))
    #determinant A stores the value of the coefficients of the formed equations
    #b stores the solution of the formed equations and c is a copy of matrix a used in calculation
    A=[[sum_Xsqr,sum_X,n],[sum_Xcub,sum_Xsqr,sum_X],[sum_Xtet,sum_Xcub,sum_Xsqr]]
    B=[sum_Y,sum_XY,sum_XsqrY]
    C=[[sum_Xsqr,sum_X,n],[sum_Xcub,sum_Xsqr,sum_X],[sum_Xtet,sum_Xcub,sum_Xsqr]]
    #cramers rule.
    for i in range(0,len(B)):
      for j in range(0,len(B)):
        C[j][i]=B[j]
        if i>0:
          #switing the colums with the B for individual variables 
          C[j][i-1]=A[j][i-1]
        # A=det(Delta_1)/det(Delta)
      sol.append(linalg.det(C)/linalg.det(A))
    (a,b,c)=(sol[0],sol[1],sol[2])
    return (a,b,c)
  def predict(self,xtest):
    #takes the testing values as prameters and predicts the y using the already tained model.
    #and returns the predicted value.
    (a,b,c)=self.Parabola_Curve_fit()
    #funtion to predict the data from the graph
    y=[]
    for i in range(0,len(xtest)):
        #finding the value of y from the equation y=ax^2+bx+c
        y.append((a*xtest[i]**2)+b*xtest[i]+c)
    return y
