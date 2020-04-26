#!/usr/bin/env python
# coding: utf-8

# In[118]:


def get_living_cardinals():

    import pandas as pd, numpy as np
    from feature_engineering import del_pope, del_index

    # Get the list of current cardinals

    url_cardinals = "https://en.wikipedia.org/wiki/List_of_living_cardinals"
    living_cardinals = pd.read_html(url_cardinals, parse_dates = True)[0]

    # Remove cardinals who already are over 80 years old - they are marked with '*'

    living_cardinals.drop(living_cardinals[living_cardinals.iloc[:,1].str.strip().str[-1] == "*"].index, inplace=True)

    # Remove not necessary columns

    living_cardinals = living_cardinals.drop(['No.', 'Ref.'], axis = 1).reset_index(drop=True)

    # Obtain date of birth

    living_cardinals['Born'] = living_cardinals['Born'].str[:-8]

    # Apply deleting popes' names

    living_cardinals['Consistory'] = living_cardinals['Consistory'].apply(lambda x: del_pope(x))

    # Apply deleting redundant indices

    living_cardinals['Consistory'] = living_cardinals['Consistory'].apply(lambda x: del_index(x))

    # Apply deleting 'latin' encoding to 'Born', 'Name' and 'Office' variables
    
    # Function to delete 'latin' encoded spaces from given variable

    def delete_latin_encoding(x):
        if x.find("\xa0") != -1:
            return x.replace("\xa0", " ")
        else:
            return x

    living_cardinals['Born'] = living_cardinals['Born'].apply(lambda x: delete_latin_encoding(x))
    living_cardinals['Name'] = living_cardinals['Name'].apply(lambda x: delete_latin_encoding(x))
    living_cardinals['Office'] = living_cardinals['Office'].apply(lambda x: delete_latin_encoding(x))

    pd.set_option('display.max_rows', 500)

    # Day and month of birth of Archbishop of Nairobi is unknown. hence it was set to 1st January

    living_cardinals.loc[living_cardinals['Name'] == 'John Njue', "Born"] = '1 January 1944'

    # Convert 'Born' variable to data format

    living_cardinals['Born'] = pd.to_datetime(living_cardinals['Born'], format = "%d %B %Y")

    # Convert 'Consistory' variable to data format

    living_cardinals['Consistory'] = pd.to_datetime(living_cardinals['Consistory'], format = "%d %B %Y")

    # Get dummie variables of cardinals' ranks (Bishop, Priest, Deacon)

    living_cardinals = pd.concat([living_cardinals.drop('Order', 1), pd.get_dummies(living_cardinals['Order'])], axis = 1)

    # Get binary variable - Italian or not

    living_cardinals['Italian'] = living_cardinals['Country'].apply(lambda x: 1 if x == 'Italy' else 0)

    # Transform 'Office' variable into cardinal's offices: Archbishop, Prefect or Other Vatican curia post

    living_cardinals['Office_add'] = living_cardinals['Office'].apply(lambda x: 'Archbishop' if (x.split()[0] == 'Archbishop' or x.split()[0] == 'Bishop' or x.split()[0] == 'Patriarch' or x.split()[1] == 'Archbishop' or x.split()[1] == 'Bishop') else 'Prefect' if x.split()[0] == 'Prefect' else 'Other curia')

    # Get binary checking whether cardinal is an emeritus

    living_cardinals['Emeritus'] = living_cardinals['Office'].apply(lambda x: 1 if x.split()[1] == 'emeritus' else 0)

    # Get dummy variables of cardinals offices and drop unnecessary columns

    living_cardinals = pd.concat([living_cardinals.drop(['Country', 'Office_add', 'Office'], 1), pd.get_dummies(living_cardinals['Office_add'])], axis=1)

    return living_cardinals


# In[119]:


get_living_cardinals()


# In[ ]:





# In[ ]:




