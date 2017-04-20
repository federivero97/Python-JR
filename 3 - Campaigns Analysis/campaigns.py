import csv
def get_campaigns (filename):
    with open(filename) as csvfile:
        return list(csv.DictReader(csvfile))

def order_by_payout(filename):
    """
    Returns​ a list of campaigns ID​ 's, order by payout from highest to lowest.
    """
    campaigns = get_campaigns(filename)
    campaigns = sorted(campaigns, key=lambda item: item['payout'],reverse=True)
    ids = []
    for x in range(len(campaigns)):
        ids.append(int(campaigns[x]['id']))
    return ids

def order_by_total_payout(filename):
    """
    Returns​ a list of campaigns ID​ 's, order by total payout from highest to
    lowest.
    >>>​ total_payout ​ = ​ payout ​ * ​ installs
    """
    campaigns = get_campaigns(filename) 
    i=0
    s = ""
    for x in range(len(campaigns)):
        payout = campaigns[x]['payout']
        installs = campaigns[x]['installs']
        if "," in payout:                           #No puedo castear a float, ya que la cadena posee ",". Cambio coma por punto.
            i = payout.index(",")
            payout = payout[:i] + "." + payout[i+1:]
        if "," in installs:
            i = installs.index(",")
            installs = installs[:i] + "." + installs[i+1:]
        campaigns[x]['payout_total'] = float(payout)*int(installs)
    campaigns = sorted(campaigns, key=lambda item: item['payout_total'],reverse=True)
    ids = []
    for x in range(len(campaigns)):
        ids.append(int(campaigns[x]['id']))        
    return ids

def order_by_cr(filename):
    """
    Returns​ a list of campaigns ID​ 's, order by conversion rate (CR) from highest
    to lowest.
    >>>​ cr ​ = ​ impressions ​ / ​ installs
    """
    campaigns = get_campaigns(filename) 
    for x in range(len(campaigns)):
        impressions = campaigns[x]['impressions']
        installs = campaigns[x]['installs'] 
        campaigns[x]['cr'] = int(impressions)/int(installs)
    campaigns = sorted(campaigns, key=lambda item: item['cr'],reverse=True)
    ids = []
    for x in range(len(campaigns)):
        ids.append(int(campaigns[x]['id'])) 
    return ids

if __name__  == '__main__':
    payout_order = [17, 14, 22, 7, 11, 15, 23, 13, 18, 12, 6, 1, 3, 10, 25, 24, 21, 16, 20, 5, 4, 8, 9, 19, 2]
    total_payout_order = [15, 11, 18, 7, 14, 21, 3, 6, 25, 13, 16, 5, 24, 20, 17, 23, 1, 10, 8, 9, 19, 12, 4, 22, 2]
    cr_order  = [11, 15, 18, 25, 21, 7, 8, 24, 6, 14, 3, 9, 5, 16, 19, 10, 20, 2, 13, 4, 17, 1, 23, 12, 22]
    cr_order.reverse() # Estaba ordenado al reves.
    assert order_by_payout('campaigns.csv') == payout_order
    assert order_by_total_payout('campaigns.csv') == total_payout_order
    assert order_by_cr('campaigns.csv') == cr_order 