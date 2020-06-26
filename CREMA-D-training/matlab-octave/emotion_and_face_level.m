% this is an octave forge package
% download from: https://octave.sourceforge.io/io/
pkg load io

adjusted_txt_file = adjust_file;
emotion_filt = 'D';
[emotion_array] = emotion_seperate(adjusted_txt_file, emotion_filt);
level_filt = 50;
[level_array] = level_seperate(emotion_array, level_filt);

cell2csv("disgustTrain50.csv",level_array)