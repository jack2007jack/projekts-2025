import random
import sys
import tty
import termios

PLAYER_SYMBOL = '👆'
EMPTY_SYMBOL = ' \033[90m∘\033[0m'
FENCE_SYMBOL = '🔳'
EXIT_SYMBOL = '🕌'
MONSTER_SYMBOL = '🐫'
BARRIER_SYMBOL = '  '
SHELTER_SYMBOL = '🌵'
INTRO_SYMBOL = '🐪'
OVER_SYMBOL = '❌'
WIN_SYMBOL = '💎'

# funkcija, lai neievadītu Enter:
def getch():
    fd = sys.stdin.fileno()
    g = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        button = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, g)
    return button

class Map:
    def __init__(self):
        self.width = 13
        self.height = 13
        self.map = []
        self.init_map()

    def init_map(self):
        self.map = [None] * self.height

# kartes robežas un iekšējās struktūras:
        for w in range(self.height):
            if w == 0 or w == 12:
                self.map[w] = ([FENCE_SYMBOL] * 5) + ([BARRIER_SYMBOL] * 3) + ([FENCE_SYMBOL] * 5)
# koridori un nojumes:
            elif w == 1 or w == 11:
                self.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 3) + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 3) + [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 3) + [FENCE_SYMBOL]
# koridori un nojumes:
            elif w == 2 or w == 10:
                self.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] + [SHELTER_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL] * 5 + ([EMPTY_SYMBOL] + [SHELTER_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL]
# koridori un nojumes:
            elif w == 4 or w == 8:
                self.map[w] = [FENCE_SYMBOL] * 2 + ([EMPTY_SYMBOL] + [SHELTER_SYMBOL] + [EMPTY_SYMBOL]) + ([SHELTER_SYMBOL] + [SHELTER_SYMBOL] + [SHELTER_SYMBOL]) + ([EMPTY_SYMBOL] + [SHELTER_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL] * 2
# koridori un nojumes:
            elif w == 5:
                self.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# koridori un nojumes:
            elif w == 6:
                self.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + [EMPTY_SYMBOL] + [SHELTER_SYMBOL] + [SHELTER_SYMBOL] + ([EMPTY_SYMBOL] * 3) + [SHELTER_SYMBOL] + [SHELTER_SYMBOL] + [EMPTY_SYMBOL] + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# koridori un nojumes:
            elif w == 7:
                self.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# kartes atlikuma papildināšana:
            else:
                self.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 11) + [FENCE_SYMBOL]

    def draw(self, player):
# kartes zīmēšana ar spēlētāja atrašanās vietu:
        for height in range(self.height):
            for width in range(self.width):
# spēlētāja izvades pārbaude:
                if player.coordinate_x == width and player.coordinate_y == height:
                    print(player.symbol, end="")
                else:
                    print(self.map[height][width], end="")
            print()

class MapObject:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.coordinate_x = x
        self.coordinate_y = y

    def move(self, move_x, move_y):
        self.coordinate_x += move_x
        self.coordinate_y += move_y

class Game:
    def __init__(self):
        self.player = MapObject(PLAYER_SYMBOL, 6, 6)
        self.map = Map()
        self.monster_amount = 20
        self.add_monster()
        self.moves_number = 0
        self.exit = MapObject(EXIT_SYMBOL, 6, 6)
        self.exit_spawn = random.randint(15, 25)



    def add_exit(self):
        self.map.map[self.exit.coordinate_y][self.exit.coordinate_x] = self.exit.symbol


    def add_monster(self):
# monstru radīšana un izvietošana:
        self.monsters = []
        min_distance = 8
        for _ in range(self.monster_amount):
            while True:
# nejauša monstru nārsta vieta:
                monster_x = random.randint(1, self.map.width - 2)
                monster_y = random.randint(1, self.map.height - 2)
# pārbaudiet, vai noteiktā attālumā no spēlētāja parādās briesmonis:
                if (self.map.map[monster_y][monster_x] == EMPTY_SYMBOL and abs(self.player.coordinate_x - monster_x) + abs(self.player.coordinate_y - monster_y) >= min_distance):
                    monster = MapObject(MONSTER_SYMBOL, monster_x, monster_y)
                    self.monsters.append(monster)
                    self.map.map[monster_y][monster_x] = MONSTER_SYMBOL
                    break

    def intro_screen(self):
# sveiciena un instrukciju ekrāns:
        for w in range(self.map.width):
# zīmēšanas ekrāna dizains:
            if w == 0 or w == 12:
                self.map.map[w] = ([FENCE_SYMBOL] * 5) + ([BARRIER_SYMBOL] * 3) + ([FENCE_SYMBOL] * 5)
# zīmēšanas ekrāna dizains:
            elif w == 1 or w == 11:
                self.map.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 3) + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 3) + [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 3) + [FENCE_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 2 or w == 10:
                self.map.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] + [INTRO_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL] * 5 + ([EMPTY_SYMBOL] + [INTRO_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 4 or w == 8:
                self.map.map[w] = [FENCE_SYMBOL] * 2 + ([EMPTY_SYMBOL] + [EMPTY_SYMBOL] + [EMPTY_SYMBOL]) + ([EMPTY_SYMBOL] + [EMPTY_SYMBOL] + [EMPTY_SYMBOL]) + ([EMPTY_SYMBOL] + [EMPTY_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL] * 2
# zīmēšanas ekrāna dizains:
            elif w == 5:
                self.map.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 6:
                self.map.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 7:
                self.map.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# zīmēšanas ekrāna dizains:
            else:
                self.map.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 11) + [FENCE_SYMBOL]
# izvades instrukcijas ekrānā:
        for y in range(self.map.height):
            for x in range(self.map.width):
# izvades nosaukums un norādes:
                if y == 5 and x == 2:
                    print("","\033[93mDESERT ADVENTURES\033[0m", end="")
                    print(FENCE_SYMBOL, end="")
                    break
# instrukcija:
                elif y == 6 and x == 3:
                    print(" \033[92m!MOVE TO WIN!\033[0m", end="")
                    print(" " * 2 + FENCE_SYMBOL, end="")
                    break
# padoms:
                elif y == 7 and x == 3:
                    print(" \033[93m(press enter)\033[0m", end="")
                    print(" " * 2 + FENCE_SYMBOL, end="")
                    break
# kartes izvade:
                else:
                    print(self.map.map[y][x], end="")
            print()

        input()
        self.add_monster()
        self.__init__()

    def death_screen(self):
# zaudējumu ekrāns:
        for w in range(self.map.width):
# zīmēšanas ekrāna dizains:
            if w == 0 or w == 12:
                self.map.map[w] = ([FENCE_SYMBOL] * 5) + ([BARRIER_SYMBOL] * 3) + ([FENCE_SYMBOL] * 5)
# zīmēšanas ekrāna dizains:
            elif w == 1 or w == 11:
                self.map.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 3) + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 3) + [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 3) + [FENCE_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 2 or w == 10:
                self.map.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] + [OVER_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL] * 5 + ([EMPTY_SYMBOL] + [OVER_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 4 or w == 8:
                self.map.map[w] = [FENCE_SYMBOL] * 2 + ([EMPTY_SYMBOL] + [EMPTY_SYMBOL] + [EMPTY_SYMBOL]) + ([EMPTY_SYMBOL] + [EMPTY_SYMBOL] + [EMPTY_SYMBOL]) + ([EMPTY_SYMBOL] + [EMPTY_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL] * 2
# zīmēšanas ekrāna dizains:
            elif w == 5:
                self.map.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 6:
                self.map.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 7:
                self.map.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# zīmēšanas ekrāna dizains:
            else:
                self.map.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 11) + [FENCE_SYMBOL]
# zaudējuma ziņojuma rādīšana:
        for y in range(self.map.height):
            for x in range(self.map.width):
# spēles beigu ziņojums:
                if y == 5 and x == 2:
                    print(" " * 4,"\033[90mGAME OVER\033[0m", end="")
                    print(" " * 4 + FENCE_SYMBOL, end="")
                    break
# konta izņemšana:
                elif y == 6 and x == 3:
                    print(" ","SCORE :", str(self.moves_number).zfill(2), end="")
                    print(" " * 4 + FENCE_SYMBOL, end="")
                    break
# padoms:
                elif y == 7 and x == 3:
                    print(" \033[90m(press enter)\033[0m", end="")
                    print(" " * 2 + FENCE_SYMBOL, end="")
                    break
# kartes izvade:
                else:
                    print(self.map.map[y][x], end="")
            print()

        input()
        self.intro_screen()

    def win_screen(self):
# uzvaras ekrāns:
        for w in range(self.map.width):
# zīmēšanas ekrāna dizains:
            if w == 0 or w == 12:
                self.map.map[w] = ([FENCE_SYMBOL] * 5) + ([BARRIER_SYMBOL] * 3) + ([FENCE_SYMBOL] * 5)
# zīmēšanas ekrāna dizains:
            elif w == 1 or w == 11:
                self.map.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 3) + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 3) + [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 3) + [FENCE_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 2 or w == 10:
                self.map.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] + [WIN_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL] * 5 + ([EMPTY_SYMBOL] + [WIN_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 4 or w == 8:
                self.map.map[w] = [FENCE_SYMBOL] * 2 + ([EMPTY_SYMBOL] + [EMPTY_SYMBOL] + [EMPTY_SYMBOL]) + ([EMPTY_SYMBOL] + [EMPTY_SYMBOL] + [EMPTY_SYMBOL]) + ([EMPTY_SYMBOL] + [EMPTY_SYMBOL] + [EMPTY_SYMBOL]) + [FENCE_SYMBOL] * 2
# zīmēšanas ekrāna dizains:
            elif w == 5:
                self.map.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 6:
                self.map.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# zīmēšanas ekrāna dizains:
            elif w == 7:
                self.map.map[w] = [BARRIER_SYMBOL] + [FENCE_SYMBOL] + ([BARRIER_SYMBOL] * 9) + [FENCE_SYMBOL] + [BARRIER_SYMBOL]
# zīmēšanas ekrāna dizains:
            else:
                self.map.map[w] = [FENCE_SYMBOL] + ([EMPTY_SYMBOL] * 11) + [FENCE_SYMBOL]
# izvades uzvaras ziņojums:
        for y in range(self.map.height):
            for x in range(self.map.width):
# uzvaras vēstījums:
                if y == 5 and x == 2:
                    print(" " * 4,"\033[94m!VICTORY!\033[0m", end="")
                    print(" " * 4 + FENCE_SYMBOL, end="")
                    break
# konta izņemšana:
                elif y == 6 and x == 3:
                    print(" ","SCORE :", str(self.moves_number).zfill(2), end="")
                    print(" " * 4 + FENCE_SYMBOL, end="")
                    break
# padoms:
                elif y == 7 and x == 3:
                    print(" \033[94m(press enter)\033[0m", end="")
                    print(" " * 2 + FENCE_SYMBOL, end="")
                    break
# kartes izvade:
                else:
                    print(self.map.map[y][x], end="")
            print()

        input()
        self.intro_screen()

    def game_loop(self):

        self.intro_screen()
# Bezgalīga cilpa, lai spēle darbotos mūžīgi:
        while True:
            self.map.draw(self.player)
            print("\033[96m★ ★ ★ ★ ★\033[0m", str(self.moves_number).zfill(2),"/", self.exit_spawn, "\033[96m★ ★ ★ ★ ★\033[0m")
# monstru pārvietošanās iespējas:
            for monster in self.monsters:
                move_monster = [(1,0), (0,-1), (1,0), (-1,0)]
                random.shuffle(move_monster)
# kustības iespēju sajaukšana:
                for x, y in move_monster:
                    monster_coordinate_x = monster.coordinate_x + x
                    monster_coordinate_y = monster.coordinate_y + y
# jauna monstru pozīcija:
                    if 1 <= monster_coordinate_x < self.map.width - 1 and 1 <= monster_coordinate_y < self.map.height - 1:
                        new_step = self.map.map[monster_coordinate_y][monster_coordinate_x]
# pārbaudīt atļautās kustības:
                        if new_step == EMPTY_SYMBOL or new_step == MONSTER_SYMBOL or new_step == SHELTER_SYMBOL:
                            if self.map.map[monster.coordinate_y][monster.coordinate_x] == MONSTER_SYMBOL:
                                if self.map.map[monster.coordinate_y][monster.coordinate_x] != SHELTER_SYMBOL:
                                    self.map.map[monster.coordinate_y][monster.coordinate_x] = EMPTY_SYMBOL
                            monster.move(x, y)
# monstru kustība:
                            if self.map.map[monster_coordinate_y][monster_coordinate_x] != SHELTER_SYMBOL:
                                self.map.map[monster_coordinate_y][monster_coordinate_x] = MONSTER_SYMBOL
                            break

            self.check_input()
            self.moves_number += 1
# palielināt kustību skaitītāju:
            if self.moves_number == self.exit_spawn:
                self.add_exit()
            map_symbol = self.map.map[self.player.coordinate_y][self.player.coordinate_x]

# uzvaras nosacījumi:
            if map_symbol == EXIT_SYMBOL:
                self.win_screen()
                self.map.draw(self.player)
# zaudējuma apstākļi:
            elif self.map.map[self.player.coordinate_y][self.player.coordinate_x] in [FENCE_SYMBOL, SHELTER_SYMBOL, MONSTER_SYMBOL]:
                self.death_screen()
                self.map.draw(self.player)


    def check_input(self):
        print(flush=True)
        button = getch()
# pārbaudiet spēlētāja ievadīto rakstzīmi - uz augšu:
        if button.lower() == "w":
            self.player.move(0, -1)
            self.player.symbol = "👆"
# pārbaudiet spēlētāja ievadīto rakstzīmi - uz leju:
        elif button.lower() == "s":
            self.player.move(0, 1)
            self.player.symbol = "👇"
# pārbaudiet spēlētāja ievadīto rakstzīmi - pa kreisi:
        elif button.lower() == "a":
            self.player.move(-1, 0)
            self.player.symbol = "👈"
# pārbaudiet spēlētāja ievadīto rakstzīmi - pa labi:
        elif button.lower() == "d":
            self.player.move(1, 0)
            self.player.symbol = "👉"
# jebkura cita ievade:
        else:
           self.death_screen()
           self.map.draw(self.player)

game = Game()
game.game_loop()

