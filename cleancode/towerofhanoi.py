"""
cleancode.towerofhanoi의 Docstring
"""
import copy
import sys

TOTAL_DISKS = 5 #원판 수 

SOLVED_TOWER = list(range(TOTAL_DISKS, 0 , -1))

def main():
    """execute the Tower of Hanoi solution"""
    print("""hanoi tower problem solution""")
    """tower dictionary key "A", "B", "C"와 탑에 쌓인 원판을 표현하는 리스트
    형태의 값을 갖고 있다. 리스트는 다양한 크기의 원판을 표현하는 정수를 포함하며, 
    리스트의 시작은 탑의 가장아래 바닥이다. 원판 다섯개로 시작하는 게임의 경우에는
    리스트 [5,4,3,2,1]가 완성된 탑을 표현한다. 
    리스트 []는 탑에 쌓인 원판이 없을을 나ㅏ타낸다. 리스트 [1,3] 은 작은 원판 위에 
    큰 원판이 있으며, 유효하지 않은 구성이다. 리스트 [3, 1]이 허용되는 이유는
    작은 원판이 큰 원판 상단에 올라갈 수 있기 때문이다. """
    towers = { "A": copy.copy(SOLVED_TOWER), "B": [], "C": [] }
    while True:
        #탑과 원판을 표시한다
        displayTowers(towers)
        #사용자에게 이동 명령을 요청한다. 
        fromTower, toTower = getPlayerMove(towers)

        #맨 위 원판을 fromTower에서 toTower로 이동한다. 
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        #check complete
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers)
            print("축하합니다! 게임을 완료했습니다.")
            sys.exit()

def getPlayerMove(towers):
    """플레이어에게 이동 명령을 요청한다. (fromTower, toTower)를 반환한다."""
    while True:
        print('탑의 "시작"과 "끝"의 글자 또는 QUIT를 입력하세요.')
        print("(예: 탑 A에서 탑 B로 원판을 이동하려면 AB를 입력합니다.)")
        print()
        response = input("> ").upper().strip()
        if response == "QUIT":
            print("게임을 종료합니다.")
            sys.exit()
        #사용자가 유효한 탑 문자를 입력했는지 확인한다. 
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue
        #더 설명적인 변수 이름을 사용
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            #from 탑은 비어 있을 수 없다. 
            print("원판이 없는 탑을 선택했습니다.")
            continue #플레이어에게 이동 명령을 다시 요청 
        elif len(towers[toTower]) ==0:
            #어떤 원판이라도 빈 to탑으로 이동 가능 
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("더 작은 원판에 더큰 원판을 올릴 수 없습니다.")
            continue #플레이어에게 이동 명령을 다시 요청
        else:
            #유효한 움직임므로 선택된 탑을 반환한다. 
            return fromTower, toTower
        
def displayTowers(towers):
    """세 탑에 배치된 원판을 표시한다."""
    for level in range(TOTAL_DISKS, -1, -1 ):
        for tower in (towers["A"], towers["B"], towers["C"]):
            #탑의 현재 레벨에 원판이 있는지 확인한다
            if level >= len(tower):
                displayDisk(0) #원판이 없으면 빈 공간을 표시한다
            else:
                displayDisk(tower[level]) #원판을 표시한다
        print() #한 레벨을 모두 표시했으면 줄바꿈한다
    emptySpace = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(emptySpace))

def displayDisk(width):
    """주어진 witdh로 원판을 표시한다. width가 0이면 원판이 없을을 의미한다."""
    emptySpace = " " * (TOTAL_DISKS - width)
    if width == 0:
        #원판이 없는 기둥을 표시한다. 
        print(f"{emptySpace}||{emptySpace}", end="")
    else:
        #원판을 표시한다.
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")

if __name__ == "__main__":
    main()