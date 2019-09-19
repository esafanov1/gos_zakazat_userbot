#  NO CHANGES NEEDED HERE TO CONFIGURE PROXY, ONLY IN CONFIG.PY !!!

from config import host_name, port, proxy_secret, rdns, username, password, proxy_type
import socks

if proxy_type:
    if type(host_name) != str:
        raise TypeError('host_name should be string')
    elif type(port) != int:
        raise TypeError('port should be int')
    proxy = [host_name, port]
    if proxy_type == 'MTProto':
        if type(proxy_secret) != str:
            raise TypeError('proxy_secret should be string')
        else:
            proxy.append(proxy_secret)
    else:
        if proxy_type == 'SOCKS4':
            proxy_type = socks.SOCKS4
        elif proxy_type == 'SOCKS5':
            proxy_type = socks.SOCKS5
        elif proxy_type == 'HTTP':
            proxy_type = socks.HTTP
        else:
            raise Exception('The proxy_type should be MTProto, SOCKS4, SOCKS5 or HTTP and string')
        proxy = [proxy_type] + proxy + [rdns]
        if username:
            proxy.append(password)
            if password:
                proxy.append(password)
    proxy = tuple(proxy)
else:
    proxy = None
