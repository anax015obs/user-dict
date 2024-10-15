import convert
import rmdup
from konlpy.tag import Okt
import re

if __name__ == "__main__":
    convert.convert(); # <- 여기 인자값을 주는 순간 
    rmdup.rmdup(); # <- 이쪽에서 중복제거가 안됨..?