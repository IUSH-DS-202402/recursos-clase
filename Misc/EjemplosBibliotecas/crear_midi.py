# Tomado de https://github.com/craffel/pretty-midi


import pretty_midi
# Create a PrettyMIDI object
cello_c_chord = pretty_midi.PrettyMIDI()
# Create an Instrument instance for a cello instrument
cello_program = pretty_midi.instrument_name_to_program('Cello')
cello = pretty_midi.Instrument(program=cello_program)
notes = ['C5', 'E5', 'G5']
# Iterate over note names, which will be converted to note number later
for pos in range(0,len(notes)):
    # Retrieve the MIDI note number for this note name
    note_number = pretty_midi.note_name_to_number(notes[pos])
    # Create a Note instance for this note, starting at 0s and ending at .5s
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=pos, end=pos+1)
    # Add it to our cello instrument
    cello.notes.append(note)
# Add the cello instrument to the PrettyMIDI object
cello_c_chord.instruments.append(cello)
# Write out the MIDI data
cello_c_chord.write('cello-C-chord.mid')