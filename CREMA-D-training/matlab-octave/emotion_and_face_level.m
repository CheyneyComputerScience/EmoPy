% this is an octave forge package
% download from: https://octave.sourceforge.io/io/
% after downloading, install with command: 
% pkg install '~/Downloads/io-2.6.1.tar.gz'
pkg load io

adjusted_txt_file = adjust_file;
emotion_filt = 'N';
type_filt = 3; %Change to 3 for voice to 5 for face
[emotion_array] = emotion_seperate(adjusted_txt_file, emotion_filt, type_filt);
level_filt = 50;
[level_array] = level_seperate(emotion_array, level_filt, type_filt);

cell2csv("neutralTrain_audio50.csv",level_array)