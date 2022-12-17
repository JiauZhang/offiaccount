import argparse
import requests

parser = argparse.ArgumentParser()

parser.add_argument('--appid', type=str, required=True)
parser.add_argument('--secret', type=str, required=True)

args = parser.parse_args()

ip_url = 'http://httpbin.org/ip'
ip_info = requests.get(url=ip_url).json()
print(ip_info)

token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(
    args.appid, args.secret
)
token_info = requests.get(url=token_url)
print(token_info.json())