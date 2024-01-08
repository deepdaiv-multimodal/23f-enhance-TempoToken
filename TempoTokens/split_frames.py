import cv2
import os
import numpy as np

def extract_frames(video_path, num_frames=5, output_folder='frames'):
    cap = cv2.VideoCapture(video_path)
    
    # 프레임 수 확인
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # 프레임 간격 계산
    interval = max(1, total_frames // num_frames)
    
    # 저장할 폴더 생성
    os.makedirs(output_folder, exist_ok=True)
    
    # 프레임 추출
    frame_count = 0
    frames = []
    
    while frame_count < total_frames:
        ret, frame = cap.read()
        if frame_count % interval == 0:
            frames.append(frame)
        frame_count += 1
    
    # 5개의 프레임을 가로로 이어붙이기
    result_image = np.concatenate(frames, axis=1)
    
    # 결과 이미지 저장
    result_filename = f"{output_folder}/{os.path.splitext(os.path.basename(video_path))[0]}_result.jpg"
    cv2.imwrite(result_filename, result_image)
    
    # 자원 해제
    cap.release()

# 비디오 파일 경로 지정
for i in range(1, 4):
    video_path = f'clap{i}.mp4'
    print(video_path)
    # 5개의 프레임을 가로로 이어붙여서 저장
    extract_frames(video_path, num_frames=5, output_folder='frames')
