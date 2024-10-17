import requests
import time
import os

def isDividable(i: str):
    import json

    host = 'http://10.0.12.93:30200'
    path = '/test2/_analyze'
    body = dict();
    
    body['analyzer'] = "nori_analyzer";
    body['text'] = i;
    body['explain'] = True;

    body = json.dumps(body, ensure_ascii=False).encode('utf-8');
    
    response = requests.request(method='get', url=host+path, data=body, headers={'Content-Type': 'application/json'});

    json = response.json();

    tokens = json.get('detail').get('tokenizer').get('tokens');

    
    print(json);
    if len(tokens) == 1:
        return False;
    else:
        return True;
    
def verify():
    i = open('korean_noun_result.txt', 'r', encoding='utf-8').read();
    iarr = i.split('\n');
    
    if os.path.exists('korean_noun_verified.txt'):
        os.remove('korean_noun_verified.txt');
    
    with open('korean_noun_verified.txt', 'w', encoding='utf-8') as f:
        for istr in iarr:
            # time.sleep(0.1);
            if isDividable(istr):
                f.write(istr + '\n');
    
    