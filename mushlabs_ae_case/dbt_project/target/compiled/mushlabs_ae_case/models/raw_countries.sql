With genders as(
    select 
        Value,
        Dim1
    from core.raw_gho_gender_inequality
    group by Value,Dim1
)

select 
    genders.Value,
    genders.DIm1,
    raw_gho_countires.TimeDim,
    raw_gho_countires.SpatialDim

from core.raw_gho_countires  

cross join genders

Where raw_gho_countries.SpatialDim = 'HTI'