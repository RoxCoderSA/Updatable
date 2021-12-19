import os #importing library os 
import colorama # importing library colorama 

print("""                                                               
     #    # #####  #####    ##   #####   ##   #####  #      ###### 
     #    # #    # #    #  #  #    #    #  #  #    # #      #      
     #    # #    # #    # #    #   #   #    # #####  #      #####  
     #    # #####  #    # ######   #   ###### #    # #      #      
     #    # #      #    # #    #   #   #    # #    # #      #      
      ####  #      #####  #    #   #   #    # #####  ###### ######  @Roxcoder \n """)


      
print ("\n") #new line

def main(): #identify function
	
	print("""
	1- Ubuntu / Debian
	2- Fedora / Red Hat
	3- ArchLinux / manjaro
	4- Opensuse / suse
	5- MacOS
	99- Exit""")

	print ("\n") #new line
	
	choose = int(input("Please Choose The Distribution : ")) #printing the massage 

	if choose == 1: # check the value from input user
		Debian() #call the function after check the value that user enterd
		exit(0)  #exit from script
	
	elif choose == 2: # check the value from input user
		Fedora() #call the function after check the value that user enterd
		exit(0)  #exit from script

	
	elif choose == 3: # check the value from input user
		Arch() #call the function after check the value that user enterd
		exit(0) #exit from script

	elif choose == 4: # check the value from input user
		Opensuse() #call the function after check the value that user enterd
		exit(0) #exit from script

	elif choose == 5:
		MacOS() #call the function after check the value that user enterd
		exit(0) #exit from script
	
	elif choose == 99: # check the value from input user
		print("See You Next Time") #printing the massage
		os.system('sleep 5') # stopping system 5 sec
		os.system('clear') # clear the terminal after 5 sec
		exit(0)  #exit from script

	
	else:
		print("The Value Not Found " + str(choose)) # printing the massage
		os.system('sleep 5') # stopping system 5 sec
		os.system('clear') # clear the terminal after 5 sec 
		exit(0)  # exit from script
	
	######### UPDATE DEBIAN OR UBUNTU #########

def Debian():
	os.system('sudo apt update -y')# Check for update of apt 
	os.system('sudo apt upgrade -y')# Upgrade of apt repo 
	os.system('sudo apt dist-upgrade -y')# Upgrade all system and programes 
	os.system('sudo apt autoremove -y')# Remove all package deos not needs 
	print("All update completed\n")# Printing massage after upgrading 
	print (colorama.Fore.GREEN + "Code By:" + colorama.Fore.WHITE + " Roxcoder")# Printing massage with call colors library
	os.system('sleep 15')# Stopping the system 15 sec
	os.system('clear')# Clear the terminal after 15 sec

########## UPDATE FEDORA OR RED HAT ##########

def Fedora(): # identify function 
	os.system('sudo yum -y update') # check for update of yum
	print("All update completed\n") # printing massage 
	print (colorama.Fore.RED + "Code By:" + colorama.Fore.WHITE + " Roxcoder") # printing massage with call colors library
	os.system('sleep 15') # stopping the system 15 sec
	os.system('clear') # clear the terminal after 15 sec

	####### CHECK ON KERNELS ON SYSTEM #######

	check = input('Do Want Check On Kernels (Y/n) : ') # asking the user if want check on kernels
	if check ==  'y' or check == 'Y': # check on the value user entered 
		os.system('yum list installed kernel') # view the all kernels that installed in system
	elif check == 'n' or check == 'N': # check on the value user entered
		exit(0) #exit from script

	######## REMOVE OLD KERNELS ########

	kernelRemove = input('Do You Want Remove old kernels (Y/n) : ') #asking user if want remove old kernel
	if kernelRemove == 'y' or kernelRemove == 'Y': # check the user entered  
		kernel = input('Enter Versoin Kernel : ') # asking the user enter the version of kernel 
		os.system('yum list installed kernel*' + str(kernel)) # show the kernel and addons
		os.system('sudo yum -y remove kernel*' +  str(kernel)) # remove old kernel  from list 
	elif kernelRemove == 'n' or kernelRemove == 'N': # check the user entered 
		exit(0)

def MacOS(): # identify function
	os.system('sudo softwareupdate -l') # Check update for MacOS
	os.system('sudo softwareupdate -i -a') # Install all update 
	print('All update completed\n') # Printing massage
	print(colorama.Fore.YELLOW + "Code By: " + colorama.Fore.WHITE + " Roxcoder") # printing massage with call colors library
	os.system('sleep 15') # stopping the system 15 sec
	os.system('clear') # clear the terminal after 15 sec

def Arch(): # identify function
	os.system("sudo pacman -Syu") # Check update for Arch
	os.system("sudo pacman -Syy") # Upgrade system for Arch
	print('All update completed\n') # Printing massage
	print(colorama.Fore.BLUE + "Code By: " + colorama.Fore.WHITE + " Roxcoder") # printing massage with call colors library
	os.system("sleep 15") # stopping the system 15 sec
	os.system("clear") # clear the terminal after 15 sec

def Opensuse(): # identify function
	os.system("sudo zypper refresh") # Refresh the repo
	os.system("sudo zypper update")  # updating packge after refresh the repo
	print('All update completed\n') # Printing massage
	print(colorama.Fore.CYAN  + "Code By: " + colorama.Fore.WHITE + " Roxcoder") # printing massage with call colors library
	os.system("sleep 15") # stopping the system 15 sec
	os.system("clear") # clear the terminal after 15 sec

if __name__ == '__main__': # check on main function 
	main() # call the main function
