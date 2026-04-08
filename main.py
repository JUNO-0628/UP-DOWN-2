# 개발 시작일 : 2026.03.20
# 개발 종료 : 2026.04.03
# UP! & DOWN! 2

import os
import json
import random
import time
from colorama import init, Fore, Back, Style

# 작업 디렉토리를 스크립트가 위치한 곳으로 설정
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DATA_FILE = 'user_data.json'
init(autoreset=True) 

# 유저 데이터
user_data = {
    'name': 'guest',
    'level': 1,
    'exp': 0,
    'money': 0,
    'admin': 0,
    'record': [None,None,None,None],
    'skin': '기본',
    'skin_owned': ['기본']
}

# 유저데이터 저장
def save_data():
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=4)

# 데이터 불러오기
def load_data():
    global user_data
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            user_data = json.load(f)

            # 파일 무결성 검사
            if 'name' not in user_data:
                user_data['name'] = 'guest'
            if 'level' not in user_data:
                user_data['level'] = 1
            if 'exp' not in user_data:
                user_data['exp'] = 0
            if 'money' not in user_data:
                user_data['money'] = 0
            if 'admin' not in user_data:
                user_data['admin'] = 0
            if 'record' not in user_data:
                user_data['record'] = [None,None,None,None]
            if 'skin' not in user_data:
                user_data['skin'] = '기본'
            if 'skin_owned' not in user_data:
                user_data['skin_owned'] = ['기본']

    except Exception as e:
        print('데이터 불러오기 실패', e)
        print('데이터를 초기화합니다...')
        time.sleep(3)
        user_data = {
            'name': 'guest',
            'level': 1,
            'exp': 0,
            'money': 0,
            'admin': 0,
            'record': [None,None,None,None],
            'skin': '기본',
            'skin_owned': ['기본']
        }
        save_data()

# 자동 불러오기 시스템
if os.path.exists(DATA_FILE):
    load_data()
    os.system('cls')
    print(Fore.YELLOW + '[ 파일 확인됨 ]')
    print(f"📂 자동으로 {user_data['name']}의 데이터를 불러옵니다...📂")
    time.sleep(2)
else:
    os.system('cls')
    print(Fore.YELLOW + '게임 최초실행시에만 실행되는 화면입니다. (닉네임은 추후에도 변경 가능합니다.)')
    user_data['name'] = input('닉네임을 설정해주세요: ')
    save_data()

# 기록 업데이트 함수
def update_record(index, attempt):
    if user_data['record'][index] is None:
        user_data['record'][index] = attempt
    else:
        user_data['record'][index] = min(user_data['record'][index], attempt)

# 레벨업 함수
def level_up():
    if user_data['exp'] >= exp_limit:
        while user_data['exp'] >= exp_limit:
            user_data['level'] += 1
            user_data['exp'] -= exp_limit

# 스킨 업데이트 함수
def skin_check():
    global UP_text, DOWN_text
    if user_data['skin'] == '기본':
        UP_text = Fore.RED + 'UP!'
        DOWN_text = Fore.BLUE + 'DOWN!'
    elif user_data['skin'] == '하트':
        UP_text = Fore.MAGENTA + '💖 UP 💖'
        DOWN_text = Fore.MAGENTA + '💖 DOWN 💖'
    elif user_data['skin'] == '별':
        UP_text = Fore.YELLOW + '🌠 UP 🌠'
        DOWN_text = Fore.YELLOW + '🌠 DOWN 🌠'
    elif user_data['skin'] == '캔디':
        UP_text = Fore.CYAN + '🍬 UP 🍬'
        DOWN_text = Fore.CYAN + '🍬 DOWN 🍬'

# 게임 기본 변수
game_version = 'v.1.0'
exp_limit = 100
difficult = ['쉬움', '보통', '어려움', '매우 어려움']

