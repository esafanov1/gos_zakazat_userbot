import os

api_id = 1039582  # should be int
api_hash = os.environ['api_hash']  # should be string

# proxy, if don't need proxy, leave proxy_type(!) and others as None
proxy_type = None  # MTProto, SOCKS4, SOCKS5 and HTTP are supported, should be string
#  fill the required parameters, other leave as None
host_name = None  # should be string
port = None  # should be int
proxy_secret = None  # should be string
rdns = True  # should be True or False (Boolean)
username = None  # should be string
password = None  # should be string

# admins
admins = [431164113, 500238135]  # should be int in form [id, id, id, id]
