# 연락처(전화번호부) 관리

# 상황: 친구들 전화번호를 저장하고 검색하는 프로그램이 필요하다.

# 요구사항 — 메뉴를 반복(while)하며 다음 기능 제공
# 1. 추가: 이름과 번호를 입력받아 딕셔너리에 저장 {이름: 번호}
# 2. 검색: 이름으로 번호 찾기 (get 으로 없으면 안내)
# 3. 삭제: 이름으로 연락처 삭제
# 4. 전체 목록: 모든 연락처 출력 (items() 순회)
# 5. 종료: 반복 끝내기

# 출력 예:
# 메뉴 선택: 2
# 검색할 이름: 김철수
# 김철수: 010-1234-5678
# 힌트: contacts = {}, while True + if/elif 메뉴 분기, break 로 종료

contacts = {}

while True:
    try:
        response = int(input(
            '1. 추가\n' \
            '2. 검색\n' \
            '3. 삭제\n' \
            '4. 전체 목록\n' \
            '5. 종료\n' \
            '원하시는 항목을 입력해주세요: '))
            
        if response == 1:
            name = input('추가할 이름: ')
            while True:
                try:
                    phone = input('추가할 번호(숫자만): ')
                    if phone.isdigit() and len(phone) == 11:
                        contacts[name] = phone
                        print('추가되었습니다.')
                        break
                    else:
                        print('전화번호는 숫자만 11자리로 입력해주세요. (예: 01012345678)')

                except ValueError:
                    print('숫자를 입력해주세요.')
        
        elif response == 2:
            name = input('검색할 이름: ')
            phone = contacts.get(name, '등록된 정보가 없습니다.')
            if name in contacts:
                print(f'{name}: {phone}')
            else:
                print(phone)

        elif response == 3:
            name = input('삭제할 이름: ')
            if name in contacts:
                del contacts[name]
                print(f'{name}님의 연락처가 삭제되었습니다.')
            else:
                print('존재하지 않습니다.')
        
        elif response == 4:
            if not contacts:
                print("저장된 정보가 없습니다.")
            else:
                print('=== 전체 연락처 목록 ===')
                for name, phone in contacts.items():
                    print(f'{name}: {phone}')
        elif response == 5:
            print("종료합니다.")
            break    
    
        else:
            print('항목 중에서 선택해주세요')
    
    except ValueError:
        print('숫자를 입력해주세요.')