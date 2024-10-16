import re;
import time, os

def rmdup():
    start = int(time.time())
    # read file 
    f = open('korean_noun_result.txt', 'r', encoding='utf-8');

    # toString
    i = f.read();

    iarr = i.split('\n');
    
    map = dict();
    
    for i in iarr: 
        # 한글자 제외 
        if len(i) == 1: continue;    

        if '에게로' in i: continue;
        
        if i.endswith('에게'): continue;
        if i.endswith('어요'): continue;
        if i.endswith('이여'): continue;
        if i.endswith('니까'): continue;
        if i.endswith('로의'): continue;

        schoolregex = re.compile(r'[가-힣]+학교$');

        map[i] = 1;
   
    o = '\n'.join([k for k, v in map.items() if v == 1]);
    
    os.remove('korean_noun_result.txt');
    f = open('korean_noun_result.txt', 'w', encoding='utf-8');
    f.write(o);
    print("***run time(sec) :", int(time.time()) - start)