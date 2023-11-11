import random

def generate_random_number():
    """
    0부터 9까지 서로 다른 세 숫자로 이루어진 랜덤한 숫자를 생성합니다.
    """
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers[:3]

def user_input():
    """
    사용자로부터 0부터 9까지 서로 다른 세 숫자를 입력받습니다.
    """
    while True:
        try:
            user_guess = list(map(int, input("세 자리 숫자를 입력하세요 (0-9 사이의 서로 다른 숫자): ")))
            if len(user_guess) != 3 or any(x < 0 or x > 9 for x in user_guess) or len(set(user_guess)) != 3:
                raise ValueError
            return user_guess
        except ValueError:
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")

def check_guess(target, guess):
    """
    추측한 숫자와 정답을 비교하여 S, B, O를 반환합니다.
    """
    strikes = sum(x == y for x, y in zip(target, guess))
    balls = sum(x in guess for x in target) - strikes
    outs = 3 - (strikes + balls)
    return strikes, balls, outs

def baseball_game():
    """
    야구 게임을 실행합니다.
    """
    target_number = generate_random_number()
    attempts = 0

    while attempts < 10:
        attempts += 1
        user_guess = user_input()
        strikes, balls, outs = check_guess(target_number, user_guess)

        print(f"시도 횟수: {attempts} - S:{strikes}, B:{balls}, O:{outs}")

        if strikes == 3:
            print("축하합니다! 정답을 맞췄습니다.")
            break

    if strikes != 3:
        print("10회의 기회를 모두 사용했습니다. 게임 오버. 정답은", target_number)

if __name__ == "__main__":
    baseball_game()
