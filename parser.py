"""
프로젝트명 : 파이선 텍스프파싱 프로젝트
용도 : 텍스트파싱 모듈 작성
시작일 : 2022/02/08
"""
filePath = ""
fileName = "test.txt"
tgtFile = filePath + fileName

# r:읽기, w:쓰기, a: 뒤에 추가
f = open(tgtFile, 'w')

# 데이터 작성 예제
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
    # print(data)
f.close()

f = open(tgtFile, 'r')

# 전체텍스트 읽어서 라인별로 배열 담고 출력
line = f.readlines()
for i in range(1, len(line)):
    print(line[i])

f.close()

# read 함수 테스트
f = open(tgtFile, 'r')
data = f.read()
print(data)
f.close()


class Text:
    def __init__(self):
        self.name = "newFile"

"""
xml파일에서 설정 읽어와서 파싱 전략 선택하도록 DI 구현
팩토리메서드 , 스트레티지 디자인패턴 적용하여 다양한 텍스트파일 처리할 수 있도록 구상
dtd, f2f 처리 가능하도록 api 설계
테스트케이스 작성할 것
다른 시스템에서 돌릴 때 인코딩 이슈나 기타 이슈 확인방법 고려 
"""