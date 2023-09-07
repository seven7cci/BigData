# 학번 : 201830135
# 성명 : 최찬일
"""
중간고사

문제) 다음 프로그램의 battle 함수를 파이썬 코드로 작성하시오.

조건1) battle 함수 안쪽 코드만 작성합니다 (다른 코드는 건드리지 않습니다)
조건2) 플레이어는 이상해(bulbasaur), 파이리(charmander), 꼬부기(squirtle) 중 하나를 선택 할 수 있습니다.
      현재 코드에서는 이상해로 지정되어 있습니다.
조건3) 적 포켓몬은 게임 실행 중 초반에 선택할 수 있습니다.
조건4) "공격" 메뉴(1번) 선택 시 플레이어 포켓몬과 적군 포켓몬은 1~10 사이의 데미지 피해를 랜덤으로 입힙니다.
       양쪽 포켓몬 모두 각각의 랜덤 데미지 만큼 체력이 줄어 듭니다.
조건5) "도망" 메뉴(2번) 선택 시 10%의 확률(0.0에서 1.0미만의 난수를 발생하는 random.random() 메서드 사용)로 전투에서 탈출 할 수 있습니다.
       탈출 실패 시 적군 포켓몬으로 부터 1~10사이의 데미지를 입습니다.
조건6) 잘못된 메뉴 선택 시 "유효한 입력이 아닙니다. 다시 시도해주세요." 메시지를 출력합니다.
조건7) 아군 포켓몬의 체력이 0이 되면 기절상태가 됩니다. 적군 포켓몬도 체력이 0이 되면 기절상태가 됩니다.
조건8) 적군 포켓몬 기절 시 아군 포켓몬의 경험치(exp)가 +1 됩니다.
       +2가 되면 아군 포켓몬 경험치는 0으로 리셋 되고 hp는 +10으로 증가합니다.
조건9) 이외 내용은 아래 실행결과를 참고하거나 시험 감독관에게 질문합니다

프로그램 실행 결과)
D:\game\venv\Scripts\python.exe D:/game/PokemonGame.py

적 포켓몬을 고르세요 :
1 피카츄 - 전기 HP: 30
2 푸린 - 노멀/페어리 HP: 35
3 꼬마돌 - 바위/땅 HP: 40
번호 입력 : 2
야생  푸린 이(가) 나타났다!
이상해  돌격!

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 1 점을 적중!
적군 푸린 이(가) 데미지 7 점을 적중!
이상해의 체력 : 63

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 10 점을 적중!
적군 푸린 이(가) 데미지 10 점을 적중!
이상해의 체력 : 53

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 6 점을 적중!
적군 푸린 이(가) 데미지 10 점을 적중!
이상해의 체력 : 43

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 3 점을 적중!
적군 푸린 이(가) 데미지 4 점을 적중!
이상해의 체력 : 39

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 3 점을 적중!
적군 푸린 이(가) 데미지 5 점을 적중!
이상해의 체력 : 34

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 8 점을 적중!
적군 푸린 이(가) 데미지 2 점을 적중!
이상해의 체력 : 32

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 8 점을 적중!
적군 푸린 이(가) 기절함!
이상해 이(가) 경험치 1점 획득!
한 게임 더?
한 판 더할거면 Y 그만할거면 N을 입력 : y

적 포켓몬을 고르세요 :
1 피카츄 - 전기 HP: 30
2 푸린 - 노멀/페어리 HP: -4
3 꼬마돌 - 바위/땅 HP: 40
번호 입력 : 1
야생  피카츄 이(가) 나타났다!
이상해  돌격!

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 7 점을 적중!
적군 피카츄 이(가) 데미지 3 점을 적중!
이상해의 체력 : 29

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 3 점을 적중!
적군 피카츄 이(가) 데미지 2 점을 적중!
이상해의 체력 : 27

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 7 점을 적중!
적군 피카츄 이(가) 데미지 2 점을 적중!
이상해의 체력 : 25

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 2 점을 적중!
적군 피카츄 이(가) 데미지 8 점을 적중!
이상해의 체력 : 17

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 6 점을 적중!
적군 피카츄 이(가) 데미지 2 점을 적중!
이상해의 체력 : 15

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 8 점을 적중!
적군 피카츄 이(가) 기절함!
이상해 이(가) 경험치 1점 획득!
이상해 이(가) 레벨 업!
한 게임 더?
한 판 더할거면 Y 그만할거면 N을 입력 : y

적 포켓몬을 고르세요 :
1 피카츄 - 전기 HP: -3
2 푸린 - 노멀/페어리 HP: -4
3 꼬마돌 - 바위/땅 HP: 40
번호 입력 : 3
야생  꼬마돌 이(가) 나타났다!
이상해  돌격!

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 2
이상해 이(가) 도망을 시도함...
탈출 실패!
적군 꼬마돌 이(가) 데미지 4 점을 적중!
이상해의 체력 : 21

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 2
이상해 이(가) 도망을 시도함...
탈출 실패!
적군 꼬마돌 이(가) 데미지 8 점을 적중!
이상해의 체력 : 13

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 1
이상해 이(가) 데미지 4 점을 적중!
적군 꼬마돌 이(가) 데미지 6 점을 적중!
이상해의 체력 : 7

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 2
이상해 이(가) 도망을 시도함...
탈출 실패!
적군 꼬마돌 이(가) 데미지 2 점을 적중!
이상해의 체력 : 5

 이상해 의 선택은?
1. 공격
2. 도망
번호 입력 : 2
이상해 이(가) 도망을 시도함...
탈출 성공!
한 게임 더?
한 판 더할거면 Y 그만할거면 N을 입력 : n
프로그램을 종료합니다!

Process finished with exit code 0


"""