# 게임 메인 루프
while True:
    load_data()
    skin_check()
    os.system('cls')
    print(Fore.YELLOW + '[ UP! & DOWN! II ]')
    print(f'이름: {user_data['name']}, 돈: {user_data["money"]}')
    print(f'레벨: {user_data["level"]} [경험치: { user_data["exp"]}/100]')
    print(f'현재 스킨: {user_data["skin"]}')
    print('1. 게임시작 / 2. 상점 / 3. 기록 / 4. 설정 / 5. 게임종료')
    menu_selc = input(Fore.YELLOW + '메뉴를 선택해주세요: ')

    # 게임코드
    if menu_selc == '1':
        clear = 0
        while True:
            if clear == 0:
                os.system('cls')
                print('[ 난이도 ]')
                print('1. 쉬움 / 2. 보통 / 3. 어려움 / 4. 매우 어려움 / 5. 나가기')
                difficult_selc = input('난이도를 선택해주세요: ')
                if difficult_selc == '1':
                    answer = random.randint(1, 50)
                    num = 50
                    diff = '쉬움'
                    diff_exp = 25
                    diff_money = 50
                elif difficult_selc == '2':
                    answer = random.randint(1, 100)
                    num = 100
                    diff = '보통'
                    diff_exp = 50
                    diff_money = 100
                elif difficult_selc == '3':
                    answer = random.randint(1, 1000)
                    num = 1000
                    diff = '어려움'
                    diff_exp = 100
                    diff_money = 250
                elif difficult_selc == '4':
                    answer = random.randint(1, 10000)
                    num = 10000
                    diff = '매우 어려움'
                    diff_exp = 150
                    diff_money = 500
                elif difficult_selc == '5':
                    break
                attempt = 0
                os.system('cls')
                print(Fore.YELLOW + ('현재 난이도:' + diff))
                while True:
                    try:
                        user_num = int(input(f'1 ~ {num}까지 랜덤한 숫자를 맞춰보세요 :'))
                    except ValueError:
                        print("숫자만 입력해주세요!")
                        continue  # 다시 입력받도록 반복문 처음으로 돌아감

                    if user_num == answer:
                        print('정답입니다!')
                        print(f'시도횟수 : {attempt}')
                        update_record(int(difficult_selc)-1, attempt)
                        level_up()
                        user_data['money'] += diff_money
                        user_data['exp'] += diff_exp
                        
                        print(f'돈 +{diff_money}, 경험치 +{diff_exp}')
                        input('엔터를 눌러 돌아가기')
                        clear = 1
                        save_data()
                        break

                    elif user_num > answer:
                        print(DOWN_text)
                        attempt += 1

                    elif user_num < answer:
                        print(UP_text)
                        attempt += 1
            else:
                break

    # 상점
    elif menu_selc == '2':
        while True:
            os.system('cls')
            print(Fore.YELLOW + '[ 스킨 상점 ]')
            # 하트
            if '하트' in user_data['skin_owned']:
                if user_data['skin'] == '하트':
                    print("1." + Fore.MAGENTA + '💖 UP 💖 / 💖 DOWN 💖'+ Fore.BLUE + ' [장착중]')
                else:
                    print("1." + Fore.MAGENTA + '💖 UP 💖 / 💖 DOWN 💖'+ Fore.GREEN + ' [보유중]')
            else:
                print("1." + Fore.MAGENTA + '💖 UP 💖 / 💖 DOWN 💖', ' [가격 : 1500원]')
            # 별
            if '별' in user_data['skin_owned']:
                if user_data['skin'] == '별':
                    print("2." + Fore.YELLOW + '🌠 UP 🌠 / 🌠 DOWN 🌠'+ Fore.BLUE + ' [장착중]')
                else:
                    print("2." + Fore.YELLOW + '🌠 UP 🌠 / 🌠 DOWN 🌠'+ Fore.GREEN + ' [보유중]')
            else:
                print("2." + Fore.YELLOW + '🌠 UP 🌠 / 🌠 DOWN 🌠', ' [가격 : 2500원]')

            # 캔디
            if '캔디' in user_data['skin_owned']:
                if user_data['skin'] == '캔디':
                    print("3." + Fore.CYAN + '🍬 UP 🍬 / 🍬 DOWN 🍬'+ Fore.BLUE + ' [장착중]')
                else:
                    print("3." + Fore.CYAN + '🍬 UP 🍬 / 🍬 DOWN 🍬'+ Fore.GREEN + ' [보유중]')
            else:
                print("3." + Fore.CYAN + '🍬 UP 🍬 / 🍬 DOWN 🍬', ' [가격 : 3500원]')

            print('4. 나가기')
            shop_selc = input(Fore.YELLOW + '메뉴를 선택해주세요: ')

            # 하트 구매/장착
            if shop_selc == '1':
                if '하트' in user_data['skin_owned']:
                    os.system('cls')
                    print('스킨이 장착되었습니다.')
                    user_data['skin'] = '하트'
                    save_data()
                    input('Enter를 눌러 돌아가기')
                elif user_data['money'] >= 1500:
                    user_data['money'] -= 1500
                    user_data['skin_owned'].append('하트')
                    save_data()
                    os.system('cls')
                    print('구매가 완료되었습니다.')
                    input('Enter를 눌러 돌아가기')
                else:
                    os.system('cls')
                    print('돈이 부족합니다.')
                    input('Enter를 눌러 돌아가기')
            
            # 별 구매/장착
            if shop_selc == '2':
                if '별' in user_data['skin_owned']:
                    os.system('cls')
                    print('스킨이 장착되었습니다.')
                    user_data['skin'] = '별'
                    save_data()
                    input('Enter를 눌러 돌아가기')
                elif user_data['money'] >= 2500:
                    user_data['money'] -= 2500
                    user_data['skin_owned'].append('별')
                    save_data()
                    os.system('cls')
                    print('구매가 완료되었습니다.')
                    input('Enter를 눌러 돌아가기')
                else:
                    os.system('cls')
                    print('돈이 부족합니다.')
                    input('Enter를 눌러 돌아가기')
            
            # 캔디 구매/장착
            elif shop_selc == '3':
                if '캔디' in user_data['skin_owned']:
                    os.system('cls')
                    print('스킨이 장착되었습니다.')
                    user_data['skin'] = '캔디'
                    save_data()
                    input('Enter를 눌러 돌아가기')
                elif user_data['money'] >= 3500:
                    user_data['money'] -= 3500
                    user_data['skin_owned'].append('캔디')
                    save_data()
                    os.system('cls')
                    print('구매가 완료되었습니다.')
                    input('Enter를 눌러 돌아가기')
                else:
                    os.system('cls')
                    print('돈이 부족합니다.')
                    input('Enter를 눌러 돌아가기')

            elif shop_selc == '4':
                break
    # 기록 (리더보드)
    elif menu_selc == '3':
        os.system('cls')
        print(Fore.YELLOW + '[ 기록 ]')
        for i, rec in enumerate(user_data['record']):
            if rec is not None:
                print(f'{difficult[i]} : {rec}회')
            else:
                print(f'{difficult[i]} : 기록 없음')
        input('Enter를 눌러 돌아가기')

    # 설정
    elif menu_selc == '4':
        while True:
            os.system('cls')
            print(Fore.YELLOW + '[ 설정 ]')
            print('1. 닉네임 변경 / 2. 데이터 초기화 / 3. 패치 노트 / 4. 나가기')
            setting_menu = input('메뉴를 선택해주세요: ')
            # 닉네임 변경
            if setting_menu == '1':
                os.system('cls')
                user_data['name'] = input('변경할 닉네임을 입력해 주세요: ')
                save_data()
            
            # 초기화
            elif setting_menu == '2':
                os.system('cls')
                print('[ 초기화 ]')
                reset_input = input('초기화 하시겠습니까? y/n : ')
                if reset_input.lower() == 'y':
                    user_data = {
                        'name': 'guest',
                        'level': 1,
                        'exp': 0,
                        'money': 0,
                        'admin': 0,
                        'record': [None,None,None,None],
                        'skin': '기본',
                        'skin_owned': ['기본']
                    }
                    save_data()
                    print('초기화 하였습니다.')
                    time.sleep(2)
                elif reset_input.lower() == 'n':
                    print('취소되었습니다.')
                    time.sleep(2)

            # 패치노트
            elif setting_menu == '3':
                os.system('cls')
                print(Fore.YELLOW + '[ 패치 노트 ]')
                print(f'2026.04.03 - {game_version}')
                print('- 무결성 검사 코드 오류 수정')
                print('- 자동 불러오기 시스템 개선')
                print('- 스킨 가격 조정')
                print('- 게임종료 코드 개선(약 2초 단축)')
                print('- 추가적인 디자인 개선')
                print('- 게임 실행 오류 수정')
                print('==================================')
                print('업다운2의 마지막 업데이트입니다. 사후지원은 할 예정입니다!')
                input('Enter를 눌러 돌아가기')

            # 설정 나가기
            elif setting_menu == '4':
                break 

    # 게임 종료
    elif menu_selc == '5':
        os.system('cls')
        print('📂 데이터를 저장중입니다...📂')
        save_data()
        time.sleep(0.2)
        print('✅ 성공적으로 저장되었습니다! 게임을 종료합니다...✅')
        time.sleep(1)
        break
    
    # 디버그) 인게임에서 변수나 리스트 확인하는 용도
    elif menu_selc == 'debug':
        os.system('cls')
        print(user_data) # 유저 데이터
        print(f'버전: {game_version}') # 게임 버전
        input()