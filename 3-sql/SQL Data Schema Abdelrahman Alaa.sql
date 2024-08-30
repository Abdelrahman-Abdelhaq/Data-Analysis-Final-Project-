drop database if exists mydatabase;

CREATE DATABASE mydatabase;
use mydatabase;

create table cleaned_1 (
Country_or_dependency varchar(50) primary key,
Population_2024 int,
Yearly_Change float,
Net_Change int,
Density_PKm2 int,
Land_Area_Km2 int,
Migrants_net int,
Fertility_Rate float,
Median_Age int,
Urban_Pop_Percentage int,
World_Share float
);



create table cleaned_2 (
Country_or_dependency varchar(50) primary key,
Total_Area_KM int,
Total_Area_M int,
Land_Area_KM int,
Land_Area_M	int,
Percentage_World_Mass float
);


create table cleaned_3 (
Year int primary key,
World_Population double,
Percentage_Yearly_Change float,
Net_change int,
Population_Density int
);


create table cleaned_4 (
Country_or_dependency varchar(50) primary key,
kids float,
adults float,
retired float
);

select * from cleaned_1;
select * from cleaned_2;
select * from cleaned_3;
select * from cleaned_4;


 select cleaned_1.Country_or_dependency,
    Population_2024,
    Yearly_Change,
    Net_Change,
    Density_PKm2,
    Land_Area_Km2,
    Migrants_net,
    Fertility_Rate,
    Median_Age,
    Urban_Pop_Percentage,
    World_Share,
    Total_Area_KM,
    Total_Area_M,
    Land_Area_KM,
    Land_Area_M,
    Percentage_World_Mass
FROM 
    cleaned_1
JOIN 
    cleaned_2
ON 
    cleaned_1.Country_or_dependency = cleaned_2.Country_or_dependency;
    
SELECT 
    cleaned_1.Country_or_dependency,
    Population_2024,
    Yearly_Change,
    Net_Change,
    Density_PKm2,
    Land_Area_Km2,
    Migrants_net,
    Fertility_Rate,
    Median_Age,
    Urban_Pop_Percentage,
    World_Share,
    Total_Area_KM,
    Total_Area_M,
    Land_Area_KM,
    Land_Area_M,
    Percentage_World_Mass,
    cleaned_4.kids,
    cleaned_4.adults,
    cleaned_4.retired
FROM 
    cleaned_1
JOIN 
    cleaned_2
ON 
    cleaned_1.Country_or_dependency = cleaned_2.Country_or_dependency
JOIN
    cleaned_4
ON
    cleaned_1.Country_or_dependency = cleaned_4.Country_or_dependency;