import random

def battle(func):
    def wrapper(**kwargs):
        player_pokemon = kwargs['player_pokemon']
        enemy_pokemon = kwargs['enemy_pokemon']
        print(f'야생 {enemy_pokemon["name"]}이(가) 나타났다!')
        print(f'{player_pokemon["name"]} 돌격!')

        while True:
            print(f'\n{player_pokemon["name"]}의 선택은?')
            print("1. 공격")
            print("2. 도망")
            choice = input("번호 입력 : ")
            if choice == "1":
                damage = random.randint(1, 10)
                enemy_pokemon["hp"] = enemy_pokemon["hp"] - damage
                print(f'{player_pokemon["name"]} 이(가) 데미지 {damage}를 입혔습니다.')
                if enemy_pokemon["hp"] <= 0:
                    enemy_pokemon["hp"] = 0
                    print(f"적군 {enemy_pokemon['name']} 이(가) 기절함!")
                    print(f"{player_pokemon['name']} 이(가) 경험치 1점 획득")
                    player_pokemon["exp"] = player_pokemon["exp"] + 1
                    return
                damage = random.randint(1, 10)
                player_pokemon["hp"] = player_pokemon["hp"] - damage
                print(f'적군 {enemy_pokemon["name"]} 이(가) 데미지 {damage}를 입힘')
                print(f'{player_pokemon["name"]}의 체력 : {player_pokemon["hp"]}')
                if player_pokemon["hp"] <= 0:
                    player_pokemon["hp"] = 0
                    print(f'{player_pokemon["name"]} 기절함')
                    print("게임 종료")
                    return
            elif choice == "2":
                print(f'{player_pokemon["name"]} 이(가) 도망을 시도함...')
                if random.random() < 0.9:  # 90%의 확률로 탈출 실패
                    print("탈출 실패!")
                    damage = random.randint(1,10)
                    player_pokemon["hp"] = player_pokemon["hp"] - damage
                    print(f'적군 {enemy_pokemon["name"]} 이(가) 데이미 {damage} 점을 적중!')
                    print(f'{player_pokemon["name"]}의 체력 : {player_pokemon["hp"]}')
                    if player_pokemon["hp"] <= 0:
                        player_pokemon["hp"] = 0
                        print(f'{player_pokemon["name"]} 기절함')
                        print("게임 종료")
                        return
                else:  # 10%의 확률로 탈출 성공
                    print("탈출 성공!")
                    return
            else:
                print("휴효한 입력이 아닙니다. 다시 시도해주세요.")

    return wrapper


# 이상해
bulbasaur = {
    "name": "이상해",
    "type": "풀/독",
    "hp": 70,
    "exp": 0
}


# 파이리
charmander = {
    "name": "파이리",
    "type": "불",
    "hp": 40,
    "exp": 0
}


# 꼬부기
squirtle = {
    "name": "꼬부기",
    "type": "물",
    "hp": 45,
    "exp": 0
}


# 적 포켓몬
enemy_pokemon_list = [
    {
        "name": "피카츄",
        "type": "전기",
        "hp": 30
    },
    {
        "name": "푸린",
        "type": "노멀/페어리",
        "hp": 35
    },
    {
        "name": "꼬마돌",
        "type": "바위/땅",
        "hp": 40
    }
]

player_pokemon = bulbasaur  # 플레이어는 이상해, 파이리, 꼬부기 중 선택 가능. 여기선 이상해 선택

while True:
    print("\n적 포켓몬을 고르세요 :")
    for i, enemy_pokemon in enumerate(enemy_pokemon_list):
        print(i+1, enemy_pokemon["name"], "-", enemy_pokemon["type"], "HP:", enemy_pokemon["hp"])
    choice = input("번호 입력 : ")
    try:
        enemy_pokemon = enemy_pokemon_list[int(choice)-1]
    except:
        print("유효하지 않은 입력입니다. 다시 시도하세요")


    @battle
    def fight(player_pokemon, enemy_pokemon):
        pass


    fight(player_pokemon=player_pokemon, enemy_pokemon=enemy_pokemon)

    if player_pokemon["exp"] >= 2:
        print(player_pokemon["name"], "이(가) 레벨 업!")
        player_pokemon["hp"] += 10
        player_pokemon["exp"] = 0

    print("한 게임 더?")
    choice = input("한 판 더할거면 Y 그만할거면 N을 입력 : ")
    if choice.upper() == "N":
        print("프로그램을 종료합니다!")
        break
