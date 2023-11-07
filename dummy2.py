import rtmidi
import time

def PlaySound(Tone,Length):
    # Create a MIDI output port
    midiout = rtmidi.MidiOut()
    selected_port = 1  
    midiout.open_port(1)


    # Send a MIDI note-on message (Note 60, Velocity 64)
    note_on = [0x90, Tone, 64]
    midiout.send_message(note_on)
    time.sleep(Length/1000)

    # Send a MIDI note-off message (Note 60, Velocity 0)
    note_off = [0x80, Tone, 0]
    midiout.send_message(note_off)

    # Close the MIDI output port
    midiout.close_port()

PlaySound(52,500)