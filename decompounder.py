import re;
import time, os
import copy


class StoppedException(Exception): pass;

def preprocess(i: str):
    iarr = i.split('\n')
    resultmap = dict();  
    leastmap2 = dict(); 
    leastmap3 = dict();
    leastmap4 = dict();

    for i in iarr:
        if len(i) == 1: continue;   
        elif len(i) == 4: 
            try:
                resultmap[i] = 1;
                leastmap4[i] = leastmap4[i] + leastmap4[i] / 2;
            except:
                leastmap4[i] = 1;
        elif len(i) == 3: 
            try:
                resultmap[i] = 1;
                leastmap3[i] = leastmap3[i] + leastmap3[i] / 3;
            except:
                leastmap3[i] = 1;
        elif len(i) == 2: 
            try:
                leastmap2[i] = leastmap2[i] + leastmap2[i] / 5;
            except:
                leastmap2[i] = 1;
        else:
            resultmap[i] = 1;
    return resultmap, leastmap2, leastmap3, leastmap4;

def subprocess(i: str, leastmap2: dict, leastmap3: dict, leastmap4: dict, stopmap: dict):
    o = i;
    if len(i) == 2: return o;

    word_list = [];
    if len(i) > 4:
        lp = 0;
        for idx, j in enumerate(i):
            if idx < lp: continue;
            try:
                if leastmap4[i[idx:idx+4]] and leastmap4[i[idx:idx+4]]:
                    try:
                        if stopmap[i[idx:idx+4]]: raise StoppedException();
                    except KeyError: pass;
                    lp = idx + 4;
                    word_list.append({ 'word': i[idx:idx+4], 'idx': idx });
                    continue;
                else: raise Exception();
            except:
                try:
                    if leastmap3[i[idx:idx+3]] and leastmap3[i[idx:idx+3]] > 1.3:
                        try:
                            if stopmap[i[idx:idx+3]]: raise StoppedException();
                        except KeyError: pass;
                        lp = idx + 3;
                        word_list.append({ 'word': i[idx:idx+3], 'idx': idx });
                        continue;
                    else: raise Exception();
                except: 
                    try:
                        if leastmap2[i[idx:idx+2]] and leastmap2[i[idx:idx+2]] > 1.1:
                            try:
                                if stopmap[i[idx:idx+2]]: raise StoppedException();
                            except KeyError: pass;
                            lp = idx + 2;
                            word_list.append({ 'word': i[idx:idx+2], 'idx': idx });
                            continue;
                        else: raise Exception();
                    except: continue; 
    elif len(i) > 3:
        lp = 0;
        for idx, j in enumerate(i):
            if idx < lp: continue
            try:
                if leastmap3[i[idx:idx+3]] and leastmap3[i[idx:idx+3]]:
                    try:
                        if stopmap[i[idx:idx+3]]: raise StoppedException();
                    except KeyError: pass;
                    lp = idx + 3;
                    word_list.append({ 'word': i[idx:idx+3], 'idx': idx }); 
                    continue;
                else: raise Exception();
            except: 
                try:
                    if leastmap2[i[idx:idx+2]] and leastmap2[i[idx:idx+2]]:
                        try:
                            if stopmap[i[idx:idx+2]]: raise StoppedException();
                        except KeyError: pass;
                        lp = idx + 2;
                        word_list.append({ 'word': i[idx:idx+2], 'idx': idx });
                        continue;
                    else: raise Exception();
                except: continue;
    elif len(i) > 2:
        lp = 0;
        for idx, j in enumerate(i):
            if idx < lp: continue;
            try:
                if leastmap2[i[idx:idx+2]] and leastmap2[i[idx:idx+2]]:
                    try:
                        if stopmap[i[idx:idx+2]]: raise StoppedException();
                    except KeyError: pass;
                    lp = idx + 2;
                    word_list.append({ 'word': i[idx:idx+2], 'idx': idx });
                    continue;
                else: raise Exception();
            except: continue;
            
    word_list = sorted(word_list, key=lambda x: x['idx']);
    word_join = ' '.join([i['word'] for i in word_list]);
    return o + ' ' + word_join;    


def process(resultmap: dict, leastmap2: dict, leastmap3: dict, leastmap4: dict, stopmap: dict):
    oarr = [];
    for i in resultmap.keys():
        decompound = subprocess(i, leastmap2, leastmap3, leastmap4, stopmap);
        oarr.append(decompound);
        
    o = '\n'.join(oarr);
    return o;


def decompound():
    start = int(time.time())

    i = open('korean_noun_result.txt', 'r', encoding='utf-8').read();
    
    resultmap, leastmap2, leastmap3, leastmap4 = preprocess(i);
    
    if os.path.exists('weight_3.txt'):
        os.remove('weight_3.txt');
    
    f = open('weight_3.txt', 'w', encoding='utf-8');

    sortedleastmap3 = sorted(leastmap3.items(), key=lambda x: x[1], reverse=True);

    o = ''
    for i in sortedleastmap3:
        o += i[0] + ' ' + str(i[1]) + '\n';
    
    f.write(o);
    
    if os.path.exists('weight_2.txt'):
        os.remove('weight_2.txt');

    f = open('weight_2.txt', 'w', encoding='utf-8');

    sortedleastmap2 = sorted(leastmap2.items(), key=lambda x: x[1], reverse=True);

    o = ''
    for i in sortedleastmap2:
        o += i[0] + ' ' + str(i[1]) + '\n';
    
    f.write(o);

    stopword = open('archive/stopword.txt', 'r', encoding='utf-8').read();
    stopmap = dict();
    for i in stopword.split('\n'):
        stopmap[i] = 1;

    o = process(resultmap, leastmap2, leastmap3, leastmap4, stopmap);
    os.remove('korean_noun_result.txt');
    f = open('korean_noun_result.txt', 'w', encoding='utf-8');
    f.write(o);
    
    print("***run time(sec) :", int(time.time()) - start)