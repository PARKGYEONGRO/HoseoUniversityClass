# 회원가입 유효성 검사기

# 상황: 회원가입 폼에서 입력값이 형식에 맞는지 검사하고 싶다.

# 요구사항 — 아래 항목을 입력받아 형식 검사(문자열 메서드 또는 정규식)

# 아이디: 영문/숫자만, 4자 이상 (isalnum, len)
# 비밀번호: 8자 이상, 숫자 1개 이상 포함 (re.search(r"\d", pw))
# 이메일: @ 와 . 포함 형식 (re.match(r"^[\w.]+@[\w]+\.[a-z]+$", ...))
# 전화번호: 010-XXXX-XXXX 형식 (re.match(r"^010-\d{4}-\d{4}$", ...))
# 각 항목별 ✅/❌ 와 안내 메시지 출력
# 출력 예:
# 아이디: ✅ 사용 가능
# 비밀번호: ❌ 숫자를 포함해야 합니다
# 이메일: ✅ 올바른 형식
# 전화번호: ❌ 010-1234-5678 형식이어야 합니다
# 힌트: 항목마다 함수로 분리하면 깔끔 (check_email(email) 등)

import re

def check_id(user_id):
    if len(user_id) >= 4 and user_id.isalnum():
        return True, "✅ 사용 가능"
    return False, "❌ 영문/숫자 조합으로 4자 이상이어야 합니다."

def check_password(user_pw):
    if len(user_pw) >= 8 and re.search(r'\d', user_pw):
        return True, "✅ 사용 가능"
    return False, "❌ 8자 이상이며 숫자를 최소 1개 이상 포함해야 합니다."

def check_email(user_email):
    if re.match(r"^[\w.]+@[\w]+\.[a-z]$", user_email):
        return True, "✅ 올바른 형식"
    return False, "❌ 올바른 이메일 형식(@와 . 포함)이 아닙니다."

def check_phone(user_phone):
    if re.match(r'^010-\d{4}-\d{4}$',user_phone):
        return True, "✅ 올바른 형식"
    return False, "❌ 010-1234-5678 형식이어야 합니다."

def validate_registration(user_id, user_pw, user_email, user_phone):
    _, id_msg = check_id(user_id)
    _, pw_msg = check_password(user_pw)
    _, email_msg = check_email(user_email)
    _, phone_msg = check_phone(user_phone)
    
    print(f"아이디: {id_msg}")
    print(f"비밀번호: {pw_msg}")
    print(f"이메일: {email_msg}")
    print(f"전화번호: {phone_msg}")

validate_registration(
    user_id='test1234',
    user_pw='abcdefg',
    user_email='user@test.com',
    user_phone='01012345678'
)