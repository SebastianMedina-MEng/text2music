from music21 import stream, meter, key, chord

import random

def generate_chord_progression(num_chords):
    # Define the musical notes
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    # Create the musical scale
    scale = [note + '4' for note in notes]  # Octave 4

    # Initialize a music stream
    music_stream = stream.Score()
    music_stream.append(meter.TimeSignature('4/4'))
    music_stream.append(key.KeySignature(0))  # C major key

    # Generate and add chords to the stream
    for _ in range(num_chords):
        # Randomly select a root note for the chord
        root_note = random.choice(scale)

        # Define the chord type (major or minor)
        chord_type = random.choice(['major', 'minor'])

        # Build the chord
        if chord_type == 'major':
            current_chord = chord.Chord(
                [root_note, scale[(scale.index(root_note) + 4) % 12], scale[(scale.index(root_note) + 7) % 12]])
        else:  # Minor chord
            current_chord = chord.Chord(
                [root_note, scale[(scale.index(root_note) + 3) % 12], scale[(scale.index(root_note) + 7) % 12]])

        # Append the chord to the stream
        music_stream.append(current_chord)

    meter.freezeNotation(music_stream)
    return music_stream

# Example usage
num_chords = 8
progression_stream = generate_chord_progression(num_chords)

# Save the chord progression to a MusicXML file
progression_stream.write('musicxml', 'chord_progression.xml')

# Optionally, you can uncomment the following line to open the file using the default application
# progression_stream.show('musicxml')
