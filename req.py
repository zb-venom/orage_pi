import requests
payload = {'key': 0002, 'auditory': 404, 'user': 4564, 'device': 456}
r = requests.post("http://192.168.43.234/post.php", data=payload)
print(r.text)
