# Version print
print("J.E.R.M Language version = 16.2")

# Complier repeat
while True:
	# Code asker
	user_input = input("RK:/JERM/User/newfile.jerm>>> ")
	
	# File opener and user input saver
	with open("JERMcode.txt", "a") as file:
		file.write(user_input + "\n")

	# Syntax checker
	if "NW" or "W" not in user_input:
		print("Err: No system connecting definer (NW) or (W)")
	
		if "System" not in user_input:
			print("Err: no connector (System)")
