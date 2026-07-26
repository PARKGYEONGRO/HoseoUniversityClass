# 나만의 클래스 설계·구현

# 상황: 내가 관심 있는 사물을 클래스로 만들어보자.

# 요구사항 — 자유 주제로 클래스 1개 설계·구현

# 속성 3개 이상 (그 사물이 가진 데이터)
# 메서드 2개 이상 (그 사물이 할 수 있는 일, 1개는 상태 변경)
# 인스턴스 2개 이상 만들어 동작 시연
# __str__ 으로 보기 좋게 출력
# 예시 주제: 게임 캐릭터, 스마트폰, 카페 주문, 반려동물, 자동차

""" 차량 공유 서비스의 자동차 클래스 설계 및 구현
설계 목적
    상태 관리의 무결성 검증 (Encapsulation): 차량의 대여 가능 여부, 연료 잔량 등 실시간으로 변하는 비즈니스 데이터를
    외부의 잘못된 직접 접근으로부터 보호하기 위해 더블 언더스코어(__)를 활용하여 강력하게 캡슐화합니다.
    외부 레이어는 오직 안전하게 제한된 인터페이스(Getter/@property)를 통해서만 데이터를 조회할 수 있습니다.

    현실적인 비즈니스 로직 구현 (Domain Logic): "연료가 10% 이하이면 대여할 수 없음", "이미 대여 중인 차는 중복 대여 불가능",
    "주행 시 연료가 소모되며, 연료 고갈 시 정비 필요 상태로 전환" 등 현실 세계의 제약 조건을 도메인 규칙으로 코딩합니다.

    관심사의 분리 (Separation of Concerns): 핵심 비즈니스 로직을 담당하는 자동차 객체(Domain)와 사용자의 입출력을 처리하는 콘솔 시스템(Presentation)을 철저히 분리하여 결합도를 낮추고 유연성을 확보합니다.

요구사항 정의
    속성 (Attributes) — 캡슐화 적용
    car_name (문자형): 차량 모델명 (예: "ELANTRA_N")
    car_number (문자형): 차량 번호 (예: "123가 4567")
    __fuel (정수형, 0~100%): 외부 변경이 차단된 차량의 연료 잔량
    __status (문자형): 외부 변경이 차단된 차량의 현재 상태 (AVAILABLE, RENTED, NEEDS_REPAIR)

    메서드 (Methods)
    rent(): [상태 변경] 차량 대여 상태를 전환합니다. 이미 대여 중이거나 연료가 10% 이하일 경우, 성공 여부를 리턴하는 대신 명확한 커스텀 예외(Custom Exception)를 던집니다.
    drive(distance): [상태 변경] 차량을 주행시킵니다. 주행 거리에 비례하여 연료를 차감하며, 주행 중 연료가 0 이하로 떨어지면 연료 고갈 예외를 던지고 상태를 NEEDS_REPAIR로 강제 변경합니다.
    __str__(): 인스턴스의 현재 상태를 가독성 높은 문자열 포맷으로 반환합니다.

    필요 모듈 (Standard Modules)
    time: 주행 시 현실감을 주기 위한 시간 지연 시뮬레이션(time.sleep)에 사용합니다.
    datetime: 대여 및 이벤트 발생 시점의 정확한 타임스탬프 기록을 위한 확장성을 위해 포함합니다.
    random: 초기 차량 생성 시 실감 나는 테스트 환경 조성을 위해 연료 잔량을 임의 지정(rd.randint)하는 데 사용합니다.

출력 결과
    === 1. 차량 생성 및 초기 상태 확인 ===
    [123가 4567] 상태: AVAILABLE | 연료: 80%
    [99나 9999] 상태: AVAILABLE | 연료: 8%

    === 2. 정상 차량 대여 및 주행 테스트 ===
    123가 4567 차량 대여를 시작합니다.
    [123가 4567] 상태: RENTED | 연료: 80%

    [123가 4567] 50km 주행을 시작합니다. (연료 25% 소모)
    주행 완료 후 차량 상태:
    [123가 4567] 상태: RENTED | 연료: 55%

    === 3. 예외 상황 테스트 1: 연료 부족 차량 대여 시도 ===
    [99나 9999] 대여 실패: 연료가 부족합니다. (현재 연료: 8%)

    === 4. 예외 상황 테스트 2: 이미 대여 중인 차량 대여 시도 ===
    [123가 4567] 대여 실패: 이미 대여 중인 차량입니다.

    === 5. 예외 상황 테스트 3: 주행 중 연료 고갈 상황 ===
    [123가 4567] 150km 주행을 시작합니다. (연료 75% 필요)
    경고: 주행 중 연료가 고갈되었습니다! 운행을 강제 종료합니다.
    [123가 4567] 상태: NEEDS_REPAIR | 연료: 0%
"""
from datetime import datetime
import random as rd
import time


