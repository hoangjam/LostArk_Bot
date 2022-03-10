# James Hoang
import subprocess


# launch game
def game_launch():
    # steam://rungameid/1599340
    subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 1599340")


if __name__ == '__main__':
    game_launch()
