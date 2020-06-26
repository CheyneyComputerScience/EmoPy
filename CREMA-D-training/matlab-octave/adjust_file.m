function [summaryTable] = adjust_file
%adjust_file gets a file and converts it to just the data of the table
%   need to load the io package using
%   pkg load io

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

wholeTable = csv2cell(curr_fnm);
% assumes there is a single header row.
wholeTable (1,:)
summaryTable = wholeTable(2:end,:);

return

