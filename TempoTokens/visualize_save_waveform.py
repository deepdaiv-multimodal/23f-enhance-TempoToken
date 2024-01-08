import librosa
import librosa.display
import matplotlib.pyplot as plt

def visualize_save_waveform(audio_path, output_path):
    # 오디오 파일 로드
    y, sr = librosa.load(audio_path)

    # 오디오 파형 그리기
    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title('Waveform of the Audio')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    # 이미지 파일로 저장
    plt.savefig(output_path)
    plt.close()

# 예시: clap.m4a 오디오 파일의 파형을 'waveform.png'로 저장
visualize_save_waveform('audios\clap.m4a', 'clap_audio.png')
