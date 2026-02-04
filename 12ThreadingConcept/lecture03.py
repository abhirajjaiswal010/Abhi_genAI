import time
import threading

# (timestamp_in_seconds, lyric_line)
lyrics = [
    (0,  "Cause there is something, and there is nothing"),
    (4,  "There is nothing in between"),
    (8,  "And in my eyes, there is a tiny dancer"),
    (13, "Watching over me, he's singing"),
    (17, "She's a, she's a lady, and I am just a boy"),
    (24, "He's singing, she's a, she's a lady"),
    (28, "And I am just a line without a hook"),
]

def show_line(line):
    """Typewriter effect for one line"""
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.09)
    print()

def displayLyrics(lyrics):


    start_time = time.time()

    for timestamp, line in lyrics:
        # wait until correct time
        while time.time() - start_time < timestamp:
            time.sleep(0.01)

        # start thread for typing effect
        t = threading.Thread(target=show_line, args=(line,))
        t.start()
        t.join()  # wait till line finishes

if __name__ == "__main__":
    displayLyrics(lyrics)
