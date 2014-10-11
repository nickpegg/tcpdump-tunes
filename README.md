# Tcpdump Tunes

Think tcpdump is too boring? Put some music to your packets!

Takes tcpdump human output via stdin, spits out a MIDI file to stdout.

This is a terrible hack. It's mostly interesting with TCP traffic.

## Installation
1. Clone this repo
2. Install python-midi from here: https://github.com/vishnubob/python-midi/
3. Enjoy some sweet jams

## Usage
`tcpdump -n -c 100 | ./tcpdump_tunes.py | timidity -`

* The `-n` option is required since domain lookups are slow and my regex is lazy.
* The `-c` option is required since the MIDI file can't be created until all notes (packets) are accounted for

## Credits
Thanks to Ryan O'Hara for the idea
