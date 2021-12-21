import numpy as np
import pickle

#Game set
Win_streak = 5  # 3 for Tic-tac-toe Games and 5 for Gomoku Games
Board_size = 15  # 3 for Tic-tac-toe Games and 15 (or 19) for Gomoku Games

p1 = Player("p1")
p2 = Player("p2")

st = State(p1, p2)
st.play(5000)

p1.savePolicy()
p2.savePolicy()