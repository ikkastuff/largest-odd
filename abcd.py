print("enter three numbers")
x=int(input())
y=int(input())
z=int(input())
if(x%2==1):
	if(y%2==1):
   		if(z%2==1):
   			if(x>y):
   				if(x>z):
   					print("largest odd number is ",x)
   				else:
   					print("largest odd number is ",z)
   			elif(y>z):
   				print("largest odd number is ",y)   			
   			else:
   				print("largest odd number is ",z)   			
   		elif(x>y):
   			print("largest odd nunmber is ",x)
   		else:
   			print("largest odd number is ",y)	
	elif(z%2==1):
		if(x>z):
   			print("largest odd number is ",x)  				     
          else:
    			print("largest odd number is ",z)
   	else:
   		print("largest odd number is ",x)
elif(y%2==1):
	if(z%2==1):
		if(y>z):
   			print("largest odd number is ",y)
   		else:
   			print("largest odd number is ",z)   
   	else:
   		print("largest odd number is ",y)
elif(z%2==1):
	print("largest odd number is ",z)
else:
	print("no number is odd")	
