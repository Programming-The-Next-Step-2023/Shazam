import os
from pydub import AudioSegment

# to do later:
# 1. add check if input is mp3 or allow other types of audio inputs


# directory where mp3 files are found
my_input_directory = 'C:/Users/mirth/Documents/GitHub/Shazam/Shazam/input'
# directory of stored .wav files
my_output_directory = 'C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output'


def converter(input_directory, output_directory):
    """This function takes the input directory of the folder that contains mp3 audio files. It converts the .mp3 files 
    into .wav files. These .wav files are stored in an output directory.

        Parameters:
        input_directory(str): the input directory of the folder that contains the audio files
        output_directory(str): the output directory of the folder where the converted audio files should be stored
        
        Example: 
        There is a local folder that contains several .mp3 files, defined as input_directory
        There is a local folder where the .wav files should be stored, defined as output_directory
        To convert my .mp3 files to .wav files, the convert function can be used

        output_directory = 'C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output'
        input_directory = 'C:/Users/mirth/Documents/GitHub/Shazam/Shazam/input'
        converter(input_directory, output_directory)
       """

    # get list of all audio mp3 files in input folder
    audio_list = os.listdir(input_directory)
    for song in audio_list:
        input_filename = os.path.join(input_directory, song)
        output_filename = os.path.join(output_directory, song.replace('mp3', 'wav'))
        sound = AudioSegment.from_mp3(input_filename)
        sound = sound.set_channels(1) # from stereo to mono
        sound.export(output_filename, format="wav")


converter(my_input_directory, my_output_directory)
