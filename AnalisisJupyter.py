#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# # El dataset data viene con 28 columnas
# ### Siendo la 1ra timestamp y las otras 27 a analizar
# ### posteriormente se van a crear dos columnas al inicio con el fin de filtrar dias y horas más facilmente

# In[13]:


data = pd.read_csv(r'c:\Users\personal\Downloads\cs_db.csv',low_memory=False,delimiter=";")
lista = data.columns
data.dropna(subset= data.columns.difference(['timestamp']),thresh=1, inplace=True)
dataResume =  pd.read_csv(r'c:\Users\personal\Downloads\cs_db_2.csv',low_memory=False,delimiter="," )
data


# ### Funcion que añade dos columnas al inicio separando timestamp

# In[6]:


def hours( df ):
    new = df["timestamp"].str.split(" ", n = 1, expand = True)
    hours = new[1]
    date = new[0]
    df.insert(0,"DateHours", hours)
    df.insert(0,"Date", date)
hours(data)
hours(dataResume)


# ## ANALISIS DE TODO EL DATASET
# 
# ### Borro temporalmente las filas que tengan vacios en la columna a analizar 
# ### Datos a saber:
# - Se empieza a iterar desde la columna 3 porque desde esa empieza la información a analizar
# - Se está analizando cada variable con las horas del día, sin importar los días. 
#     Es como hacerse la pregunta **¿Que pasa a tal hora del dia?**
# - Se hace de a intervalos pequeños para que no se dañen las graficas
# - Hay variables que deben ser excluidas o analizadas de otra forma posteriormente

# In[7]:


for column in data.columns[3:10]:
    temp = data.dropna(subset=[column], inplace=False)
    temp = temp[temp[column]!= 0]
    temp = temp.sort_values("DateHours")
    px.scatter(temp, x="DateHours", y=column).show()


# In[8]:


for column in data.columns[10:17]:
    temp = data.dropna(subset=[column], inplace=False)
    temp = temp[temp[column]!= 0]
    temp = temp.sort_values("DateHours")
    px.scatter(temp, x="DateHours", y=column).show()


# In[9]:


for column in data.columns[17:24]:
    temp = data.dropna(subset=[column], inplace=False)
    temp = temp[temp[column]!= 0]
    temp = temp.sort_values("DateHours")
    px.scatter(temp, x="DateHours", y=column).show()


# In[10]:


for column in data.columns[24:30]:
    temp = data.dropna(subset=[column], inplace=False)
    temp = temp[temp[column]!= 0]
    temp = temp.sort_values("DateHours")
    px.scatter(temp, x="DateHours", y=column).show()


# ## El siguiente código grafica todas las variables por día específico

# ### No modificar el código de abajo

# El siguiente código permitirá graficar semanalmente algunas variables

# In[ ]:


# lista[0] es Date
for column in data.columns [3:]:
    count=0
    for j in data['Date'].unique():
        day = data[data['Date'] == j]       # filtra cada valor por una caracteristica, en este caso la fecha
        dayLen = len(day.dropna(subset = column, inplace=False))
        if dayLen >10: # Si hay más de 10 datos en la variable a analizar, entonces la grafica
            #px.scatter(day, x="DateHours", y=column).show()
             count+=1
    #print(f'La columna { column} tiene {count} dias de informacion')


# ### Comparación de resultados del__________________ de la batería

# In[187]:


differences = data.dropna(subset = ['Charge stateVE.Bus System [289].36', 'Charge stateSolar Charger [289].5', 'VE.Bus state'], inplace= False)
differences


# ## Comparación de resultados del estado de la carga de la batería

# ### Análisis sobre las mediciones del estado de carga , para verificar el por qué pasa eso.

# Tomamos las diferencias mayores o iguales a 0.5 para tener una diferencia de carga significativa.
# No sabemos por qué mide mal porque no hubo registro de más datos aparte del estado de carga
# 
# 

# #### Errores en mediciones

# In[18]:


stateCharge1 = data.dropna(subset=['Battery State of Charge'], inplace=False)
stateCharge2 = data.dropna(subset = ['VE.Bus state of charge'], inplace = False)
stateCharge3 = data.dropna(subset = ['State of charge'], inplace = False)

totalStateCharge = pd.concat([stateCharge1, stateCharge2,stateCharge3]).drop_duplicates()
totalStateCharge 
  
dif1 = totalStateCharge[ abs(totalStateCharge['State of charge'] - totalStateCharge['Battery State of Charge'])> 0.5]
dif2 = totalStateCharge[ abs(totalStateCharge['Battery State of Charge'] - totalStateCharge['VE.Bus state of charge'])> 0.5]
dif3 = totalStateCharge[ abs(totalStateCharge['State of charge'] - totalStateCharge['VE.Bus state of charge'])> 0.5]

dif = pd.concat([dif1,dif2,dif3]).drop_duplicates()
dif = dif.loc[:, ['timestamp','State of charge', 'Battery State of Charge', 'VE.Bus state of charge']]
dif                                     


# In[16]:


print(totalStateCharge)


# In[ ]:


totalCharge = 


# In[218]:



#px.scatter(totalStateCharge, y='State of charge', x='timestamp')
fig = px.scatter(totalStateCharge, x="Battery State of Charge")
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Comparar cada dia con lo que pasó

# In[ ]:


for i in range(3,6):
    temp = dataResume.dropna(0, subset=lista[i], inplace=False)
    temp = temp[temp[lista[i]]!= 0]
    plt.scatter(temp["DateHours"], temp[lista[i]])
    plt.xlabel("DateHours")
    plt.ylabel(lista[i])
    plt.plot()
    


# In[ ]:


# Voy a graficar por dias todas las variables
for j in range(len(data['Date'].unique()))
    usa = data[data[lista[0] == data[lista[0]][j]]
    #usa.columns = usa.columns.to_series().apply(lambda x: x.strip())
    plt.scatter(temp["DateHours"], temp[lista[i]])


# In[ ]:


for i in range(3,6):
    temp = dataResume.dropna(0, subset=lista[i], inplace=False)
    temp = temp[temp[lista[i]]!= 0]
    plt.scatter(temp["DateHours"], temp[lista[i]])
    plt.xlabel("DateHours")
    plt.ylabel(lista[i])
    plt.plot()


# ### saquemos algunos estadísticos para las variables que tuvieron un comportamiento más dinámico

# In[8]:


data['Input voltage phase 1'].plot(kind='density')
data['Input voltage phase 1'].describe()


# In[10]:


data['AC Consumption L1'].plot(kind='density')
data['AC Consumption L1'].describe()


# In[ ]:





# In[162]:





# In[ ]:





# 
