# Tcpdump Tunes

Think tcpdump is too boring? Put some music to your packets!

Takes tcpdump human output in, spits out a MIDI file to /tmp/tcpdump.mid.

This is a terrible hack. It's mostly interesting with TCP traffic.

## Installation
1. Clone this repo
2. Install python-midi from here: https://github.com/vishnubob/python-midi/
3. Enjoy some sweet jams

## Usage
`tcpdump -n -c 100 | ./tcpdump_tunes.py; timidity /tmp/tcpdump.mid`

* The `-n` option is required since my regex is lazy and domain lookups are slow.
* The `-c` option is required since the MIDI file can't be created until all notes (packets) are accounted for

## Credits
Thanks to @ryanwohara for the idea
