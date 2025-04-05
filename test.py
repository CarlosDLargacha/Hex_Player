from board import HexBoard
from player import AIPlayer

def test_hex_game():
    board = HexBoard(10)
    player2 = AIPlayer(2, 2)
    player1 = AIPlayer(1, 2)
    
    current_player = 1
    players = {1: player1, 2: player2}
    
    print("=== INICIO DEL JUEGO ===")
    board.print_board()
    
    while True:
        try:
            print(f"\nTurno Jugador {current_player}")
            move = players[current_player].play(board)
            print(f"Juega en: {move}")
            
            if move not in board.get_possible_moves():
                raise ValueError(f"Movimiento inválido: {move}")
            
            board.place_piece(*move, current_player)
            board.print_board()
            
            if board.check_connection(current_player):
                print(f"\n¡Jugador {current_player} gana!")
                break
                
            current_player = 3 - current_player
            
            if not board.get_possible_moves():
                print("\n¡Empate!")
                break
                
        except ValueError as e:
            print(f"Error: {e}")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            break

if __name__ == "__main__":
    test_hex_game()