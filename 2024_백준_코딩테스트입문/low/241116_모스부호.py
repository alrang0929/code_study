import sys
sys.stdin = open('input.txt','r')

# 앞의 학생 배열과 유사하다고 생각함..
# N = 문자열의 길이

'''
for i in mos:
    if i == '.-' : text += 'A'
    elif i == '-...' : text += 'B'
    elif i == '-.-.' : text += 'C'
    elif i == '-..' : text += 'D'
    elif i == '.' : text += 'E'
    elif i == '..-.' : text += 'F'
    elif i == '--.' : text += 'G'
    elif i == '....' : text += 'H'
    elif i == '..' : text += 'I'
    elif i == '.---' : text += 'J'
    elif i == '-.-' : text += 'K'
    elif i == '.-..' : text += 'L'
    elif i == '--' : text += 'M'
    elif i == '-.' : text += 'N'
    elif i == '---' : text += 'O'
    elif i == '.--.' : text += 'P'
    elif i == '--.-' : text += 'Q'
    elif i == '.-.' : text += 'R'
    elif i == '...' : text += 'S'
    elif i == '-' : text += 'T'
    elif i == '..-' : text += 'U'
    elif i == '...-' : text += 'V'
    elif i == '.--' : text += 'W'
    elif i == '-..-' : text += 'X'
    elif i == '-.--' : text += 'Y'
    elif i == '--..' : text += 'Z'
    elif i == '.----' : text += '1'
    elif i == '..---' : text += '2'
    elif i == '...--' : text += '3'
    elif i == '....-' : text += '4'
    elif i == '.....' : text += '5'
    elif i == '-....' : text += '6'
    elif i == '--...' : text += '7'
    elif i == '---..' : text += '8'
    elif i == '----.' : text += '9'
    elif i == '-----' : text += '0'
    elif i == '--..--' : text += ','
    elif i == '.-.-.-' : text += '.'
    elif i == '..--..' : text += '?'
    elif i == '---...' : text += ':'
    elif i == '-....-' : text += '-'
    elif i == '.--.-.' : text += '@'

..왠지 똑똑한 청년이 된거 같아 딕셔너리로 수정
'''
morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?',
    '---...': ':', '-....-': '-', '.--.-.': '@'
}

N = int(input())
morse_code = input()
text = ''
current_code = ''  # 현재 모스 부호를 저장하는 변수

for char in morse_code:
    if char == '.' or char == '-':
        current_code += char  # 현재 모스 부호에 문자 추가
    else:  # 공백을 만난 경우
        text += morse_code_dict.get(current_code, '')  # 현재 모스 부호 해독
        current_code = ''  # 현재 모스 부호 초기화

text += morse_code_dict.get(current_code, '')  # 마지막 모스 부호 해독
print(text)