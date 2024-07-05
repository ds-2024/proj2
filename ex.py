# STEP 1
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis


# STEP 2 추론기 만들기. 모델 자동 다운
app = FaceAnalysis()
app.prepare(ctx_id=0, det_size=(640,640))

# STEP 3 데이터 가져오기
img1 = cv2.imread("huhuhuhu.jpg")
img2 = cv2.imread("han.jpg")

# STEP 4 추론. 무결성 테스트
faces1 = app.get(img1)
faces2 = app.get(img2)
assert len(faces1)==1
assert len(faces2)==1


print(faces1[0])

# # STEP 5 응용.가져오기
rimg = app.draw_on(img2, faces2)
cv2.imwrite("./huhuhuhu_output.jpg", rimg) #app.draw_on 함수를 사용하여 img2 이미지에 얼굴을 그리고, 그 결과를 "./huhuhuhu_output.jpg" 파일로 저장하는 것을 의미

feat1 = np.array(faces1[0].normed_embedding, dtype=np.float32)
feat2 = np.array(faces2[0].normed_embedding, dtype=np.float32)
sims = np.dot(feat1, feat2.T) #임베딩, normed파일 형태, 유사도 계산
print(sims)

