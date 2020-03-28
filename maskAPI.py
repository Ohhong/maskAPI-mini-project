import requests
import json

url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page="

print("약국 이름을 입력해주세요.")
pharm_name = input("입력 : ")
print()
print("< " + pharm_name + " > 이 포함된 약국 이름을 가진 약국의 주소 및 목록입니다.")
print()
for i in range(1, 55):
    req = requests.get(url+str(i))
    stores = json.loads(req.text)['storeInfos']
    for s in stores:
        if pharm_name in s["name"] : print(s["name"] + " : " + s["addr"])


