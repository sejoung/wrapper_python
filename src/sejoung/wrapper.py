import subprocess


def run_script():
    print("여기서 시작...........")
    result = subprocess.run(["python", "/Users/beni/wrapper_python/src/sejoung/run.py"], capture_output=True, text=True)
    print("출력 결과:", result.stdout)
    if result.stderr is not '':
        print("에러 메시지:", result.stderr)
