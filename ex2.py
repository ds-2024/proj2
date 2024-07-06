def profile(name, lang, age=17):
    print("이름:{0}\t 사용언어:{1}\t 나이:{2}".format(name, lang, age))

profile("김일일", "파이썬")

def std_weight(height, gender):
    if gender =="남자":
        return height*height *22
    else:
        return height*height *21

height =175
gender ="남자"
weight = std_weight(height / 100, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight)) 

#시험성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 공부중")