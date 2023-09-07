try:
    fahrenheit = float(input("화씨 온도 입력 : "))
    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
    print(f"화씨 {fahrenheit}도는 섭씨 {celsius:.3f}도 입니다.")

    numbers = [3, 1, 99]
    # print(numbers[4])  # exeption
    # print(numbers[0] / 0)  #exeption
    print(numbers[2] / 3)

    # raise "예외를 강제로 던집니다."
    raise Exception("내가 던지는 예외")  # throw

except ValueError as err:
    print(err)
    print("입력 값을 확인하세요. 입력 값은 수치형이어야 합니다.")
except IndexError as err:
    print(err)
    print("인덱스의 범위를 확인하세요")
except ZeroDivisionError as err:
    print(err)
    print("분모에 0이 올 수 없습니다")
except Exception as other:
    print(other)
    print("에러 발생")

a = int(input("..."))