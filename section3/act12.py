'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
ACTIVITY 12: Find the difference!

Billiam and Bob wrote the following codes. They look similar, but why do they produce different output?
'''


# Billiam's code
count = 0

def addToCount():
	count = count + 1
	print("count is now = " + str(count))

for i in range(5):
	addToCount()


# Bob's code
count = 0

def addToCount():
	global count
	count = count + 1
	print("count is now = " + str(count))

for i in range(5):
	addToCount()
