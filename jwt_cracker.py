#!/usr/bin/env python
import jwt,sys

def jwt_cracker(token,file):
	file = open(file,'r').read().split('\n')
	
	for candidate in file:
		try:
			jwt.decode(token,candidate,algorithm='HS256')	
			print(candidate)
			return
		except:
			print('failed for '+candidate)
#			raise	

if __name__=='__main__':
	jwt_cracker(sys.argv[1],sys.argv[2])
