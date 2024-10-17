import re;
import time, os
import copy

def preprocess(i: str):
    iarr = i.split('\n')
    resultmap = dict();  
    leastmap3 = dict();  
    leastmap4 = dict();
    leastmap5 = dict();
    leastmap6 = dict();

    for i in iarr:
        if len(i) < 3: continue;   
        elif len(i) == 6: 
            resultmap[i] = 1;
            leastmap6[i] = 1;
        elif len(i) == 5:
            resultmap[i] = 1;
            leastmap5[i] = 1;
        elif len(i) == 4:
            resultmap[i] = 1;
            leastmap4[i] = 1;
        elif len(i) == 3:
            resultmap[i] = 1;
            leastmap3[i] = 1;
    return resultmap, leastmap3, leastmap4, leastmap5, leastmap6;



def process(resultmap: dict, leastmap3: dict, leastmap4: dict, leastmap5: dict, leastmap6: dict):
    # 단어의 부분집합을 제거 ex. 체르노빌 체르노 두 개가 공존하면 체르노빌이 파괴되므로 체르노를 제거
    
    for i in resultmap.keys():
        if len(i) > 6:
            for jdx, j in enumerate(i):
                if jdx + 6 <= len(i):
                    subset = i[jdx:jdx+6];
                    try:
                        if leastmap6[subset]:
                            resultmap[subset] = 0;
                            break;
                    except: continue;
    
    for i in resultmap.keys():
        if len(i) > 5:
            for jdx, j in enumerate(i):
                if jdx + 5 <= len(i):
                    subset = i[jdx:jdx+5];
                    try:
                        if leastmap5[subset]:
                            resultmap[subset] = 0;
                            break;
                    except: continue;
    
    for i in resultmap.keys():
        if len(i) > 4:
            for jdx, j in enumerate(i):
                if jdx + 4 <= len(i):
                    subset = i[jdx:jdx+4];
                    try:
                        if leastmap4[subset]:
                            resultmap[subset] = 0;
                            break;
                    except: continue;
    
    for i in resultmap.keys():
        if len(i) > 3:
            for jdx, j in enumerate(i):
                if jdx + 3 <= len(i):
                    subset = i[jdx:jdx+3];
                    try:
                        if leastmap3[subset]:
                            resultmap[subset] = 0;
                            break;
                    except: continue;

    o = '\n'.join([k for k, v in resultmap.items() if v == 1]);
    return o;


def rmdup():
    start = int(time.time())

    i = open('korean_noun_result.txt', 'r', encoding='utf-8').read();
    
    resultmap, leastmap3, leastmap4, leastmap5, leastmap6 = preprocess(i);
    o = process(resultmap, leastmap3, leastmap4, leastmap5, leastmap6);

    os.remove('korean_noun_result.txt');
    f = open('korean_noun_result.txt', 'w', encoding='utf-8');
    f.write(o);
    
    print("***run time(sec) :", int(time.time()) - start)