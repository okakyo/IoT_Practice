#�T�[�o�[��micropython�ł̒ʐM��json�`���ōs���Ă���

import ujson,requests,

def send_json(data):

    return ujson.dump(data)

def get_json(url=None):
    if url:
        json=ujson.loads(url)
    else:
        json=ujson.loads(open('config.json','r').read())
    for i in json:
        print(i)


