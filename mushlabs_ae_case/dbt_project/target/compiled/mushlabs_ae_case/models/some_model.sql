-- placeholder model so dagster can load.
with customer_orders as (
    select
        customer_id,
        min(order_date) as first_order_date,
        max(order_date) as most_recent_order_date,
        count(order_id) as number_of_orders

    from mushlabs_ae_case.orders

    group by 1
)

select
    some_model.customer_id,
    some_model.first_name,
    some_model.last_name,
    customer_orders.first_order_date,
    customer_orders.most_recent_order_date,
    coalesce(customer_orders.number_of_orders, 0) as number_of_orders

from mushlabs_ae_case.customers

left join customer_orders using (customer_id)