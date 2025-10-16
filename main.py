from pyscript import display

store_name = 'Reverie Patisserie Boutique'
owner_name = 'Frances Hailey A. Jamet'
year_established = 2025
has_delivery = True
popular_items = ['Chocolate Sweet Printed Dress', 'Tier Layered Ruffle Miniskirt', 'Bisqcuit Bear Bag']
product_names = ['Melon Pan Beret', 'Wafer Hairclips', 'Strawberry Shortcake Mary Janes' ]
business_hours = ('11:00AM - 10:30 PM')
product_prices = [1599.00, 899.00, 677.00,350.00, 199.00, 1299.00]
product_stock = [5, 10, 3]
tax_rate = 0.12


display("Item Selection", target = 'mip',)

display(f'{popular_items[0]}', target = 'the')
display(f'{popular_items[1]}', target = 'the')
display(f'{popular_items[2]}', target = 'the')

display(f'{product_names[0]}', target = 'the')
display(f'{product_names[1]}', target = 'the') 
display(f'{product_names[2]}', target = 'the')

display("Prices (₱)", target = 'ay')


display(f'{product_prices[0]}', target = 'div3')
display(f'{product_prices[1]}', target = 'div3')
display(f'{product_prices[2]}', target = 'div3')

display(f'{product_prices[3]}', target = 'div3')
display(f'{product_prices[4]}', target = 'div3')
display(f'{product_prices[5]}', target = 'div3')


display(f'{business_hours}', target = 'div4')
if has_delivery:
    display('We offer delivery services!', target = 'div4')