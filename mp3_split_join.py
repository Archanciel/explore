from pydub import AudioSegment

SOUND_FILE = 'c:/temp/JMJ2.mp3'
#SOUND_FILE = '/storage/emulated/0/music/JMJ2.mp3'
#SOUND_FILE_NEW = '/storage/emulated/0/music/JMJ2_new.mp3'
SOUND_FILE_EXTRACT = 'c:/temp/JMJ2_extract.mp3'
SOUND_FILE_EXTRACT_3_TIMES = 'c:/temp/JMJ2_extract_3.mp3'

sound = AudioSegment.from_mp3(SOUND_FILE)

# len() and slicing are in milliseconds
startPosition = 1626 * 1000
endPosition = 1686 * 1000
extractedPortion = sound[startPosition:endPosition]

# Concatenation is just adding
extractedPortionThree = extractedPortion + extractedPortion + extractedPortion

# writing mp3 files is a one liner
extractedPortion.export(SOUND_FILE_EXTRACT, format="mp3")
extractedPortionThree.export(SOUND_FILE_EXTRACT_3_TIMES, format="mp3")