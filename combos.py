""" 
Create simple combination of 3-5 movements on demand
"""
import typer
from typing import Optional, List
import random

app = typer.Typer()

MOVES: List[str] = ["jab", "cross", "hook", "uppercut", "side kick", "front kick", "round kick", "defense", "dive"]
MAX_REPETITION: int = 10
MIN_MOVES: int = 3
MAX_MOVES: int = 6

@app.command()
def combo(int: Optional[int] = 3) -> str:
    """ Randomly combines moves into a combo to execute and how many times. Max 10. Moves are statically provided in json file for now. """
    result_combo: List[str] = []
    
    # attempt 1: random number of moves + random with return choice
    moves: int = random.randint(MIN_MOVES, MAX_MOVES)
    repetition: int = random.randint(1, MAX_REPETITION)
    for i in range(0, moves):
        result_combo.append(random.choice(MOVES))
    res: str = f"Do {', '.join(result_combo)}. {repetition} times!"
    print(res)
    return res




if __name__ == "__main__":
    app()
