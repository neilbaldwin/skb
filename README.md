# SKB - Synth Kit Builder for Synthstrom Deluge

A Python utility for the Synthstrom Deluge, used for building KITS (drum kits) from existing SYNTH sounds.

## Motivation

Reasoning: whilst you can manually create a KIT using the synthesis engine and you can build a KIT by loadinging one or more samples into a KIT LANE, it's not possible, as of Firmware 3.1.5, to load SYNTH files into KIT LANES. I wrote this utility to enable you to do just that.

## Requirements

- Latest Deluge firmware. At time of first release this is 3.1.5
- The ability to mount your Deluge SD card in your computer and have read/write access
- Python 3 plus Pip tools to install Paython packages
- familiarity with Python command-line tools

## Installation or Getting Started

Provding you have Python 3 and the corresponding Pip installer tools it should be a case of just doing:

```Text
python3 -m pip install skb
```

## Usage

skb --sd-root 'path' --input-file 'filemame' --ouput-file 'filename'

Example:

```Text
skb --sd-root '/Volumes/DELUGE32/' --input-file 'kitfile.txt' --output-file skb.XML
```

**sd-root** = full path to root of your mounted SD card e.g. /Volumes/DELUGE/

**input-file** = name of XML file which describes your KIT contents (see below)

**output-file** = name of the generated KIT file, plain text, one synth filename per line

## XML Kit File

In order to tell the tool which SYNTH patches you want in your KIT, you need to create a text file e.g.

```Text
KICK.XML
SNARE.XML
CLAP.XML
```

Do not include the full path e.g. /SYNTHS/KICK.XML - just specify the synth XML filename.

The script will create the KIT in reverse order meaning the first synth in your text file will be the lowest row etc.

You can specify the same SYNTH more than once and theoretically there should be no (reasonable) limit to how many lanes you can generate. For anyone wanting to build their own synth kits, this tool would be really handy as you could create, say, a kick drum synth patch that you're happy with and then load 16 copies of that into a KIT. Then you can tweak each one on the Deluge to give you a kit full of variation on the synthesis method.

It's probably worth pointing out that any editing or changes you make to the generated kit on the Deluge will not be reflected in the original SYNTH patches. That's probably a good thing though!

NOTE:

The script assumes (correctly!) that you have a KITS and SYNTHS folder in the root of your Deluge SD card. It will look for the SYNTH patches in the SYNTHS folder and will output the KIT in the KITS folder.

## Contributors

Contributions welcome!

## License

MIT
