from tkinter import Tk, Text, Frame, Button
import pyttsx3

engine = pyttsx3.init()

font = ('open sans', 13, 'bold')


# Functions
def speak(voice_id):
    # Rate of speech
    engine.setProperty('rate', 150)
    # Volume
    engine.setProperty('volume', 0.8)
    # Voices
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)

    # Convert text to speech
    words = textarea.get('1.0', 'end')
    engine.say(words)
    engine.runAndWait()
    engine.stop()

    # Save to file
    engine.save_to_file(words, 'audio.mp3')


# UI
app = Tk()
app.title("Text 2 Speech")
app.geometry('500x400+400+150')
app.resizable(False, False)

# Frames
mainframe = Frame(app)
mainframe.pack()

top_frame = Frame(mainframe)
top_frame.pack()

textarea = Text(top_frame, height=17, font=font)
textarea.pack(fill='x', padx=5, pady=5)

bottom_frame = Frame(mainframe)
bottom_frame.pack()

male_btn = Button(bottom_frame, width=15, height=2, font=font, text='Male',
                  command=lambda: speak(0)
                  )
male_btn.pack(side='left')

female_btn = Button(bottom_frame, width=15, height=2, font=font, text='Female',
                    command=lambda: speak(1)
                    )
female_btn.pack(side='left')

app.mainloop()