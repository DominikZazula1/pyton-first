from . import produts

basket = []


def add_to_list(name, qauntity):
    if name in produts.name:
       index = produts.name.index(name)
       if qauntity <= produts.quantity[index]:
          cost = produts.amount[index] * qauntity
          basket.append([name,qauntity,cost])
          produts.quantity[index] -= qauntity
          print("produkt dodany do koszyka")
       else: print("nie ma takej ilosci w zaopatrzeniu")
    else: print("nie ma takiego produktu")

