With country as(
    select 
        TimeDim,
        SpatialDim
    from core.raw_gho_countires
    group by TimeDim,SpatialDim
)

select 
    raw_gho_gender_inequality.Value, 
    raw_gho_gender_inequality.Dim1,
    country.TimeDim,
    country.SpatialDim

from core.raw_gho_gender_inequality  

cross join country

Where raw_gho_gender_inequality.Dim1 = 'FMLE'