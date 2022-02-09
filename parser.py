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