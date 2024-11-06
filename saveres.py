import os
import re
import matplotlib.pyplot as plt
from datetime import datetime

# 분석할 텍스트 파일의 이름을 여기에 입력하세요
file_path = 'log_20241105_151307.txt'  # 예: 'your_file.txt'


# 파일에서 Epoch와 Accuracy 데이터 읽기
def read_data_from_txt(file_path):
    epochs = []
    accuracies = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'Accuracy at (\d+) epochs is : ([\d.]+)%', line)
            if match:
                epoch = int(match.group(1))
                accuracy = float(match.group(2))
                epochs.append(epoch)
                accuracies.append(accuracy)
    return epochs, accuracies


# 그래프 그리기 및 저장
def plot_accuracy_graph(epochs, accuracies):
    plt.figure(figsize=(8, 6))  # 16:9 비율 설정
    plt.plot(epochs, accuracies, marker='o')
    plt.xlabel('Epoch', weight='bold')
    plt.ylabel('Accuracy (%)', weight='bold')
    plt.title('Accuracy per Epoch', weight='bold')
    plt.grid(False)

    # x, y 축 범위 설정
    plt.xlim(-5, max(epochs)+5)
    plt.xticks(range(0, max(epochs) + 1, 25), weight='bold')
    plt.ylim(0, 100)
    plt.yticks(weight='bold')

    # 파일명에서 .txt 부분을 제거하고 폴더 이름으로 사용
    folder_name = os.path.splitext(os.path.basename(file_path))[0]
    save_path = f"./res/{folder_name}/"
    os.makedirs(save_path, exist_ok=True)

    # 그래프 저장
    plt.savefig(f"{save_path}accuracy_epoch_graph.png")
    # 그래프 화면에 표시
    plt.show()

    plt.close()

    return save_path


# 최고 Accuracy와 해당 Epoch 출력 및 저장
def save_max_accuracy(epochs, accuracies, save_path):
    max_accuracy = max(accuracies)
    max_epoch = epochs[accuracies.index(max_accuracy)]

    # 결과 출력
    print(f"최고 Accuracy: {max_accuracy}% (Epoch: {max_epoch})")

    # 결과 저장
    with open(f"{save_path}max_accuracy.txt", 'w') as file:
        file.write(f"최고 Accuracy: {max_accuracy}% (Epoch: {max_epoch})\n")


# 메인 함수
def main():
    epochs, accuracies = read_data_from_txt(file_path)
    save_path = plot_accuracy_graph(epochs, accuracies)
    save_max_accuracy(epochs, accuracies, save_path)


if __name__ == '__main__':
    main()
