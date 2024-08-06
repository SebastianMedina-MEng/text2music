# Import required libraries
import random
import os
import music21
import time  # Add this line to import the time module
import pygame  # Add this line to import the pygame module
from pydub import AudioSegment  # Add this line to import the AudioSegment class from pydub
from midi2audio import FluidSynth

cwd = r'C:\Users\PC\PycharmProjects\Text2Music'
os.chdir(r'C:\Users\PC\PycharmProjects\Text2Music')
starting_oct = 0
pitch_names = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

def generate_music(string_input, bpm):


    # Filter out non-alphabetic characters from the input string
    string_input = ''.join(char for char in string_input if char.isalpha())

    # Step 1: Extract distinct characters from the input string
    unique_characters = list(set(string_input))
    num_octaves = (len(unique_characters) // 7) + 1
    notes_mapping = dict()
    k=0
    oct = 4     ## starting oct
    for j in range (len(unique_characters)):
        note = str(pitch_names[k])+str(oct)
        print(note)
        pitch = music21.pitch.Pitch(note)
        note_duration = music21.duration.Duration((random.choice([0, 0.125, 0.25, 0.5,  1, 2])) )  # 1, 2, 4, or 8 beats
        notes_mapping[unique_characters[j]] = music21.note.Note(pitch, duration=note_duration)
        if k == len(pitch_names)-1:
            k=0
            oct=oct+1
        else:
            k=k+1
    #print(note)
    ##print(unique_characters)


    # Step 4: Create a stream to hold the musical notes
    music_stream = music21.stream.Score()

    # Step 5: Add notes to the stream based on the input string
    for char in string_input:
        # Create a new Note object for each occurrence
        music_stream.append(music21.note.Note(notes_mapping[char].pitch, duration=notes_mapping[char].duration))

    # Step 6: Set the tempo for the music
    music_stream.insert(0, music21.tempo.MetronomeMark(number=bpm))

    # Step 7: Save the generated music as a MIDI file
    midi_filename = 'generated_music.mid'
    music_stream.write('midi', fp=midi_filename)

    FluidSynth().play_midi(os.path.join(cwd,midi_filename))

# Example usage:
generate_music("Hey Fiona, No tengo nada de ganas de pelear cotigo... asi que espero que no lo hagamos más... es más, me gustaría que nos olvidaramos de todo e hicheramos el amor ahora mismo!", 120)
# Add a delay to allow pygame to play the music
time.sleep(10)  # Adjust the sleep duration as needed