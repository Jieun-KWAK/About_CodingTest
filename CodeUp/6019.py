#"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
year, mon, day = map(str, input().split("."))
print(f"{day}-{mon}-{year}")