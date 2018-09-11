#5.6.2小节
def displayInventory(inventory):
    print("Inventory:")
    item_total=0
    for k,v in inventory.items():
        print(v,k)
        item_total += v
    print('total number of items:'+ str(item_total))

def addToInventory(inventory,addedItems):
    a={}
    for i in addedItems:
        a.setdefault(i,0)
        a[i]=a[i]+1
    c=a
    for k,v in inventory.items():
        c[k]=v+c.get(k,0)
    return c

dragonLoot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv={'gold coin':42,'rope':1}        
inv=addToInventory(inv,dragonLoot)
displayInventory(inv)
