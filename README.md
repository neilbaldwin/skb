# SKB - Synth Kit Builder for Synthstrom Deluve

A Python utility for building KITS (drum kits) for the Synthstrom Deluge.

## Motivation

Reasoning: whilst you can manually build a KIT using the synthesis engine and you can build a KIT by loadinging one or more samples into a KIT LANE, it's not possible, as of Firmware 3.1.5, to load SYNTH files into KIT LANES. I wrote this utility to enable you do do just that.

## Requirements

- Latest Deluge firmware. At time of first release this is 3.1.5
- The ability to mount your Deluge SD card in your computer and have read/write access
- Python 3 plus Pip tools to install Paython packages
- familiarity with Python command-line tools

## Installation or Getting Started

Provding you have Python 3 and the corresponding Pip installer tools it should be a case of just doing:

    python3 -m pip install skb

## Usage

skb --sd-root 'path' --input-file 'path' --ouput-file 'path'

    sd-root = full path to root of your mounted SD card e.g. /Volumes/DELUGE/
    input-file = name of XML file which describes your KIT contents (see below)
    output-file = name of the generated KIT file, including .XML extension

XML Kit File

In order to tell the tool which SYNTH patches you want in your KIT, you need to create a basic XML file e.g.

    ```XML
    <?xml version='1.0' encoding='UTF-8'?>
    <synthkit>
        <drum synth="KICK.XML" name="BIG KICK" />
        <drum synth="SNARE.XML" name="" />
        <drum synth="CLAP.XML" name="" />
    </synthkit>
    ```

    synth = filename of the SYNTH patch you'd like to load into the KIT LANE
    name = optional name to display in the KIT LANE, if blank ("") the filename is used

NOTE:

The script assumes (correctly!) that you have a KITS and SYNTHS folder in the root of your Deluge SD card. It will look for the SYNTH patches in the SYNTHS folder and will output the KIT in the KITS folder.

## Contributors

Contributions welcome!

## License

MIT
