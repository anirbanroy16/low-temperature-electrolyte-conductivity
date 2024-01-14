
% This script processes the raw data to create model-ready inputs

clearvars
clear all

tic
data = readtable ('HTE_dataset_PC_EMC_EC_LiPF6.csv');
data = data (data.Temp_K<=243.5 & data.PC_fraction~=1,:);

salt_loading_values = unique (data.salt_load);

averages = zeros(size(salt_loading_values,1),2);

for i=1: size (salt_loading_values)
    window = data(data.salt_load==salt_loading_values(i),:);
     averages(i,1)= mean (window.PC_fraction);
     averages(i,2)= mean (window.conductivity);

end
 average_values = horzcat(salt_loading_values,averages);

 x = average_values(:,1);
 y = average_values (:,2);
z = average_values (:,3);

scatter (x,z,[],y, 'filled')

colormap jet

xlabel ("[Li] in e'lyte, mol kg {-1}")
ylabel ('conductivity')
zlabel ('PC fraction')

axis ('square')
