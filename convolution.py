import numpy as np

def Multiply(filter,I,row,col):
    #function for filter and I window multiplication
    result=0
    for i in range(3):
        for c in range(3):
            result=result+filter[i][c]*I[i+row][col+c]

    return result

def Convolution(fitler,I):
    Result = np.random.rand(3,4)
    for i in range(3):
        for c in range(4):
            Result[i][c]=Multiply(filter,I,i,c)
    return Result


if __name__=="__main__":


  filter=np.array([[-2,0,1],
              [-4,0,4],
              [-2,0,2]])
  I=np.array([[8,8,8,10,10,10],[8,8,8,10,10,10],[8,8,8,10,10,10],[9,9,9,9,9,9],[9,9,9,9,9,9]])
  result=Convolution(filter, I)

  print("The result of the convolution is : ")
  print(result)

