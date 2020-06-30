function [emotion_array] = emotion_seperate(adjusted_txt_file, emotion_filt, type_filt)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
%Takes adjusted text file and emotion symbol you wish to filter from the
%file as capitol letter string such as D for disgust.
%Can change type to filter diff colm[ie. voice(3) or face level(5))]
[tot_rows, tot_colms] = size(adjusted_txt_file);
count1 = 1;
count2 = 1;
emotion_array(1,:) = adjusted_txt_file(1, :);
while (count1 ~= tot_rows)
    count1 = count1 + 1;
    curr_emotion_cell = adjusted_txt_file(count1, type_filt); %Can be changed to filter diff colm
    curr_emotion_mat = cell2mat(curr_emotion_cell);
    if (curr_emotion_mat == emotion_filt)
        count2 = count2 + 1;
        emotion_array(count2,:) = adjusted_txt_file(count1, :);
    end
end

    


return

