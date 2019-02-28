#python2.7
import json
import urllib

def get(itemid):
    url=("http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=" + str(itemid))
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price= makeint(data['item']['current']['price'])
    return price

def profit(ore_price, ore_ammount, coal_price, coal_ammount,stam,out):
    cost = ore_price * ore_ammount + coal_price * coal_ammount + stam*7.5 +72000
    revenue = ore_ammount*out
    profit = revenue - cost
    
    print("Cost: " + str(cost) + "\nRevenue: " + str(revenue) + "\nProfit: " +str(profit))


def makeint(price):
    try:
        return int(price)
    except:
        try:
            return int(price.replace(',',''))
        except:
            try:                 
                return int(float(price.replace('k','')) * 1000)
            except:
                try:
                    return int(float(price.replace('m','')) * 1000000)
                except:
                    print("Error converting price to int: " + price)
            
    

iron_ore=get(440)
mith_ore=get(447)
adam_ore=get(449) #has comma
rune_ore=get(451) #price is returned as a string, need try/catch/strip/convert
coal= get(453)

stel_bar=get(2353)
mith_bar=get(2359)
adam_bar=get(2361) #has comma 
rune_bar=get(2363) #price has a k, same as ore.

stam_pot= get(12625) #comes back as string with comma


print("Smithing steel bars")
profit(iron_ore, 4600, coal, 4600,stam_pot, stel_bar) 
print("Smithing xp: 70000\n\n")

print("Smithing mithril bars")
profit(mith_ore, 3000, coal, 6000, stam_pot, mith_bar) 
print("Smithing xp: 90000\n\n")

print("Smithing adamantite bars")
profit(adam_ore, 2300, coal, 6900, stam_pot, adam_bar)
print("Smithing xp: 86250\n\n")

print("Smithing rune bars")
profit(rune_ore, 1600, coal, 6400, stam_pot, rune_bar)
print("Smithing xp: 80000\n\n")

