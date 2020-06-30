function [level_array] = level_seperate(emotion_cell_array, level_filt, type_filt)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
%Takes adjusted text file and emotion symbol you wish to filter from the
%file as capitol letter string such as D for disgust.
%Can change to 3 + 1 or type_filt + 1 filt voice level and 5 + 1 or type_filt + 1 to filt face level
[tot_rows, tot_colms] = size(emotion_cell_array);
count1 = 1;
count2 = 1;
level_array(1,:) = emotion_cell_array(1, :);
while (count1 ~= tot_rows)
    count1 = count1 + 1;
    curr_face_level_cell = emotion_cell_array(count1, type_filt+1); %Can be changed to filter a diff colm
    curr_face_level_mat = cell2mat(curr_face_level_cell);
    if (str2num(curr_face_level_mat) >= level_filt)
        count2 = count2 + 1;
        level_array(count2,:) = emotion_cell_array(count1, :);
    end
end

    


return