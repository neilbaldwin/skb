SKB

Synth Kit Builder for Synthstrom Deluge

Basic utility script for creating a KIT from existing SYNTH sounds.

You need:

to put your Deluge SD card in your computer

    the script WILL write to your SD card. If this makes you nervous back it up first.

to create a XML file that describes the kit you'd like (see example)

    The structure is simple. You need the filename of each synth you'd like to load
    into KIT lanes. Put the full name in, including the XML extension. You also can
    specify a name for the SYNTH as it will appear in the KIT, otherwise leave this
    blank ("") and it will use the name of the SYNTH.

to get the path of your SD card when it's mounted on your computer

    On OSX it will be something like /Volumes/DELUGE. I'm not a Windows user so I haven't
    done a version for that platform yet but I will try. I'll put the source on GitHub so
    theoretically you should be able to build an executable on Windows using py2win, for
    example (https://pypi.org/project/py2win/). Heopfully I can update this soon with a
    Windows version.

to copy the executable to a place on your computer (OSX) to be able to run it from the Terminal.

If you copy it to your Desktop then launch Terminal, cd to your Desktop and type:

./skb

which, if it runs will complain about a lack of arguments/options. Do:

./skb -h to show some help text

To run it properly, put your kit descriptor XML file in the same folder as the executable (SKB) and:

./skb --sd-root <your sd root> --input-file <your kit file> --output-file <name of the new kit>

