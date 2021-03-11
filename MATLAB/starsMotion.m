%% Изучение красного смещения звуёзд

close all
clear variables
%% 
% Иморт данных

spectra = importdata("spectra.csv");
lambdaStart = importdata("lambda_start.csv");
lambdaDelta = importdata("lambda_delta.csv");
starNames = importdata("star_names.csv");
%starNames1 = starNames';

%a = starNames1{2}
%% 
% Константы

lambdaPr = 656.28; %нм
speedOfLight = 299792.458; %км/c
%% 
% Определение диапазона длин волн
% 
% 

nPl = size(spectra)
speed = zeros(1, nPl(2));
grafix = zeros(1, nPl(2));

movaway = {};
nObs = size(spectra, 1);
lambdaEnd = lambdaStart + (nObs - 1)*lambdaDelta;
lambda = (lambdaStart : lambdaDelta : lambdaEnd)';


%% 
% Основной цикл

fg1 = figure;
hold on

for i = 1:1:nPl(2)
    s = spectra(:, i);
    [sHa, idx] = min(s);
    lambdaHa = lambda(idx);
    
    z = (lambdaHa/lambdaPr) - 1;
    speed1 = z * speedOfLight ;
    speed(i) = speed1;
end

for i = 1:1:nPl(2)
    s = spectra(:, i);
    [sHa, idx] = min(s);
    lambdaHa = lambda(idx);
    
    z = (lambdaHa/lambdaPr) - 1;
    %speed1 = z * speedOfLight ;
    %speed(i) = speed1;
    %plot(lambda, s, "b--o" , 'MarkerIndices',1:5:length(s), 'MarkerSize', 2, 'Color', [rand()*0.8, rand()*0.8, rand()*0.8])
    
    if z<0
        grafix(i) = plot(lambda, s, "--", 'Color', [rand()*0.8, rand()*0.8, rand()*0.8], 'Linewidth',1, 'DisplayName', starNames{i})
    else
        grafix(i) = plot(lambda, s, 'Color', [rand()*0.8, rand()*0.8, rand()*0.8], 'Linewidth',3, 'DisplayName', starNames{i})
        movaway(end+1) = starNames(i);
    end
    
    set(gcf, 'Visible', 'on')
    xlabel('Длина волны, нм');
    ylabel(['Инстенсивность, эрг/см^2/c/', char(197)]);
    title({'Спектры звезд'})
    %  legend('I(\lambda )')
    grid on
    %plot(lambdaHa, sHa, 'rs', 'MarkerSize', 8)
end
%legend('I(\lambda)',  'northeast')
legend(grafix, 'Location', 'northeast')
text(633, 2.1*10^(-13), 'Акулов Александр Б01-005')

hold off

saveas(fg1, 'spectra.png');