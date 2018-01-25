#import the needed operations
import numpy as numpi

#create array and fill with numbers
m = numpi.array([[3,1,4],[6,3,9],[3,3,3],[6,7,9],[7,5,2]])

#print out the array
print (m)
#or using your hint

for column in m:
    print(column)

#print out subsequent columns
print (m[:,0])

print (m[:,1])

print (m[:,2])


