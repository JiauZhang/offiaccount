from base.tokenizer import Tokenizer
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--appid', type=str, required=True)
parser.add_argument('--secret', type=str, required=True)

args = parser.parse_args()

tokenizer = Tokenizer(appid=args.appid, secret=args.secret, token_required=False)
print('ip:', tokenizer.ip)
print('token:', tokenizer.access_token)
