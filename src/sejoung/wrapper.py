import subprocess


def run_script(absolute_path: str, arg: str):
    print("여기서 시작...........")
    result = subprocess.run(["python", absolute_path, arg], capture_output=True, text=True)
    print("출력 결과:", result.stdout)
    if result.stderr is not '':
        print("에러 메시지:", result.stderr)
        raise Exception(result.stderr)
