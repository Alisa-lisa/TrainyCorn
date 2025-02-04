"""
Create simple combination of 3-5 movements on demand
"""
import typer
from typing import Optional, List
import random
import kokoro
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play
import os
import time


app = typer.Typer()


MOVES: List[str] = ["jab", "cross", "hook", "uppercut", "side kick", "front kick", "roundhouse kick", "dive"]
MAX_REPETITION: int = 10
MIN_MOVES: int = 3
MAX_MOVES: int = 3
kokoro = kokoro.KPipeline(lang_code='a')


@app.command()
def combo(moves: Optional[int] = 3) -> str:
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


@app.command()
def pronounce(moves: Optional[int] = 3):
    """ Suggest a combo in a voice, hardcoded voice of Bruce Lee. """
    text = combo(moves)
    output_sound = "./data/output.ogg"
    command_sound = kokoro(text, voice='af_alloy', speed=1)
    for i, (gs, ps, audio) in enumerate(command_sound):
        sf.write(output_sound, audio, 24000)
    audio = AudioSegment.from_file(output_sound)
    play(audio)
    time.sleep(2)
    play(audio)
    os.remove(output_sound)


if __name__ == "__main__":
    app()
