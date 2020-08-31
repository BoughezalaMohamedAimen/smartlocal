import sys
import hmac
import hashlib


hash=hmac.new(b"password", b"message").hexdigest()


f = open("finish.txt", "w")
f.write(hash)
f.close()
