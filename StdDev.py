import csv,math
from typing import final

#opening the csv file and converting it into a list.

with open("data.csv") as d:
    data=csv.reader(d)
    fileData=list(data)
    finalData=fileData[0]

#Finding the mean of the given data.
sum=0
for i in finalData:
    sum+=int(i)
mean=sum/len(finalData)

#Subtract the mean from all the values and square them .
squareSum=0
for i in finalData:
    x=int(i)-mean
    x=x**2
    
    #Get the sum of all the elements from the squared list.
    squareSum+=x


#Divide the sum by the number of values in the dataset and getting its square root
standardDeviation=math.sqrt(squareSum/(len(finalData)-1))
print("The Standard Deviation of the data is: ",standardDeviation)