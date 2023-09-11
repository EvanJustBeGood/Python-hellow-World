import requests


token = "IGQWRPak93V3J5V3p4V2JHLXJ5bmFyZADN3RmhtSEpvVFhDVWV2bGUtMlFBRnVXMkxoRFBQbUhKTVBRbzlNOXF2em0xVngyUHZAMS1VRdmdLaXJPSFFMUDBtSEJYaW5zX3pCNk9QaGJkZADdhMVU3NERtZAlE4bElfUnMZD"

url = "https://graph.instagram.com/v1/users/ivan_rus8/media?fields=id,caption,media_type,timestamp,likes.count,comments.count&access_token={IGQWRPak93V3J5V3p4V2JHLXJ5bmFyZADN3RmhtSEpvVFhDVWV2bGUtMlFBRnVXMkxoRFBQbUhKTVBRbzlNOXF2em0xVngyUHZAMS1VRdmdLaXJPSFFMUDBtSEJYaW5zX3pCNk9QaGJkZADdhMVU3NERtZAlE4bElfUnMZD}".format(token)
response = requests.get(url)

if response.status_code == 200:
    results = response.json()["data"]
else:
    print("Ошибка: {}".format(response.status_code))

for result in results:
    print("Идентификатор:", result["id"])
    print("Подпись:", result["caption"])
    print("Тип медиа:", result["media_type"])
    print("Дата публикации:", result["timestamp"])
    print("Количество лайков:", result["likes"]["count"])
    print("Количество комментариев:", result["comments"]["count"])