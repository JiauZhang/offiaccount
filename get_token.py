from base.tokenizer import Tokenizer
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--appid', type=str, required=True)
parser.add_argument('--secret', type=str, required=True)

args = parser.parse_args()

tokenizer = Tokenizer(appid=args.appid, secret=args.secret)
print(tokenizer.ip, tokenizer.access_token)
