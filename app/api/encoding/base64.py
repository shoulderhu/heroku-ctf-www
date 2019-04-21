from base64 import standard_b64encode


def b64encode(data):
    return standard_b64encode(data.encode()).decode()