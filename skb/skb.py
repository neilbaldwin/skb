import os
import argparse
import lxml.builder as xb
from lxml import etree

def main():

    # XML builder template for empty Deluge KIT
    kit_template = xb.E.kit (
        xb.E.delay(
            pingPong="1",
            analog="0",
            syncLevel="7",
        ),
        xb.E.compressor(
            syncLevel="7",
            attack="327244",
            release="936",
        ),
        xb.E.defaultParams(
            xb.E.delay(
                rate="0x00000000",
                feedback="0x80000000",
            ),
            xb.E.lpf(
                frequency="0x7FFFFFFF",
                resonance="0x80000000",
            ),
            xb.E.hpf(
                frequency="0x80000000",
                resonance="0x80000000",
            ),
            xb.E.equalizer(
                bass="0x00000000",
                treble="0x00000000",
                bassFrequency="0x00000000",
                trebleFrequency="0x00000000",
            ),
            reverbAmount="0x80000000",
            volume="0x3504F334",
            pan="0x00000000",
            sidechainCompressorShape="0xDC28F5B2",
            modFXDepth="0x00000000",
            modFXRate="0xE0000000",
            stutterRate="0x00000000",
            sampleRateReduction="0x80000000",
            bitCrush="0x80000000",
            modFXOffset="0x00000000",
            modFXFeedback="0x80000000",
        ),
        xb.E.soundSources(
            #xb.E.sound(),
            #xb.E.sound(),
        ),
        xb.E.selectedDrumIndex("1"),
        firmwareVersion='3.1.5',
        earliestCompatibleFirmware="3.1.0-beta",
        lpfMode="24dB",
        modFXType="flanger",
        modFXCurrentParam="feedback",
        currentFilterType="lpf"
    )

    # Parse command line
    parser = argparse.ArgumentParser()
        
    parser.add_argument('--sd-root', action='store', dest='sd_root', required=True,
        help='The path to the root of your SD card e.g. /Volumes/DELUGE')
    parser.add_argument('--input-file', action='store', dest='input_file', required=True,
        help='XML file describing the kit to create. Run with -h for more detail.')
    parser.add_argument('--output-file', action='store', dest='output_file', required=True,
        help='XML output file')

    args = parser.parse_args()

    # create absolute paths for kit file and output file
    outputFilePath = os.path.abspath(args.sd_root) + '/KITS/' + args.output_file
    kitFilePath = os.path.abspath(args.input_file)

    # Try reading and parsing kit file
    try:
        kitfile = etree.parse(kitFilePath)
    except:
        print("\nFile not found error\n\n")
        exit()

    # Find insertion point for individual sounds
    destinationSounds = kit_template.find('soundSources')

    # Iterrate through drums in XML kit file
    for drum in kitfile.iter('drum'):
        synthName = str(drum.attrib['synth'])
        inputFilePath = os.path.abspath(args.sd_root) + '/SYNTHS/' + synthName
        with open(inputFilePath) as inputFile:
            synthfile = inputFile.read()
        
        # parse synth file from text
        synthxml = etree.fromstring(bytes(synthfile, encoding='utf-8'))

        # We do not need firmware attributes so remove them
        synthxml.attrib.pop('firmwareVersion', None)
        synthxml.attrib.pop('earliestCompatibleFirmware', None)

        # Set drum name
        drumName = str(drum.attrib['name'])
        if not drumName:
                drumName = os.path.splitext(synthName)[0]
        synthxml.set('name', drumName)

        # append sound to kit sound sources
        destinationSounds.append(etree.XML(etree.tostring(synthxml)))

    # output prettyfied XML
    outputxml = (etree.tostring(kit_template, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode())

    with open(outputFilePath, 'w') as outputFile:
        outputFile.write(outputxml)


if __name__ == "__main__":
   main()
