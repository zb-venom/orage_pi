import subprocess

def write(input):
	f = open("input.txt", "w")
	f.write(input)
	f.close

write("Inser_your_code")
subprocess.call("./orange_lcd")
