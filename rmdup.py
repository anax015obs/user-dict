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

        if i.endswith('께'): continue; 
        if i.endswith('을'): continue;
        if i.endswith('를'): continue;
        if i.endswith('로서'): continue;   
        if i.endswith('해서'): continue;
        if i.endswith('에서'): continue;
        if i.endswith('에게'): continue;
        if i.endswith('면서'): continue;

        if i.endswith('어요'): continue;
        if i.endswith('이여'): continue;
        if i.endswith('하여'): continue;
        if i.endswith('니까'): continue;
        if i.endswith('다면'): continue;
        

        if i.endswith('라고'): continue;
        if i.endswith('다고'): continue;
        if i.endswith('말고'): continue;
        if i.endswith('하고'): continue;

        if i.endswith('해라'): continue;

        if i.endswith('진다'): continue;
        if i.endswith('이다'): continue;
        if i.endswith('였다'): continue;
        if i.endswith('했다'): continue;
        if i.endswith('한다'): continue;
        if i.endswith('니다'): continue;

        # 기관 제외
        schoolregex = re.compile(r'^[^\*]+(초등학교|중학교|고등학교|연구원|연구소|센터|학회|협회|진흥|재단|법인|지원청)');

        if schoolregex.search(i): continue;
       
        if '・' in i: continue;
        if '하는' in i: continue;
        if '했던' in i: continue;
        if '까지' in i: continue;   
        if '었' in i: continue;
        if '으로' in i: continue;

        # ~라면 -> 라면으로 치환 
        if '라면' in i: i = '라면';

        map[i] = 1;

    # 단어, 단어 + 1단어 or 단어, 단어 + 2단어 케이스 제거
    for i in iarr:
        rootminus1 = i[:-1];
        rootminus2 = i[:-2];
        if len(i) > 2 and (rootminus1 in map or rootminus2 in map): 
            map[i] = 0;
   
    o = '\n'.join([k for k, v in map.items() if v == 1]);
    
    os.remove('korean_noun_result.txt');
    f = open('korean_noun_result.txt', 'w', encoding='utf-8');
    f.write(o);
    print("***run time(sec) :", int(time.time()) - start)