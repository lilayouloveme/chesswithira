import chess

b = chess.Board()
[print(b) or b.push_san(input("Move: ")) for _ in iter(int, 1)]
