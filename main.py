import requests

auditory = '404'

user = ''
key = ''
device = ''

while 1:
    print("Insert user code:")
    user = input()
    while 1:
        print("Selecet\n1.Take2.Give3.quit")
        key = input()
        if key == 1 or key == 2:
            	device = input()
            	payload = {'key': key, 'auditory': auditory, 'user': user, 'device': device}
            	r = requests.post("http://esau.tusur.ru:2280/post.php", data=payload)
            	print(r.text)
        elif key == 3:
            break
    if key == 3:
         break

