import subprocess
import sys
import requests
import time

def lcd_write(input1, input2):
	f1 = open("input.txt", "w")
	f2 = open("input2.txt", "w")
	f1.write(input1)
	f2.write(input2)
	f1.close
	f2.close

def barcode_read():
	hid = {4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm',
           17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y',
           29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ',
           45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';', 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'}

    	hid2 = {4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M',
            17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y',
            29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ',
            45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':', 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'}

	fp = open('/dev/hidraw0', 'rb')
	code = ''
	shift = False
	done = False
	while not done:
		buffer = fp.read(8)
		for c in buffer:
			if ord(c) > 0:
				if int(ord(c)) == 40:
					done = True
					break
				if shift:
					if int(ord(c)) == 2:
						shift = True
					else:
						code += hid2[int(ord(c))]
						shift = False
				else:
					if int(ord(c)) == 2:
						shift = True
					else:
						code += hid[int(ord(c))]
	return code

auditory = '404'
user =''
key = ''
device = ''

while 1:
	lcd_write("Scan_your_code..", "................")
	subprocess.call('./orange_lcd')
	user = barcode_read()
	lcd_write("Your_id_code_is:", user)
	subprocess.call('./orange_lcd')
	time.sleep(2)
	while 1:
		lcd_write("Select_next_step", "Give_Take_Exit.")
		subprocess.call('./orange_lcd')
		key = barcode_read()
		while 1:
			if key != '1' and key != '2':
				break
			lcd_write("Scan_device_code", "................")
			subprocess.call('./orange_lcd')
			device = barcode_read()
			lcd_write("Device_id_code_:", device)
			time.sleep(5)
			payload = {'key': key, 'auditory': auditory, 'user': user, 'device': device}
            		r = requests.post("http://esau.tusur.ru/post.php", data=payload)
			print(r.text())
			break
