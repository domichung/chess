import zone_show
import zone_reset
array = [['空' for _ in range(9)] for _ in range(10)]
zone_reset.initialize_chess_board(array)
zone_show.show_zone(array)