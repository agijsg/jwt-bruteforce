import jwt
import re
import time
target_token_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" # {"alg":"HS256","typ":"JWT"}
target_token_2 = "eyJldHVpZCI6MzAxLCJpYXQiOjE2MTkyOTMxMDd9" # {"etuid":301,"iat":1619293107}
target_token_3 = "zCogDBSF52IjjRRl3fdGOluLh4_X-oqgA4xCVhFCbXA" # key and verification

data = {"etuid":301,"iat":1619293107}
algorithm = "HS256"

keys = re.findall("\w+", open('rockyou.txt','r').read())

for secret_key in keys :
	print(secret_key)
	encoded_payload = jwt.encode(data,secret_key, algorithm="HS256")

	if encoded_payload==target_token_1+target_token_2+target_token_3:
		print("Key Found : "+secret_key)
		exit(1)

print("Key not found ...")
exit(0)