import random
"""
#error type,
real_num = 43
guess_num =int( raw_input("Please guess the real num:"))

#print type(guess_num), ord(guess_num)
#error while True
while True:
    if guess_num > real_num :
        print "Wrong ! You need try smaller"
    elif guess_num < real_num :
        print "Wrong ! You need try bigger"
    else:
        print "Congratulations ! You got it"
"""
"""
real_num = 43
retry_count = 0
while retry_count < 3:
    guess_num =int( raw_input("Please guess the real num:"))
    if guess_num > real_num :
        print "Wrong ! You need try smaller"
        retry_count +=1
    elif guess_num < real_num :
        print "Wrong ! You need try bigger"
        retry_count +=1
    else:
        print "Congratulations ! You got it"
        break
"""
"""
real_num = random.randrange(10)
while retry_count <= 3 :
    guess_num = int (raw_input("Please guess the real num:"))
    if guess_num > real_num :
        print("Wrong! Try a num smaller! ")
        retry_count +=1
    elif guess_num < real_num :
        print("Wrong! Try a num bigger! ")
        retry_count +=1
    else:
        print("congratulations! You got it")
        break
    retry_count = 1
else:
    print "The real num is: ",real_num
"""


"""

real_num = random.randrange(10)
retry_count = 0
while retry_count < 3 :
    guess_num = raw_input("Please guess the real num: ").strip()
    if len(guess_num) == 0:
        print len(guess_num)
        continue
    if guess_num.isdigit() :
        guess_num = int(guess_num)
    else:
        print("You need input a integer instead of string")
    if guess_num > real_num:
        print "Wrong! You need try smaller!"
    elif guess_num < real_num:
        print "Wrong! You need try bigger!"
    else:
        print "Congraulations! You got it!"
        break
    retry_count += 1
else:
    print "The real num is: ",real_num

"""



real_num = random.randrange(10)
for i in range(0,3):
    guess_num = raw_input("Please guess a num: ").strip()
    if len(guess_num) == 0:
        continue
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print "You need input a integer instead of string"
        continue
    if guess_num > real_num:
        print "Wrong! You need try smaller!"
    elif guess_num < real_num:
        print "Wrong! You need try bigger!"
    else:
        print "Congratulations! You got it"
        break
else:
    print "The real num is:",real_num







































