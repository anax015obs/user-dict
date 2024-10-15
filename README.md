위키피디아 제목을
korean_noun.parquet으로 저장 한다.

py index.py를 돌리고 난 후

~의 로 끝나는(의$) 단어들을
korean_noun_result.txt에서 추출하여 archive/josa(n).txt에 저장.

수작업으로 조사 분리 해준다.
이때 다음 정규표현식을 활용한다.
[가-힣]{1,}[^주|회|\n]의
왠만하면 이 정규표현식에 캡쳐되는것들만 고치면 된다.
다만 100%는 아님.

그리고 korean_noun_result.txt를 archive/user_dict(n).txt로 복제한 후
~의 를 제거

archive/user_dict(n).txt에 다음 두 파일 내용을 추가한다.

1. archive/josa(n).txt
2. archive/additional.txt
