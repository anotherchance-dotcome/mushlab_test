
  create view "core"."raw_gender_inequality__dbt_tmp" as (
    select * from dbt_project.core.raw_gender_inequality
  );
