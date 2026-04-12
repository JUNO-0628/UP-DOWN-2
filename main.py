# 개발 시작일 : 2026.03.20
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
    'challenge_record' : None,
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
            if 'challenge_record' not in user_data:
                user_data['challenge_record'] = None
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
            'challenge_record' : None,
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
    time.sleep(1)
else:
    os.system('cls')
    print(Fore.YELLOW + '게임 최초실행 시 실행되는 화면입니다. (닉네임은 추후 설정에서 변경 가능합니다.)')
    user_data['name'] = input('닉네임을 설정해주세요: ')
    save_data()

# 일반 모드 기록 업데이트 함수
def update_record(index, attempt):
    if user_data['record'][index] is None:
        user_data['record'][index] = attempt
    else:
        user_data['record'][index] = min(user_data['record'][index], attempt)

# 챌린지 모드 기록 업데이트 함수
def update_challenge_record(challenge_round):
    if user_data['challenge_record'] is None:
        user_data['challenge_record'] = challenge_round
    else:
        user_data['challenge_record'] = max(user_data['challenge_record'], challenge_round)

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
    elif user_data['skin'] == '파도':
        UP_text = Fore.CYAN + '🌊 UP 🌊'
        DOWN_text = Fore.CYAN + '🌊 DOWN 🌊'

# cls (터미널 클리어 함수)
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# 게임 기본 변수
game_version = 'v.1.35'
exp_limit = 100 # 경험치는 고정
difficult = ['쉬움', '보통', '어려움', '매우 어려움']

