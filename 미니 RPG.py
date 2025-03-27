import random

def mini_rpg():
    print("===== 간단한 텍스트 기반 RPG 게임 =====")
    print("악당을 물리치고 승리를 쟁취하세요!\n")

    # 플레이어와 적의 초기 상태 설정
    player = {"name": "플레이어", "health": 100, "attack": 20, "potion": 3}
    enemy = {"name": "악당", "health": 80, "attack": 15}

    while True:
        # 상태 출력
        print(f"\n[상태] {player['name']} 체력: {player['health']} | 물약: {player['potion']}개")
        print(f"[적 정보] {enemy['name']} 체력: {enemy['health']}\n")

        # 사용자 행동 선택
        print("1. 공격하기")
        print("2. 물약 사용하기")
        print("3. 도망가기")
        
        choice = input("무엇을 하시겠습니까? (1, 2, 3): ")

        if choice == "1":
            # 플레이어가 적을 공격
            damage = random.randint(10, player['attack'])
            enemy['health'] -= damage
            print(f"\n{player['name']}이(가) {enemy['name']}에게 {damage}의 데미지를 입혔습니다!")

            if enemy['health'] <= 0:
                print(f"\n{enemy['name']}을 물리쳤습니다! 승리하셨습니다!")
                break
            
            # 적이 반격
            damage = random.randint(5, enemy['attack'])
            player['health'] -= damage
            print(f"{enemy['name']}이(가) {player['name']}에게 {damage}의 데미지를 입혔습니다!")
            
            if player['health'] <= 0:
                print("\n당신이 쓰러졌습니다... 게임 오버!")
                break
        
        elif choice == "2":
            # 물약 사용
            if player['potion'] > 0:
                heal = random.randint(15, 40)
                player['health'] += heal
                player['potion'] -= 1
                print(f"\n{player['name']}이(가) 물약을 사용해 체력을 {heal} 회복했습니다!")
            else:
                print("\n더 이상 사용할 물약이 없습니다!")
                
        elif choice == "3":
            # 도망가기
            print("\n용감한 선택이 아니지만, 당신은 도망쳤습니다!")
            break
        
        else:
            # 잘못된 입력 처리
            print("\n잘못된 입력입니다. 다시 선택해주세요.")
        
        # 게임 진행 중 상태 확인
        if player['health'] > 0 and enemy['health'] > 0:
            continue
        elif player['health'] <= 0:
            print("\n당신은 패배했습니다... 게임 오버!")
            break
        elif enemy['health'] <= 0:
            print("\n적을 물리쳤습니다! 당신의 승리입니다!")
            break

# 게임 실행
mini_rpg()