import sys
from time import sleep

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("파일 경로를 입력해주세요.")

    file_path = sys.argv[1]
    if len(file_path) < 1:
        raise Exception("파일 경로를 입력해주세요.2")

    print("file path: ", file_path)

    print("Hello, Python!")
    sleep(1)
    print("ok, bye!")
