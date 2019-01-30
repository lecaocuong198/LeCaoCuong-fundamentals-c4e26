import random
n = random.randint(1,100)
cloud = '''          .-~~~-.
  .- ~ ~-(       )_ _
 /                    ~ -.
|                          ',
 \                         .'
   ~- ._ ,. ,.,.,., ,.. -~
                  '''
rain = '''  _(  )_( )_
   (_   _    _)
  / /(_) (__)
 / / / / / /
/ / / / / /'''
if(n<30):
    print(rain)
elif(n<60):
    print(cloud)
else:
    print("Sunny")