"""
Create simple combination of 3-5 movements on demand
"""
import typer
from typing import Optional, List, Tuple
import random
import kokoro
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play
import os
import time
import json

app = typer.Typer()


MOVES: dict = json.load(open("./data/moves.json", "r"))
MAX_DURATION: int = 30
MAX_DURATION: int = 60*2
REST: int = 60 * 1
kokoro = kokoro.KPipeline(lang_code='a')


@app.command()
def combos() -> Tuple[str, int, int]:
    """ Chooses base combos to execute, repeat for X sec """
    result_combo: str = random.choice(list(MOVES.keys()))
    duration: int = random.randint(MAX_DURATION, MAX_DURATION)
    print(result_combo)
    return result_combo, duration, REST


@app.command()
def pronounce():
    """ Suggest a combo in a voice, hardcoded voice of Bruce Lee. """
    combination, duration, rest = combos()
    text = f"Execute {combination} for {duration} seconds. Rest afterwards for {rest} seconds."
    output_sound = "./data/output.ogg"
    command_sound = kokoro(text, voice='af_alloy', speed=1)
    for i, (gs, ps, audio) in enumerate(command_sound):
        sf.write(output_sound, audio, 24000)
    audio = AudioSegment.from_file(output_sound)
    play(audio)
    os.remove(output_sound)


if __name__ == "__main__":
    app()
