from DESERT_ADVENTURES import Map, MapObject, Game

#test_1:
def test_map_size():
    map = Map()
    assert map.width == 13
    assert map.height == 13

#test_2:
def test_player_move():
    mapObject = MapObject ("👆", 6, 6)
    mapObject.move(1, 0)
    assert mapObject.coordinate_x == 7
    assert mapObject.coordinate_y == 6

#test_3:
def test_player_death():
    game = Game()
    game.player.coordinate_x == 6
    game.player.coordinate_y == 6
    game.map.map[6][6] = "🐫"
    game.death_screen()

#test_4:
def test_spawn_exit():
    game = Game()
    game.add_exit()
    assert game.map.map[game.exit.coordinate_y][game.exit.coordinate_x] == "🕌"
