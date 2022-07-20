select * from insurance limit 10;

select count(*) from insurance;

describe insurance;

select age,charges, smoker, if (charges>20000.00, "high","low") as status
from insurance;

select smoker,
avg(age) as avg_age,
avg(bmi) as avg_bmi,
avg(charges) as avg_charges,
max(age) as max_age,
max(bmi) as max_bmi,
max(charges) as max_charges,
min(age) as min_age,
min(bmi) as min_bmi,
min(charges) as min_charges
from insurance;
group by smoker;

