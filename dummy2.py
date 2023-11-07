import mido
from mido import MidiFile, MidiTrack, Message
import tempfile
import subprocess
import json
import os
import time
from pydub import AudioSegment


def PlaySound(Tone,Length):

    # Create a MIDI file
    midi_file = MidiFile()

    #Load Config
    soundfont_path = "/usr/share/sounds/sf2/FluidR3_GM.sf2"

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
        "-F", "/tmp/temp.wav",
        'quit'
    ]


    #subprocess.call(command)
    process = subprocess.Popen(command)
    playback_duration = Length/1000 + 0.6
    time.sleep(playback_duration)
    process.terminate()
    sound = AudioSegment.from_wav("/tmp/temp.wav")
    sound.export(str(Tone) + str(Length), format="mp3")
    
    
PlaySound(56,2000)
PlaySound(56,1000)
PlaySound(56,500)
PlaySound(56,250)

PlaySound(59,2000)
PlaySound(59,1000)
PlaySound(59,500)
PlaySound(59,250)

PlaySound(63,2000)
PlaySound(63,1000)
PlaySound(63,500)
PlaySound(63,250)

PlaySound(66,2000)
PlaySound(66,1000)
PlaySound(66,500)
PlaySound(66,250)