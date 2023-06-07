With country_data as(
    select 
        raw_gho_gender_inequality.Value as number_of_people,
        TimeDim as year,
        SpatialDim as country

    from {{ source('core', 'raw_gho_countries') }} 
    cross join {{ source('core', 'raw_gho_gender_inequality') }}
)

select 
    country,
    count(nums_of_people) as country_total
from country_data
group by country
order by country_total desc
Limit 15
