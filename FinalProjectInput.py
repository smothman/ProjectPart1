# Name:
# ID:




import pandas as pd 
# Important Libraries that is used to read the csv files and manuplulations





MANF=pd.read_csv("ManufacturerList.csv",header=None)
# Reading the ManufacturerList file





PRCL=pd.read_csv("PriceList.csv",header=None)
## Read the price list file




SDL=pd.read_csv("ServiceDatesList.csv",header=None)
## Read the ServiceDatesList file





MANF.columns=['item ID','manufacturer name', 'item type','optionally a damaged indicator']
## Column names so that we can combine files later



PRCL.columns=['item ID','the item price. ']
## Column names for price lists





SDL.columns=['item ID','servicedate']
## Column names for service dates


# ## FullInventory.csv -- all the items listed by row with all their information . 
# #### The items should be sorted alphabetically by manufacturer. Each row should contain item ID, manufacturer name, item type, price, service date, and list if it is damaged. The item attributes must appear in this order.



COMBINE=pd.merge(pd.merge(MANF,PRCL,on='item ID'),SDL,on='item ID')
## Combining dates based on items ID





COMBINE=COMBINE.sort_values("item type")
## The item attributes must appear in this order.


# In[10]:


COMBINE=COMBINE.sort_values("manufacturer name").reset_index(drop=True)
## The items should be sorted alphabetically by manufacturer. 




COMBINE=COMBINE[['item ID','manufacturer name','item type','the item price. ','servicedate','optionally a damaged indicator']]
## Each row should contain item ID, manufacturer name, item type, price, service date, and list if it is damaged. 





COMBINE.to_csv("FinalProject_FullInventory.csv",header=None,index=False)
## d name your files with the starting phrase “FinalProject”


# ## Item type Inventory list, i.e LaptopInventory.csv -- 
# #### there should be a file for each item type and the item type needs to be in the file name. Each row of the file should contain item ID, manufacturer name, price, service date, and list if it is damaged. The items should be sorted by their item ID. 
# 




COMBINE['item type'].unique()
## unique item types



COMBINE=COMBINE.sort_values("item ID")
## The items should be sorted by their item ID.





PHONE=COMBINE[COMBINE['item type']=='phone']
## there should be a file for each item type phone




PHONE=PHONE[['item ID','manufacturer name','the item price. ','servicedate','optionally a damaged indicator']]
## Each row of the file should contain item ID, manufacturer name, price, service date, and list if it is damaged.




PHONE.to_csv("FinalProject_LaptopInventory_phone.csv",header=None,index=False)
##  the item type needs to be in the file name





laptop=COMBINE[COMBINE['item type']=='laptop']
## ## there should be a file for each item type laptop
laptop=laptop[['item ID','manufacturer name','the item price. ','servicedate','optionally a damaged indicator']]
## Each row of the file should contain item ID, manufacturer name, price, service date, and list if it is damaged.
laptop.to_csv("FinalProject_LaptopInventory_laptop.csv",header=None,index=False)
##  the item type needs to be in the file name





tower=COMBINE[COMBINE['item type']=='tower']
## ## there should be a file for each item type tower
tower=tower[['item ID','manufacturer name','the item price. ','servicedate','optionally a damaged indicator']]
## Each row of the file should contain item ID, manufacturer name, price, service date, and list if it is damaged.
tower.to_csv("FinalProject_towerInventory_tower.csv",header=None,index=False)
##  the item type needs to be in the file name


# ## PastServiceDateInventory.csv – all the items that are past the service date on the day the program is actually executed.
# #### Each row should contain: item ID, manufacturer name, item type, price, service date, and list if it is damaged. The items must appear in the order of service date from oldest to most recent. 
# 




COMBINE['servicedate']=pd.to_datetime(COMBINE['servicedate'])
## datetime needed so we can compare with today




COMBINE=COMBINE.sort_values("servicedate")
## The items must appear in the order of service date from oldest to most recent.¶




import datetime
## to get today





past=COMBINE[COMBINE['servicedate']<datetime.datetime.today()]
## all the items that are past the service date on the day the program is actually executed





past.to_csv("FinalProject_PastServiceDateInventory.csv",header=None,index=False)
## saving the past data file


# ## DamagedInventory.csv –all items that are damaged. 
# 
# #### Each row should contain : item ID, manufacturer name, item type, price, and service date. The items must appear in the order of most expensive to least expensive. 



COMBINE=COMBINE.sort_values("the item price. ",ascending=False)
## The items must appear in the order of most expensive to least expensive.


# In[26]:


damage=COMBINE[COMBINE['optionally a damaged indicator']=='damaged']
## all items that are damaged.


# In[27]:


damage=damage[['item ID','manufacturer name','item type','the item price. ','servicedate']]
## Each row should contain : item ID, manufacturer name, item type, price, and service date




damage.to_csv("FinalProject_DamagedInventory.csv")
## saving the final file






