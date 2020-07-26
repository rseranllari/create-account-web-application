from flask import *

app = Flask(__name__)

app.secret_key = b'6\xe5\x15\xae|3N\xc0\xb6\xb5\xbdU{}8V'

@app.route('/assignment11.html')
def webpage():
	
	username = "none"
	password = "none"

	newuser = "none"
	newpass = "none"
	fname = "none" 
	lname = "none" 

	color = "none"
	title = "none"
	image = "none"

	titletag = "off"
	successful = "off"
	
	edituser = "none"
	editfname = "none"
	editlname = "none"
	editcolor = "none"
	edittitle = "none"
	editimage = "none"
	

	if "editfname" in request.args:
		editfname = request.args.get("editfname")
		editlname = request.args.get("editlname")
		editcolor = request.args.get("color")
		edittitle = request.args.get("title")
		editimage = request.args.get("image")
		edituser = request.args.get("hidden")


	if editfname == "none":
		
		if "username" in request.args:
			username = request.args.get("username")
			password = request.args.get("password")
			newuser = "none"
			newpass = "none"
			fname = "none"
			lname = "none"

		if "newuser" in request.args:
			newuser = request.args.get("newuser")
			newpass = request.args.get("newpass")
			fname = request.args.get("fname")
			lname = request.args.get("lname")
		
			username = "none"
			password = "none"
	
	
		if newuser == "none":
			f = open("assignment11-account-info.txt", "r+")
			infos = f.readlines()
			f.close()
			i = 0
			for info in infos:
				credent = info.split(";")
				if username == credent[0]:
					i += 1
			
			if i == 0 and username != "none":
				successful = "noaccount"
			else:
				for info in infos:
					credent = info.split(";")
					if username == credent[0]:
						if password == credent[1]:
					
							newuser = credent[0]
							newpass = credent[1]
							fname = credent[2]
							lname = credent[3]
							color = credent[4]
							title = credent[5]
							image = credent[6]
							titletag = "on"
							successful = "on"
		
						else: 
							if password == "":
								successful = "nopass"
							else:
								successful = "wrong"
		
		else:
			if newuser == "":
				successful = "nouser"
			elif newpass == "":
				successful = "nopass"
			elif fname == "":
				successful = "nofname"
			elif lname == "":
				successful = "nolname"
			else:
				i = 0
				f = open("assignment11-account-info.txt", "r+")
				infos = f.readlines()
				f.close()
				for info in infos: 
					credent = info.split(";")
					if newuser == credent[0]:
						i += 1
				if i >= 1:
					successful = "usertaken"
				else:
					f = open("assignment11-account-info.txt", "a+")
					color = "white"
					title = "Welcome to Ronaldo Seranllari's assignment11 web site"
					image = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Stick_Figure.svg/1200px-Stick_Figure.svg.png"
					f.write(newuser + ";" + newpass + ";" + fname + ";" + lname + ";" + color + ";" + title + ";" + image + "\n")
					f.close()
					successful = "on"
	else:
		f = open("assignment11-account-info.txt", "r+")
		infos = f.readlines()
		f.close()
		
		f = open("assignment11-account-info.txt", "w+")
		for info in infos:
			credent = info.split(";")
			if edituser == credent[0]:
				credent[2] = editfname
				credent[3] = editlname
				credent[4] = editcolor
				credent[5] = edittitle
				credent[6] = editimage
				
				newuser = credent[0]
				newpass = credent[1]
				fname = credent[2]
				lname = credent[3]
				color = credent[4]
				title = credent[5]
				image = credent[6]
				titletag = "on"
				successful = "on"
			f.write(credent[0] + ";" + credent[1] + ";" + credent[2] + ";" + credent[3] + ";" + credent[4] + ";" + credent[5] + ";" + credent[6] + "\n")
		f.close()
	return render_template("assignment11.html", newuser = newuser, newpass = newpass, fname = fname, lname = lname, color = color, title = title, image = image, successful = successful, titletag = titletag)