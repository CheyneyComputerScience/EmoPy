function [adjusted_txt_file] = adjust_file
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

%Set the paramater to the handle of the figure with tag fig.1
h_fig = findobj('tag', 'fig.1');
%If h_fig is empty generates a figure with handle h_fig, tag fig.1 and
%filename default.png
if (isempty(h_fig))
	h_fig = figure('tag', 'fig.1','filename', 'default.txt');
end
%Sets parameter equal to the filename stored in the figure with handle
%h_fig
def_fnm = get(h_fig, 'filename');
%Prompts the user to select a .exp file with the title of pop-up window
%as Choose File and the default filename def_fnm. Sets the filename and
%path of the file to that of the file chosen.
[fnm pth] = uigetfile('*','Choose File', def_fnm);
curr_fnm = fullfile(pth, fnm);
set(h_fig, 'filename', curr_fnm)
S_curr = uiimport(curr_fnm);
dim_file = size(S_curr.summaryTable);
tot_rows = dim_file(1,1); %or (7443)
count1 = 0;
%adjusted_txt_file = {};
final_filt_mat = [];
while (count1 ~= tot_rows)
    count1 = count1 + 1;
    curr_line = S_curr.summaryTable(count1,1);
    %Splits the item into cells by chosen character 
    curr_split_line = regexp(curr_line, ',', 'split');
    dim_line = size(curr_split_line{1,1});
    curr_colms = dim_line(1,2);
    count2 = 0;
    while (count2 ~= curr_colms)
        count2 = count2 + 1;
        %Sets the parameter to the the first row count2 colm cell of the
        %cell in the frist row and column of the cell array curr_split_line
        curr_split_cell = curr_split_line{1,1}(1,count2);
        curr_filt_cell = regexp(curr_split_cell, '"', 'split');
        final_filt_cell = curr_filt_cell{1,1}(1,2);
        adjusted_txt_file(count1, count2) = final_filt_cell;
    end
end





return

