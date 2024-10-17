import requests
import time
import os

def mergable(i: str):
    import json

    host = 'http://10.0.12.93:30200'
    path = '/test1/_analyze'
    body = dict();
    
    body['analyzer'] = "nori_analyzer";
    body['text'] = i;
    body['explain'] = True;

    body = json.dumps(body, ensure_ascii=False).encode('utf-8');
    
    response = requests.request(method='get', url=host+path, data=body, headers={'Content-Type': 'application/json'});

    json = response.json();

    tokens: list = json.get('detail').get('tokenizer').get('tokens');

    _mergable = False;

    for token in tokens:
        if token.get('token') == i:
            _mergable = True;
            break;
    
    if not _mergable:
        print('Found unmergable ', i);
    
    return _mergable;
    
def verify():
    i = open('korean_noun_result.txt', 'r', encoding='utf-8').read();
    iarr = i.split('\n');
    
    if os.path.exists('korean_noun_verified.txt'):
        os.remove('korean_noun_verified.txt');
    
    with open('korean_noun_verified.txt', 'w', encoding='utf-8') as f:
        for istr in iarr:
            # time.sleep(0.1);
            if not mergable(istr):
                f.write(istr + '\n');
    
    