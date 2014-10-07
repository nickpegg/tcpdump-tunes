#!/usr/bin/env python

# Parses the text output of tcpdump (with no -v) from stdin, makes music

import re
import sys
from datetime import datetime

import midi


MIN_SPACING = 30
MIN_LENGTH = 20


def main():
    line_re = r"(?P<timestamp>\d{2}:\d{2}:\d{2}.\d{6}) IP (?P<src>\d+\.\d+\.\d+\.\d+)\.(?P<sport>\d+) > (?P<dst>\d+\.\d+\.\d+\.\d+)\.(?P<dport>\d+): (?:Flags \[(?P<flags>[SFPRUWE\.]+)\])?.+?length (?P<length>\d+)"

    pattern = midi.Pattern()
    track = midi.Track()
    pattern.append(track)

    last_time = datetime.now()
    line = sys.stdin.readline()
    while line:
        match = re.match(line_re, line)
        if match:
            data = match.groupdict()

            # Get the difference between now and the last event
            now = datetime.strptime(data['timestamp'], '%H:%M:%S.%f')

            spacing = int((now - last_time).microseconds / 1000.0)
            last_time = now

            if spacing < MIN_SPACING:
                spacing = MIN_SPACING

            # Determine note length based on packet length
            pkt_length = int(data.get('length', 0))
            note_length = int(pow(pkt_length, 0.75))

            if note_length < MIN_LENGTH:
                note_length = MIN_LENGTH

            # determine the note to play based on TCP flags
            note = midi.C_0
            flags = data.get('flags', '')
            if 'S' in flags:
                note = midi.D_0
            elif '.' in flags:
                note = midi.C_0
            elif 'F' in flags:
                note = midi.F_0
            elif 'R' in flags:
                note = midi.G_0

            # Determine the octave based on the src and dst IPs
            octave = hash((data['src'], data['dst'])) % 6 + 2
            note = note + octave * 12

            # Finally, append the note to the track
            track.append(midi.NoteOnEvent(tick=spacing, velocity=70, pitch=note))
            track.append(midi.NoteOffEvent(tick=note_length, pitch=note))

        line = sys.stdin.readline()

    # Dump MIDI track to stdout
    track.append(midi.EndOfTrackEvent(tick=1))
    midi.write_midifile('test.midi', pattern)

    return 0


if __name__ == '__main__':
    exit(main())
