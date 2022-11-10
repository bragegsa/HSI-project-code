clear all;
close all;
clc
warning('off');

% Choose the dataset you want to load
dataset_name = 'data/anomaly_datasets/abu-airport-1';
results_name = 'data/results/cbad_out_2c';

% dataset = ['plot/', dataset_name];
% results = ['plot/', dataset_name, '_res'];
% disp(join(results));

% load(join(dataset));
load(dataset_name);
load(results_name);
mask = map;
% load(join(results));

AUC=ROC(cbad_out,mask,0);

disp(AUC);