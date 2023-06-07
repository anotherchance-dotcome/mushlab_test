With gender_inequlity as(
    select 
        Value as nums_of_people,
        Dim1 as gender

    from {{ source('core', 'raw_gho_gender_inequality') }}
)
select
    gender,
    sum(nums_of_people) as sum_Female
from gender_inequlity
where gender = 'FMLE'
group by gender