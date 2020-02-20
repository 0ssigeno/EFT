import json
import hashlib
import requests
import zlib

base_launcher="https://launcher.escapefromtarkov.com"

def encode_request(data):
    return zlib.compress(data)

def decode_request(data):
    return zlib.decompress(data)

def login(email: str, pwd: str, hwcode: str):
    md5=hashlib.md5()
    md5.update(pwd.encode("utf-8"))
    pwd_hash=md5.hexdigest()
    content={"email": email, "pass": pwd_hash, "hwcode":hwcode, "captcha": None}
    content_json = json.dumps(content).replace(" ","")
    content_encoded=encode_request(content_json.encode("utf-8"))
    version="0.9.3.1023"
    branch="live"
    params={"launcherVersion":version,"branch":branch}
    cfuid="d6c4e328ce8449b45a669f1ed9c5cb64e1582206944"
    phpsession="554abe009717500647012fe16b7b42fb"
    cookies={"__cfduid":cfuid,"PHPSESSID": phpsession}
    headers={"User-Agent":"BSG Launcher 0.9.3.1023", "Host":"launcher.escapefromtarkov.com","content-type":"application/json"}
    res= requests.post(base_launcher+"/launcher/login", params=params,data=content_encoded,cookies=cookies,headers=headers)
    print(decode_request(res.content))

if __name__ == "__main__":
    hw="#1-dd18247e1c4ebac8d09bc8578e576aa65c01b71a:1c061982a4ff10fdb59781dd3f07759348aed140:2f77d21529f86ea3e5dc4501be1e669bf77e80a7-0f224ce50bb7ccc3e6b64f9b6e76aa78dcf00b38-4715e29742e526cc1020de9c1ffc705c5d6658f1-1355f1ad921b92f74c406f06c910fb29d5a0906f-38a485f1a6f9f028d8bf258c13c0cc4baf5ca58f-7ad9d5a81ba7076ecf145cbbb4800706"
    pwd="Dieci51996"
    email="xbuji6@gmail.com"
    login(email,pwd,hw)