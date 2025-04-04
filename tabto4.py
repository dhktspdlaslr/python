import sys

# 명령줄 인자가 충분히 제공되었는지 확인
if len(sys.argv) < 3:  # 최소한 src와 dst 두 개의 인자가 필요
    print("오류: 입력 파일과 출력 파일 경로를 제공해야 합니다.")
    print("사용법: python tabto4.py <입력 파일 경로> <출력 파일 경로>")
    sys.exit(1)  # 프로그램 종료

# 명령줄에서 입력 파일(src)과 출력 파일(dst) 경로 가져오기
src = sys.argv[1]
dst = sys.argv[2]

try:
    # 입력 파일 열기
    with open(src, "r") as f:
        tab_content = f.read()

    # 탭을 공백 4칸으로 변환
    space_content = tab_content.replace("\t", " " * 4)

    # 변환된 내용을 출력 파일에 저장하기
    with open(dst, "w") as f:
        f.write(space_content)
    
    print(f"변환 완료: {src} -> {dst}")

except FileNotFoundError:
    print(f"오류: 파일 '{src}'(이)가 존재하지 않습니다.")
    sys.exit(1)

except Exception as e:
    print(f"예기치 못한 오류 발생: {e}")
    sys.exit(1)