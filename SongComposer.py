import random

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
def generate_song(note, octave, notes_song):
    # Define the musical notes
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    # Create the musical scale starting from the given note and octave
    scale = [note + str(octave) for note in notes]

    # Randomly select Tonic (I), Dominant (V), and Subdominant (IV) notes
    tonic = random.choice(scale)
    dominant = scale[(scale.index(tonic) + 7) % 12]  # Fifth note in the scale
    subdominant = scale[(scale.index(tonic) + 5) % 12]  # Fourth note in the scale

    # Combine selected notes to create the song
    song = [tonic, dominant, subdominant] * (notes_song // 3)
    # Add remaining notes randomly
    song += random.sample(scale, notes_song % 3)

    return song

while True:
    # Example usage
    print(notes)
    user_note = input("Enter a musical note (A, A#, B, ..., G#): ")
    user_octave = int(input("Enter the octave (0 to 7): "))
    num_notes = int(input("Enter the number of notes for the song (0 to 6): "))

    result = generate_song(user_note, user_octave, num_notes)
    print("Generated Song:", result)
