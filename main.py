import tkinter as tk
from tkinter import filedialog
import lyricwikia
import pyautogui


def save_lyrics():
    foldername = filedialog.askdirectory() # get the path of the folder the save the lyrics text file in
    if foldername == "": # checks if a folder was chosen
        pyautogui.alert(text="Choose a folder!")
    else:
        if song_lyrics.get("1.0", "end") is not None: # checks if there is any text in the text box
            try:
                cr = open(foldername + "\\" + song + " Lyrics.txt", "x") # creates a text file with the song name and " Lyrics"
            except NameError: # catches the error if there is no song's lyrics
                pyautogui.alert(text="Get a song's lyrics first!")
            except FileExistsError:
                pyautogui.alert(text="File already exists")
            else:
                with open(foldername + "\\" + song + " Lyrics.txt", "w") as file:
                    song_lyrics_text = song_lyrics.get("1.0", "end")
                    pyautogui.alert(text="Get a song's lyrics first!")
                    file.write(song_lyrics_text)
                    pyautogui.alert(text="lyrics saved at " + song + "Lyrics.txt")
                    file.close()
        else:
            pyautogui.alert(text="Get a song's lyrics first!")


def get_song_lyrics():
    artist = artist_entry.get()
    global song
    song = song_entry.get()
    try:
        lyrics = lyricwikia.get_lyrics(artist, song) # gets the lyrics from the api
    except Exception:
        pyautogui.alert(title='Error!', text="Error! Song or Artist Not Found")
    else:
        song_lyrics.delete("1.0", "end") # "flashes" the text box
        song_lyrics.insert("1.0", lyrics) # putting in the new song lyrics


canvas_background = "black"

hex_colors = {"blue": "#1a75ff", "turquoise": "#00e6e6", "green": "#39e600", "orange": "#ff9933", canvas_background: "#404040",
              "dark green": "#006622", "navy blue": "#006699", "light blue and green": "#00cc99", "very light blue": "#66ffff",
              "another dark blue": "#006666", "very light green": "#bbff33", "another green": "#33cc33"}

win = tk.Tk()
win.geometry("800x800")
win.title("Songs Lyrics")
win.resizable(width=False, height=False)

# ------------ Canvas ------------
canvas = tk.Canvas(height=800, width=800, bg=hex_colors[canvas_background])
canvas.place(x=0, y=0)
# ------------ LABELS ------------
enter_artist_label = tk.Label(text="Enter artist name: ", font=("Roboto Light", 14), bg=hex_colors[canvas_background])
enter_artist_label.place(x=20, y=60)
enter_song_label = tk.Label(text="Enter song name: ", font=("Roboto Light", 14), bg=hex_colors[canvas_background])
enter_song_label.place(x=20, y=88)
# ------------ Entry --------------
artist_entry = tk.Entry(font=("Roboto Light", 10))
artist_entry.place(x=178, y=66)
song_entry = tk.Entry(font=("Roboto Light", 10))
song_entry.place(x=178, y=94)
# ----------- Text Box -------------
song_lyrics = tk.Text(font=("Roboto light", 12), width=44, height=20)
song_lyrics.place(x=380, y=60)
# ----------- Buttons --------------
get_lyrics_button = tk.Button(text="Get lyrics", font=("Roboto Light", 12), height=4, width=16, command=get_song_lyrics,
                              bg=hex_colors["another green"])
get_lyrics_button.place(x=520, y=460)
save_lyrics_button = tk.Button(text="Save Lyrics", font=("Roboto Light", 12), height=4, width=16,
                               bg=hex_colors["another green"], command=save_lyrics)
save_lyrics_button.place(x=520, y=560)

# TODO create an exe file of this
# TODO search online why i can't the lyrics of some songs
# TODO check why i can't use lyricwikia when i'm converting this to exe

win.mainloop()
