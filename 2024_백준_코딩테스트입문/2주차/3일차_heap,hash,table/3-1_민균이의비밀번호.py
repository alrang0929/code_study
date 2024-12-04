'''
[문제]
창영이는 민균이의 컴퓨터를 해킹해 텍스트 파일 하나를 자신의 메일로 전송했다. 파일에는 단어가 한 줄에 하나씩 적혀있었고, 이 중 하나는 민균이가 온라인 저지에서 사용하는 비밀번호이다.

파일을 살펴보던 창영이는 모든 단어의 길이가 홀수라는 사실을 알아내었다. 그리고 언젠가 민균이가 이 목록에 대해서 얘기했던 것을 생각해냈다. 민균이의 비밀번호는 목록에 포함되어 있으며, 비밀번호를 뒤집어서 쓴 문자열도 포함되어 있다.

예를 들어, 민균이의 비밀번호가 "tulipan"인 경우에 목록에는 "napilut"도 존재해야 한다. 알 수 없는 이유에 의해 모두 비밀번호로 사용 가능하다고 한다.

민균이의 파일에 적혀있는 단어가 모두 주어졌을 때, 비밀번호의 길이와 가운데 글자를 출력하는 프로그램을 작성하시오.


[입력]
첫째 줄에 단어의 수 N (2 ≤ N ≤ 100)이 주어진다. 다음 N개 줄에는 파일에 적혀있는 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 소문자로만 이루어져 있으며, 길이는 2보다 크고 14보다 작은 홀수이다.

[츨력]
첫째 줄에 비밀번호의 길이와 가운데 글자를 출력한다. 항상 답이 유일한 경우만 입력으로 주어진다.

[예제입력 1]
4
las
god
psala
sal

[예제 출력1]
3 a

'''

# 비밀번호의 길이와 가운데 글자를 출력
# 모든 문자열은 홀수
# 9933 문제번호

import sys

sys.stdin = open("input.txt","r")

def find_password_with_set(n, words):
    word_set = set(words)  # 단어를 집합으로 저장

    for word in words:
        reversed_word = word[::-1]
        if reversed_word in word_set:  # 집합에서 역순 단어 확인
            length = len(word)
            middle_char = word[length // 2] #몫 = 가운데
            return length, middle_char

    return None  # 정상적인 입력에서는 이 부분에 도달하지 않음

# 입력 처리
n = int(input())
words = [input().strip() for _ in range(n)]

# 비밀번호 찾기
length, middle_char = find_password_with_set(n, words)
print(length, middle_char)
