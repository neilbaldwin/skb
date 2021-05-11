import os
import argparse
import lxml.builder as xb
from lxml import etree
from importlib.metadata import version
# from pbr.version import VersionInfo

__version__ = version('skb')
#__version__ = VersionInfo('skb').release_string()

class kitBuilder:
    def __init__(self):
        self.sdPath = ''
        self.kitName = ''
        self.synthList = []
        self.outputKit = xb.E.kit (
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
            ),

            xb.E.selectedDrumIndex("1"),
            firmwareVersion='3.1.5',
            earliestCompatibleFirmware="3.1.0-beta",
            lpfMode="24dB",
            modFXType="flanger",
            modFXCurrentParam="feedback",
            currentFilterType="lpf"
        )

    def kitName(self, name):
        self.kitName = name

    def sdPath(self, path):
        self.sdPath = path

    def addItems(self, items):
        for item in items:
            self.synthList.append(item)

    def removeItemAt(self, item):
        self.synthList.pop(item)

    def moveItemDown(self, item):
        moveItem = self.synthList[item]
        self.synthList.pop(item)
        self.synthList.insert(item+1, moveItem)

    def addSynthListFromFile(self, kitFilePath):
        try:
            with open(kitFilePath) as inputFile:
                self.addItems([line.rstrip() for line in inputFile])
            
            return 0

        except:
            print(f"\nInput file {kitFilePath} not found error\n\n")
            return 1

def main():

    # Create new blank kit object
    newKit = kitBuilder()
    parser = argparse.ArgumentParser()
        
    parser.add_argument('--sd-root', action='store', required=True,
        help='The path to the root of your SD card e.g. /Volumes/DELUGE')
    parser.add_argument('--input-file', action='store', dest='input_file', required=True,
        help='text file describing the kit to create.')
    parser.add_argument('--output-file', action='store', dest='output_file', required=True,
        help='XML output file')
    parser.add_argument('--version', action='version', version=__version__)

    args = parser.parse_args()

    # create absolute paths for kit file and output file
    newKit.sdPath = args.sd_root
    newKit.kitName = os.path.abspath(newKit.sdPath) + '/KITS/' + args.output_file
    kitFilePath = os.path.abspath(args.input_file)

    # Try reading and parsing kit file
    if (newKit.addSynthListFromFile(kitFilePath)):
        exit()

    # Find insertion point for individual sounds
    destinationSounds = newKit.outputKit.find('soundSources')

    # Iterrate through drums in XML kit file
    for synthName in newKit.synthList:

        inputFilePath = os.path.abspath(newKit.sdPath) + '/SYNTHS/' + synthName
        try:
            with open(inputFilePath) as inputFile:
                synthfile = inputFile.read()
        except:
            print(f"\nSynth \"{inputFilePath}\" not found error\n\n")
            exit()
      
        # parse synth file from text
        synthxml = etree.fromstring(bytes(synthfile, encoding='utf-8'))

        # We do not need firmware attributes so remove them
        synthxml.attrib.pop('firmwareVersion', None)
        synthxml.attrib.pop('earliestCompatibleFirmware', None)

        # Set drum name
        drumName = os.path.splitext(synthName)[0]
        synthxml.set('name', drumName)

        # append sound to kit sound sources
        destinationSounds.append(etree.XML(etree.tostring(synthxml)))

    # output prettyfied XML
    outputxml = (etree.tostring(newKit.outputKit, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode())

    with open(newKit.kitName, 'w') as outputFile:
        outputFile.write(outputxml)
        print("Success! Kit wrote to SD card...")

if __name__ == "__main__":
   main()
