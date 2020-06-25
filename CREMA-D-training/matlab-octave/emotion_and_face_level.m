emotion_filt = 'D';
[emotion_array] = emotion_seperate(adjusted_txt_file, emotion_filt);
level_filt = 50;
[level_array] = level_seperate(emotion_array, level_filt);