class CarSharingException(Exception):
    """호서카 서비스 기본 예외 클래스"""
    pass

class VehicleNotAvailableException(CarSharingException):
    """차량이 대여 가능한 상태가 아닐 때 발생"""
    pass

class InsufficientFuelException(CarSharingException):
    """연료가 부족할 때 발생"""
    pass


class Sharecar:
    FUEL_CONSUMPTION_PER_KM = 0.5
    MIN_FUEL_FOR_RENTAL = 10

    def __init__(self, car_name: str, car_number: str, status: str = "AVAILABLE"):
        self.car_name = car_name
        self.car_number = car_number
        self.__fuel = rd.randint(5, 100)
        self.__status = status

    @property
    def fuel(self) -> int:
        return self.__fuel

    @property
    def status(self) -> str:
        return self.__status

    def __str__(self) -> str:
        return f"{self.car_name} - [{self.car_number}] 상태: {self.__status} | 연료: {self.__fuel}%"

    def rent(self) -> None:
        """차량 대여 비즈니스 로직 (성공 여부를 True/False가 아닌 예외로 던짐)"""
        if self.__status == "RENTED":
            raise VehicleNotAvailableException(f"이미 대여 중인 차량입니다.")
        
        if self.__fuel <= self.MIN_FUEL_FOR_RENTAL:
            raise InsufficientFuelException(f"연료가 부족합니다. (현재 연료: {self.__fuel}%)")
        
        if self.__status == "AVAILABLE":
            self.__status = "RENTED"

    def drive(self, distance: float) -> None:
        """차량 주행 비즈니스 로직"""
        if self.__status != "RENTED":
            raise VehicleNotAvailableException("먼저 차량을 대여해야 합니다.")

        fuel_consumed = int(distance * self.FUEL_CONSUMPTION_PER_KM)
        self.__fuel -= fuel_consumed

        if self.__fuel <= 0:
            self.__fuel = 0
            self.__status = "NEEDS_REPAIR"
            raise InsufficientFuelException("주행 중 연료가 고갈되어 차량이 강제 정지 및 정비 상태로 전환되었습니다.")


class SharecarConsoleApp:
    def __init__(self, cars: list[Sharecar]):
        self.cars = cars

    def run(self):
        while True:
            print("\n" + "=" * 25)
            choice = input("=== 호서카 메뉴 ===\n1. 차량 렌트 및 주행\n2. 종료\n입력: ")

            if choice == "2":
                print("호서카 서비스를 종료합니다. 이용해 주셔서 감사합니다!")
                break
            elif choice == "1":
                self._manage_rental_flow()
            else:
                print("오류: 1 또는 2를 입력해주세요.")

    def _manage_rental_flow(self):
        """차량 조회부터 대여, 주행까지의 흐름을 제어하는 프레젠테이션 로직"""
        print("\n=== 호서카 차량 조회 ===")
        for idx, car in enumerate(self.cars):
            print(f"{idx + 1}. {car}")

        try:
            car_idx = int(input(f"원하시는 렌트카 번호(1~{len(self.cars)}) 입력: ")) - 1
            if not (0 <= car_idx < len(self.cars)):
                raise ValueError
        except ValueError:
            print(f"오류: 1부터 {len(self.cars)} 사이의 올바른 숫자를 입력해주세요.")
            return

        selected_car = self.cars[car_idx]

        try:
            selected_car.rent()
            print(f"\n🚗 [{selected_car.car_number}] 차량 대여를 시작합니다.")
            print(f"-> {selected_car}\n" + "-" * 25)

            distance = float(input("주행할 거리(km)를 입력하세요: "))
            if distance <= 0:
                print("오류: 주행 거리는 0보다 커야 합니다.")
                return

            print(f"\n🛣️ [{selected_car.car_number}] {distance}km 주행을 시작합니다...")
            time.sleep(0.5)
            
            selected_car.drive(distance)
            print(f"주행 완료! -> {selected_car}")

        except (VehicleNotAvailableException, InsufficientFuelException) as e:
            print(f"서비스 제한 안내: {e}")
        except ValueError:
            print("오류: 거리는 올바른 숫자로 입력해야 합니다.")


if __name__ == "__main__":
    car_list = [
        Sharecar("ELANTRA_N", "123하 4567"),
        Sharecar("CARNIVAL", "124허 5678"),
    ]
    
    app = SharecarConsoleApp(car_list)
    app.run()