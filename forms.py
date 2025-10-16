from pyscript import display, document

def order(e): 
    item_1 = document.getElementById('check1').checked
    item_2 = document.getElementById('check2').checked
    item_3 = document.getElementById('check3').checked
    item_4 = document.getElementById('check4').checked
    item_5 = document.getElementById('check5').checked
    item_6 = document.getElementById('check6').checked
    cost = item_1*1599.00 + item_2*899.00 + item_3*677.00 + item_4*700.00 + item_5*350.00 + item_6*199.00
    ordered = item_1 + item_2 + item_3 + item_4 + item_5 + item_6
    name = document.getElementById('name').value
    address = document.getElementById('address').value
    contact = document.getElementById('contact').value
    display(f"Name: {name}", target="summ")
    display(f"Address: {address}", target="summ")
    display(f"Contact Number: {contact}", target="summ")
    display(f"Total Items Ordered: {ordered}", target="summ")
    display(f"Total Cost: {cost} PHP", target="summ")
    display("Thank you for ordering with us!", target="mio")
