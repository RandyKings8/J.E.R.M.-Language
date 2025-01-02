# Version print
print("J.E.R.M Language version = 16.2")

def sleep_approx(seconds):
    iterations = seconds * 10**7  # Adjust multiplier for precision
    for _ in range(int(iterations)):
        pass  # Do nothing, just loop

# Complier repeat
while True:
	# Code asker
	user_input = input("RK:/JERM/User/newfile.jerm>>> ")
	
	# File opener and user input saver
	with open("JERMcode.txt", "a") as file:
		file.write(user_input + "\n")
	
	# Exiter
	if "exit" in user_input:
		print("RK:newfile.jerm...")
		sleep_approx(3)
		print("RK:newfile.jermsaved")
		break
	
	# Syntax checker
	if "W" not in user_input:
		print("Err: No System Connecting Definer (W) or Cap Err")
		
	elif "System" not in user_input:
		print("Err: No Connector (System) or Cap Err")
		
	elif "end" not in user_input:
		print("Err: No Code Statement Finalizer (end)")
	
	elif ":" not in user_input:
		print("Err: No Directive Selector (:)")
	
	elif "W" and "System" and "end" and ":" in user_input:
		if ":Code" or ":Body" or ":Car" or ":Plant" in user_input: 
			if 'puts "' in user_input and '"' in user_input.split('puts "')[1]:
				message = user_input.split('puts "')[1].split('"')[0]
				print(message)
