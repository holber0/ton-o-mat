import mido
from mido import MidiFile, MidiTrack, Message
import tempfile
import subprocess
import json
import os
import time


def PlaySound(Tone,Length):

    # Create a MIDI file
    midi_file = MidiFile()

    #Load Config
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)

    soundfont_path = config['fluidsynth']['soundfont_path']


    #Cleanup old Midi Files
    directory = '/tmp'
    # List all files in the specified directory
    files = os.listdir(directory)

    # Loop through the files and delete MIDI files
    for file in files:
        if file.endswith(".midi") or file.endswith(".mid"):
            file_path = os.path.join(directory, file)
            os.remove(file_path)
   
   
    #Start MIDI Generation    
    track = MidiTrack()
    midi_file.tracks.append(track)

    # Add a note (e.g., C4) to the track
    track.append(Message('note_on', note=int(Tone), velocity=64, time=0))  # C4
    track.append(Message('note_off', note=int(Tone), velocity=64, time=Length))  # Release note

    with tempfile.NamedTemporaryFile(suffix='.mid', delete=False) as tmp_midi_file:
        tmp_midi_path = tmp_midi_file.name
        midi_file.save(tmp_midi_path)


    command = [
        'fluidsynth',
        '-a', 'alsa',
        '-m', 'alsa_seq',
        soundfont_path,
        tmp_midi_path,
        'quit'
    ]

    #subprocess.call(command)
    process = subprocess.Popen(command)
    playback_duration = Length/1000 + 0.6
    time.sleep(playback_duration)
    process.terminate()

