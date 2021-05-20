import jwt

encoded = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0In0.OnuZnYMdetcg7AWGV6WURn8CFSfas6AQej4V9M13nsk"

word_list = open('password_list.txt','r').read().split('\n')

for word in word_list : 
	secret = word
	print(jwt.decode(encoded, secret, algorithms=['HS256']))
