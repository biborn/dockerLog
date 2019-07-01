import base64
def ENCODE(string_):
    return str(base64.b64encode(b''+str.encode(string_))).replace("b'", "").replace("'", "").replace('b"', '').replace('"', '')
def DECODE(string_):
    return str(base64.b64decode(b''+str.encode(string_))).replace("b'", "").replace("'", "").replace('b"', '').replace('"', '')