# 게임 메인 루프
while True:
    cls()
    load_data()
    skin_check()
    print(Fore.YELLOW + '[ UP! & DOWN! 2 ]')
    print(f'이름: {user_data['name']}')
    print(f'레벨: {user_data["level"]} [경험치: { user_data["exp"]}/100]')
    print(f'돈: {user_data["money"]} | 스킨: '+ Fore.YELLOW + f'{user_data["skin"]}')
    print('1. 게임시작 | 2. 상점 | 3. 기록 | 4. 설정 | 5. 게임종료')
    menu_selc = input(Fore.YELLOW + '메뉴를 선택해주세요: ')

    # 게임코드
    if menu_selc == '1':
        clear = 0
        while True:
            if clear == 0:
                cls()
                print(Fore.YELLOW + '[ 게임모드 선택 ]')
                print('1. 일반 모드 | 2. 챌린지 모드 |3. ❌ 나가기❌')
                game_mode = input(Fore.YELLOW + '게임모드를 선택해 주세요 : ')
                
                # 일반 모드
                if game_mode == '1':
                    while True:
                        if clear == 0:
                            cls()
                            print('[ 난이도 ]')
                            print('1.😊 쉬움😊  | 2.🙂 보통🙂 | 3.☹️ 어려움☹️  | 4.😡 매우 어려움😡 | 5.❌ 나가기❌')
                            difficult_selc = input(Fore.YELLOW + '난이도를 선택해주세요: ')
                            if difficult_selc == '1':
                                answer = random.randint(1, 50)
                                num = 50
                                diff = '😊 쉬움😊'
                                diff_exp = 25
                                diff_money = 50
                                diff_num = 0
                            elif difficult_selc == '2':
                                answer = random.randint(1, 100)
                                num = 100
                                diff = '🙂 보통🙂'
                                diff_exp = 50
                                diff_money = 100
                                diff_num = 1
                            elif difficult_selc == '3':
                                answer = random.randint(1, 1000)
                                num = 1000
                                diff = '☹️ 어려움☹️'
                                diff_exp = 100
                                diff_money = 250
                                diff_num = 2
                            elif difficult_selc == '4':
                                answer = random.randint(1, 10000)
                                num = 10000
                                diff = '😡 매우 어려움😡'
                                diff_exp = 200
                                diff_money = 500
                                diff_num = 3
                            elif difficult_selc == '5':
                                break
                            else:
                                print("올바른 난이도를 선택해주세요 (1~5)")
                                continue

                            attempt = 0
                            cls()
                            print('[ 일반 모드 ]')
                            print(Fore.YELLOW + ('현재 난이도:' + diff))
                            if user_data['record'][diff_num] == None:
                                print(Fore.YELLOW + f'현재 난이도 최고기록 : ❌ 기록없음❌')
                            else:
                                print(Fore.YELLOW + f'현재 난이도 최고기록 : 👑 {user_data['record'][diff_num]}회👑')
                            while True:
                                try:
                                    user_num = int(input(f'1 ~ {num}까지 랜덤한 숫자를 맞춰보세요 :'))
                                except ValueError:
                                    print("숫자만 입력해주세요!")
                                    continue  # 다시 입력받도록 반복문 처음으로 돌아감

                                if user_num == answer:
                                    cls()
                                    print(Fore.YELLOW + '정답입니다!')
                                    print('==============================')
                                    if user_data['record'][diff_num] is None or user_data['record'][diff_num] > attempt:
                                        print(Fore.YELLOW + '신기록!')
                                    print(f'현재 시도 횟수 : {attempt}회')
                                    if user_data['record'][diff_num] == None:
                                        print('이전 최고 기록 : ❌ 기록 없음❌')
                                    else:
                                        print(f'이전 최고 기록 : {user_data['record'][diff_num]}회')
                                    update_record(int(difficult_selc)-1, attempt)
                                    print('==============================')
                                    user_data['money'] += diff_money
                                    user_data['exp'] += diff_exp
                                    level_up()
                                    
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

                # 챌린지 모드
                elif game_mode == '2':
                    clear = 0
                    lives = 10
                    challenge_round = 1
                    answer = random.randint(1, 1000)
                    cls()
                    print(Fore.YELLOW + '[ 챌린지 모드 ]')
                    print(f'현재 라운드 : {challenge_round}')
                    print('목숨이 0이 되면 게임오버 됩니다!!')
                    while True:
                        if lives > 0:
                            try:
                                print(Fore.YELLOW + f'목숨 : {lives}')
                                user_num = int(input(f'1 ~ 1000까지 랜덤한 숫자를 맞춰보세요 : '))
                            except ValueError:
                                print("숫자만 입력해주세요!")
                                continue  # 다시 입력받도록 반복문 처음으로 돌아감
                            
                            # 정답
                            if user_num == answer:
                                cls()
                                print('정답입니다!')
                                input('Enter를 눌러 다음라운드로...')
                                challenge_round += 1
                                
                                lives += 10
                                answer = random.randint(1, 1000)

                                cls()
                                print(Fore.YELLOW + '[ 챌린지 모드 ]')
                                print(f'현재 라운드 : {challenge_round}')
                                print('목숨이 0이 되면 게임오버 됩니다!!')

                            # 업
                            elif user_num < answer:
                                print(f'{UP_text} | 목숨 -1')
                                lives -= 1
                                
                            # 다운
                            elif user_num > answer:
                                print(f'{DOWN_text} | 목숨 -1')
                                lives -= 1
                            
                        else:
                            cls()
                            print('게임 오버')
                            print(f'경험치 +{150 * (challenge_round - 1)}')
                            print(f'돈 +{350 * (challenge_round - 1)}')
                            input('Enter를 눌러 돌아가기')
                            user_data['exp'] += 150 * (challenge_round - 1)
                            user_data['money'] += 350 * (challenge_round - 1)
                            level_up()
                            update_challenge_record(challenge_round)
                            clear = 1
                            save_data()
                            break

                # 나가기
                elif game_mode == '3':
                    break

            else:
                break

    # 상점
    elif menu_selc == '2':
        while True:
            cls()
            print(Fore.YELLOW + '[ 스킨 상점 ]')
            # 하트
            if '하트' in user_data['skin_owned']:
                if user_data['skin'] == '하트':
                    print("1. 하트 | " + Fore.MAGENTA + '💖 UP 💖 | 💖 DOWN 💖'+ Fore.BLUE + ' [장착중]')
                else:
                    print("1. 하트 | " + Fore.MAGENTA + '💖 UP 💖 | 💖 DOWN 💖'+ Fore.GREEN + ' [보유중]')
            else:
                print("1. 하트 | " + Fore.MAGENTA + '💖 UP 💖 | 💖 DOWN 💖', ' [가격 : 1500원]')
            # 별
            if '별' in user_data['skin_owned']:
                if user_data['skin'] == '별':
                    print("2. 별   | " + Fore.YELLOW + '🌠 UP 🌠 | 🌠 DOWN 🌠'+ Fore.BLUE + ' [장착중]')
                else:
                    print("2. 별   | " + Fore.YELLOW + '🌠 UP 🌠 | 🌠 DOWN 🌠'+ Fore.GREEN + ' [보유중]')
            else:
                print("2. 별   | " + Fore.YELLOW + '🌠 UP 🌠 | 🌠 DOWN 🌠', ' [가격 : 2500원]')

            # 파도
            if '파도' in user_data['skin_owned']:
                if user_data['skin'] == '파도':
                    print("3. 파도 | " + Fore.CYAN + '🌊 UP 🌊 | 🌊 DOWN 🌊'+ Fore.BLUE + ' [장착중]')
                else:
                    print("3. 파도 | " + Fore.CYAN + '🌊 UP 🌊 | 🌊 DOWN 🌊'+ Fore.GREEN + ' [보유중]')
            else:
                print("3. 파도 | " + Fore.CYAN + '🌊 UP 🌊 | 🌊 DOWN 🌊', ' [가격 : 3500원]')

            print('4. 나가기')
            shop_selc = input(Fore.YELLOW + '메뉴를 선택해주세요: ')

            # 하트 구매/장착
            if shop_selc == '1':
                if '하트' in user_data['skin_owned']:
                    cls()
                    print('스킨이 장착되었습니다.')
                    user_data['skin'] = '하트'
                    save_data()
                    input('Enter를 눌러 돌아가기')
                elif user_data['money'] >= 1500:
                    user_data['money'] -= 1500
                    user_data['skin_owned'].append('하트')
                    save_data()
                    cls()
                    print('구매가 완료되었습니다.')
                    input('Enter를 눌러 돌아가기')
                else:
                    cls()
                    print('돈이 부족합니다.')
                    input('Enter를 눌러 돌아가기')
            
            # 별 구매/장착
            if shop_selc == '2':
                if '별' in user_data['skin_owned']:
                    cls()
                    print('스킨이 장착되었습니다.')
                    user_data['skin'] = '별'
                    save_data()
                    input('Enter를 눌러 돌아가기')
                elif user_data['money'] >= 2500:
                    user_data['money'] -= 2500
                    user_data['skin_owned'].append('별')
                    save_data()
                    cls()
                    print('구매가 완료되었습니다.')
                    input('Enter를 눌러 돌아가기')
                else:
                    cls()
                    print('돈이 부족합니다.')
                    input('Enter를 눌러 돌아가기')
            
            # 파도 구매/장착
            elif shop_selc == '3':
                if '파도' in user_data['skin_owned']:
                    cls()
                    print('스킨이 장착되었습니다.')
                    user_data['skin'] = '파도'
                    save_data()
                    input('Enter를 눌러 돌아가기')
                elif user_data['money'] >= 3500:
                    user_data['money'] -= 3500
                    user_data['skin_owned'].append('파도')
                    save_data()
                    cls()
                    print('구매가 완료되었습니다.')
                    input('Enter를 눌러 돌아가기')
                else:
                    cls()
                    print('돈이 부족합니다.')
                    input('Enter를 눌러 돌아가기')

            elif shop_selc == '4':
                break

    # 기록 (리더보드)
    elif menu_selc == '3':
        cls()
        print(Fore.YELLOW + '👑 난이도👑    👑 기록👑')
        print('====================================')
        if user_data['record'][0] == None:
            print(f'    쉬움     | ❌ 기록없음❌')
        else:
            print(f'    쉬움     | 👑 {user_data['record'][0]} 회👑')

        if user_data['record'][1] == None:
            print(f'    보통     | ❌ 기록없음❌')
        else:
            print(f'    보통     | 👑 {user_data['record'][1]} 회👑')

        if user_data['record'][2] == None:
            print(f'   어려움    | ❌ 기록없음❌')
        else:
            print(f'   어려움    | 👑 {user_data['record'][2]} 회👑')

        if user_data['record'][3] == None:
            print(f' 매우 어려움 | ❌ 기록없음❌')
        else:
            print(f' 매우 어려움 | 👑 {user_data['record'][3]} 회👑')
        print('====================================')
        if user_data['challenge_record'] == None:
            print(' 챌린지 모드 | ❌ 기록없음❌')
        else:
            print(f' 챌린지 모드 | 👑 {user_data['challenge_record']}라운드👑')
        print('====================================')
        input('Enter를 눌러 돌아가기')

    # 설정
    elif menu_selc == '4':
        while True:
            cls()
            print(Fore.YELLOW + '[ 설정 ]')
            print('1.♻️ 닉네임 변경 | 2.⚠️ 데이터 초기화 | 3.📋 패치 노트 | 4.❌ 나가기')
            setting_menu = input('메뉴를 선택해주세요: ')
            # 닉네임 변경
            if setting_menu == '1':
                cls()
                print(f'현재 닉네임 : {user_data['name']}')
                user_data['name'] = input('변경할 닉네임을 입력해 주세요: ')
                save_data()
                print(f'✅ 닉네임을 {user_data['name']}으로 변경하였습니다!✅')
                input('Enter를 눌러 돌아가기')
            
            # 초기화
            elif setting_menu == '2':
                cls()
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
                        'challenge_record' : None,
                        'skin': '기본',
                        'skin_owned': ['기본']
                    }
                    save_data()
                    cls()
                    print('⚠️ 초기화 하였습니다.⚠️')
                    time.sleep(2)
                elif reset_input.lower() == 'n':
                    cls()
                    print('❌ 취소되었습니다.❌')
                    time.sleep(2)

            # 패치노트
            elif setting_menu == '3':
                cls()
                print(Fore.YELLOW + '[ 패치 노트 ]')
                print(f'2026.04.12 - {game_version}')
                print('=======================================')
                print('- 챌린지 모드 추가')
                print('- 챌린지 모드 기록 추가')
                print('- 게임 클리어 시 얻는 보상 조정 (상향)')
                print('- 이모지가 정상적으로 출력되지 않는 현상 수정')
                print('- 추가적인 메모리 최적화')
                print('- 코드 간소화')
                print('- 무결성 검사 코드 수정')
                print('=======================================')
                input('Enter를 눌러 돌아가기')

            # 설정 나가기
            elif setting_menu == '4':
                break 

            # 디버그
            elif setting_menu == 'debug':
                cls()
                print(user_data) # 유저 데이터
                print(f'버전: {game_version}') # 게임 버전
                input()
                
    # 게임 종료
    elif menu_selc == '5':
        cls()
        print('📂 데이터를 저장중입니다...📂')
        save_data()
        time.sleep(0.2)
        print('✅ 성공적으로 저장되었습니다! 게임을 종료합니다...✅')
        time.sleep(1)
        break
