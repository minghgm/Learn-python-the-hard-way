# -*- coding: utf-8 -*-

global i		#define i as global variable
i = 0
numbers = []
vars = int(raw_input("pls input one number: "))
step = int(raw_input("please input step of wloop: "))
print "please select which loop you want to execute: 1.w_loop; 2.f_loop"
sloop = raw_input()

def w_loop(para1, para2):
	global i			#if no this sentence, will have "UnboundLocalError: local variable 'i' referenced before assignment", this tell the function to seek variable i in global, not in local. but I don't know why in f_loop function no need this.
	while i < para1:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += para2
		print "Numbers now: ", numbers
		print "At the bottom i is %d" %i 
		
def f_loop(lmax,lstep):
	print range(lmax)
	for i in range(lmax):
		print "At the top i is %d" %i 
		numbers.append(i)
		
		i += lstep
		print "Numbers now: ", numbers
		print "At the bottom i is %d" %i 

if sloop == "1":
	print "#-------------Now start w_loop -------------"
	w_loop(vars, step)
else:
	print "#-------------Now start f_loop --------------"
	f_loop(vars,step)

	
print "The numbers: "

for num in numbers:
	print num

		
