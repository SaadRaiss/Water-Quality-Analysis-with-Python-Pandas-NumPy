#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[2]:


import pandas as pd
df = pd.read_excel('WaterQuality.xlsx')
df.head()


# In[7]:


import pandas as pd   #question1
df = pd.read_excel ('WaterQuality.xlsx')  #read file excel

df.head(18)


# In[32]:


type(df)


# In[46]:


import pandas as pd
df = pd.read_excel ('WaterQuality.xlsx')     #Importation du fichier excel

df.head(18)

  #question 2
#calculer WAWQI
def wqi_1pH(Ci, wi):                   #Water Quality Index
    SI = (wi/12)*((Ci-8.5)/(6.5-8.5))
    return SI

par1 =wqi_1pH(df.pH,4)                    #Calculer pH pour le parametre pH

def wqi_1(Ci,wi,SI):      
    Wi=wi/45              # Si=Wi*Qi 
    m = Wi*((Ci/SI)*100)  #Qi=(Ci/SI)*100
    return m 


par2 = wqi_1(df.loc[:,'T°C'],1,30)        #les autres indices
par3 = wqi_1(df.DCO,3,90)
par4 = wqi_1(df.DBO5,4,3)
par5 = wqi_1(df.loc[:,'O2 DISSOUS'],5,5)
par6 = wqi_1(df.CONDUCTIVITE,4,1000)
par7 = wqi_1(df.MES,2,20)
par8 = wqi_1(df.TURBIDITE,2,5)
par9 = wqi_1(df.NITRITE,5,0.50)
par10 = wqi_1(df.NITRATE,5,50)
par11 = wqi_1(df.AMMONIUM,5,0.50)
par12 = wqi_1(df.PHOSPHATE,5,5)
#afficher les valeurs de SI
df['SI_ph']=par1          
df['SI_temp']=par2
df['SI_dco']=par3
df['SI_dbo5']=par4
df['SI_o2']=par5
df['SI_conductivite']=par6
df['SI_mes']=par7
df['SI_turbidite']=par8
df['SI_nitrite']=par9
df['SI_nitrate']=par10
df['SI_ammonium']=par11
df['SI_phosphate']=par12

SII = df.iloc[ : ,15: ]    #afficher les valeurs de WAWQI pour chaque point
d= SII.sum(axis=1)     
df["WAWQI"] = d
print(df)         

#question  3 
def QualiteWAWQI(WAWQI) :      #les conditions
        if WAWQI <50 :         
            Y="Excellent"
        elif WAWQI >=50 and WAWQI <=100 :
            Y="Good"
        elif WAWQI >=101 and WAWQI <=200:
            Y="Poor"
        elif WAWQI >=201 and WAWQI <=300 :
            Y="Very Poor"
        else:
            Y= "Unsuitable for drinking"
        return Y


df["QualiteWAWQI"] = df["WAWQI"].apply(QualiteWAWQI)
print(df) #afficher quality


# In[29]:


df3= pd.read_excel('WaterQuality.xlsx') #le parametre FC
col=df3.columns
df3=df3[[col[i] for i in [0,1,6,7,9,13,14]]]
col=df3.columns
df3.head()


# In[1]:


#question 4
import pandas as pd 
df1 = pd.read_excel('WaterQuality.xlsx') #Importer le fichier excel
df1 


# In[56]:


# question 5 /6
import numpy as np
import pandas as pd
df1 = pd.read_excel ('WaterQuality.xlsx')

def wti_1pH(ci,wi):
    s = np.float_power((wi/12), ((ci-8.5)/(6.5-8.5)))
    return s 
def wti_1(ci, wi, si):
    m = np.float_power((ci/si)*100, wi/45)
    return m

par1 = wti_1pH(df1.loc[ 0, "pH"], 4)
par2 = wti_1(df1.loc[:,'T°C'],1,30)
par3 = wti_1(df1.DCO ,3 ,90)
par4 = wti_1(df1.DBO5, 4, 3)
par5 = wti_1(df1.loc[:,'O2 DISSOUS'], 5, 5)
par6 = wti_1(df1.CONDUCTIVITE, 4, 1000)
par7 = wti_1(df1.MES, 2, 20)
par8 = wti_1(df1.TURBIDITE, 2, 5)
par9 = wti_1(df1.NITRITE, 5, 0.50)
par10 = wti_1(df1.NITRATE, 5, 50)
par11 = wti_1(df1.AMMONIUM, 5, 0.50)
par12 = wti_1(df1.PHOSPHATE, 5, 5)

df1['si_pH']=par1
df1['si_temp']=par2
df1['si_dco']=par3
df1['si_dbo5']=par4
df1['si_o2']=par5
df1['si_conductivite']=par6
df1['si_mes']=par7
df1['si_turbidite']=par8
df1['si_nitrite']=par9
df1['si_nitrate']=par10
df1['si_ammonium']=par11
df1['si_phosphate']=par12

g = df1.iloc[:,15:]
df1["WGWQI"] = g.prod(axis=1)


def QualiteWGWQI(WGWQI):
      # Interprétation des résultats :
        T=''
        if WGWQI <= 100 and WGWQI >= 90:
            T="Excellent "
        elif WGWQI >= 70 and WGWQI <= 89:
            T="Good "
        elif WGWQI >= 50 and WGWQI <= 69 :
            T="Medium "
        elif WGWQI >= 25 and WGWQI <= 49 :
            T= "Bad "
        elif WGWQI >= 0 and WGWQI <= 24:
            T= "Very bad "
        return T

df1["QualiteWGWQI"] = df1["WGWQI"].apply(QualiteWGWQI)
print(df1) # afficher la qualite


# In[49]:


#questin 7
import numpy as np
df2 = pd.read_excel('WaterQuality.xlsx') #read file excel
col=df2.columns
df2=df2[[col[i]for i in [0,1,2,3,5,6,11,12,13,14]]]
#print(df2[col[0]])
col=df2.columns
#print(col)
df2.head()
SiOthers=np.array([30,3,3,30,0.5,5,594]) 
#print(SiOthers)
wi= np.array([4,1,4,5,5,5,5,5])
#print(wi)
Wi= np.array([a/np.sum(wi) for a in wi])
#print(Wi)
ph =df2[col[2]]
#
qiph= (ph - 8.5)/(6.5-8.5)
qiOthers = (df2[col[3::]]/SiOthers)*100
frames=[qiph,qiOthers]
Qi=pd.concat(frames , axis=1)
SI=1/pow(Qi*Wi,2)
WQI=pow(8/SI.sum(axis=1),0.5) #une autre methode(sqrt)
frames1 = [df2,WQI]
df2=pd.concat(frames1,axis=1)
df2 = df2.rename(columns={df2.columns[-1]: 'OWQI'})
print(df2)#afficher les valeurs de OWQI
Quality = np.zeros((18,1))
Quality = pd.DataFrame(Quality, columns =['Quality'])
frames2 = [df2,Quality]
df2 = pd.concat(frames2 , axis=1)
cols=df2.columns

for i in range (df2[cols[-1]].size):#les conditions
    if (((df2.iloc[i,-2]) >=0) and ((df2.iloc[i,-2]) <=59)):
        #print(df2.iloc[1,-2])
        df2.iloc[i,-1] = "VeryPoor"
    elif (df2.iloc[i,-2] <= 79):
        df2.iloc[i,-1]= "Poor"
    elif (df2.iloc[i,-2] <= 84):
        df2.iloc[i,-1] = "Fair"
    elif (df2.iloc[i,-2] <= 89):
        df2.iloc[i,-1] = "Good"
    elif (df2.iloc[i,-2] <= 100):
        df2.iloc[i,-1] = "ExceLent"
    else:
        df2.iloc[i,-1] = "Outside"
print(df2)#afficher quality
        


# In[65]:


df2 = pd.read_excel('WaterQuality.xlsx')
col=df2.columns
df2=df2[[col[i] for i in [0,1,2,3,5,6,11,12,13,14]]]
col=df2.columns
df2.head()


import pandas as pd
df = pd.read_excel ('WaterQuality.xlsx')

df3 = pd.read_excel('WaterQuality.xlsx')
col=df3.columns
df3=df3[[col[i] for i in [0,1,6,7,9,13,14]]]
col=df3.columns
df3.head()


df.head(18)

def wqi_1pH(c, w):
    s = (w/12)*((c-8.5)/(6.5-8.5))
    return s 

def wqi_1(c, w, s):
    m = (w/12)*(c/s)*100
    return m

par1 = wqi_1pH(df.loc[ 0, "pH"], 4)
par2 = wqi_1(df.loc[:,'T°C'],1,30)
par3 = wqi_1(df.DCO ,3 ,90)
par4 = wqi_1(df.DBO5, 4, 3)
par5 = wqi_1(df.loc[:,'O2 DISSOUS'], 5, 5)
par6 = wqi_1(df.CONDUCTIVITE, 4, 1000)
par7 = wqi_1(df.MES, 2, 20)
par8 = wqi_1(df.TURBIDITE, 2, 5)
par9 = wqi_1(df.NITRITE, 5, 0.50)
par10 = wqi_1(df.NITRATE, 5, 50)
par11 = wqi_1(df.AMMONIUM, 5, 0.50)
par12 = wqi_1(df.PHOSPHATE, 5, 5)

df['si_pH']=par1
df['si_temp']=par2
df['si_dco']=par3
df['si_dbo5']=par4
df['si_o2']=par5
df['si_conductivite']=par6
df['si_mes']=par7
df['si_turbidite']=par8
df['si_nitrite']=par9
df['si_nitrate']=par10
df['si_ammonium']=par11
df['si_phosphate']=par12

SII = df.iloc[ : ,15: ]
d= SII.sum(axis=1)
df["WAWQI"] = d
print(df)

#question 3
def QualiteWAWQI(WAWQI):
        if WAWQI <50:         
            Y="Excellent"
        elif WAWQI >=50 and WAWQI <=100:
            Y="Good"
        elif WAWQI >=101 and WAWQI <=200:
            Y="Poor"
        elif WAWQI >=201 and WAWQI <=300 :
            Y="Very Poor"
        else:
            Y= "Unsuitable for drinking"
        return Y
        
        
df["QualiteWAWQI"] = df["WAWQI"].apply(QualiteWAWQI)
print(df)

# question 7
import numpy as np
df2 = pd.read_excel('WaterQuality.xlsx')#read file excel
col=df2.columns
df2=df2[[col[i]for i in [0,1,2,3,5,6,11,12,13,14]]]
#print(df2[col[0]])
col=df2.columns
#print(col)
df2.head()
SiOthers=np.array([30,3,3,30,0.5,5,594]) # si = [30]
#print(SiOthers)
wi= np.array([4,1,4,5,5,5,5,5])
#print(wi)
Wi= np.array([a/np.sum(wi) for a in wi])
#print(Wi)
ph =df2[col[2]]
#
qiph= (ph - 8.5)/(6.5-8.5)
qiOthers = (df2[col[3::]]/SiOthers)*100
frames=[qiph,qiOthers]
Qi=pd.concat(frames , axis=1)
SI=1/np.float_power(Qi*Wi,2)
WQI=np.float_power(8/SI.sum(axis=1),0.5) #une autre methode(sqrt)
frames1 = [df2,WQI]
df2=pd.concat(frames1,axis=1)
df2 = df2.rename(columns={df2.columns[-1]: 'OWQI'})
print(df2)#afficher les valeurs de OWQI
Quality = np.zeros((18,1))
Quality = pd.DataFrame(Quality, columns =['Quality'])
frames2 = [df2,Quality]
df2 = pd.concat(frames2 , axis=1)
cols=df2.columns

for i in range (df2[cols[-1]].size):#les conditions
    if (((df2.iloc[i,-2]) >=0) and ((df2.iloc[i,-2]) <=59)):
        #print(df2.iloc[1,-2])
        df2.iloc[i,-1] = "VeryPoor"
    elif (df2.iloc[i,-2] <= 79):
        df2.iloc[i,-1]= "Poor"
    elif (df2.iloc[i,-2] <= 84):
        df2.iloc[i,-1] = "Fair"
    elif (df2.iloc[i,-2] <= 89):
        df2.iloc[i,-1] = "Good"
    elif (df2.iloc[i,-2] <= 100):
        df2.iloc[i,-1] = "ExceLent"
    else:
        df2.iloc[i,-1] = "Outside"
print(df2)


# questions 5 et 6
import numpy as np  # impportation des commandes
import pandas as pd  # impportation des commandes
df1 = pd.read_excel ('WaterQuality.xlsx')#read file excel

def wti_1pH(ci,wi):
    s = np.float_power((wi/12), ((ci-8.5)/(6.5-8.5)))
    return s 
def wti_1(ci, wi, si):
    m = np.float_power((ci/si)*100, wi/45)
    return m

par1 = wti_1pH(df1.loc[ 0, "pH"], 4)
par2 = wti_1(df1.loc[:,'T°C'],1,30)
par3 = wti_1(df1.DCO ,3 ,90)
par4 = wti_1(df1.DBO5, 4, 3)
par5 = wti_1(df1.loc[:,'O2 DISSOUS'], 5, 5)
par6 = wti_1(df1.CONDUCTIVITE, 4, 1000)
par7 = wti_1(df1.MES, 2, 20)
par8 = wti_1(df1.TURBIDITE, 2, 5)
par9 = wti_1(df1.NITRITE, 5, 0.50)
par10 = wti_1(df1.NITRATE, 5, 50)
par11 = wti_1(df1.AMMONIUM, 5, 0.50)
par12 = wti_1(df1.PHOSPHATE, 5, 5)

df1['si_pH']=par1
df1['si_temp']=par2
df1['si_dco']=par3
df1['si_dbo5']=par4
df1['si_o2']=par5
df1['si_conductivite']=par6
df1['si_mes']=par7
df1['si_turbidite']=par8
df1['si_nitrite']=par9
df1['si_nitrate']=par10
df1['si_ammonium']=par11
df1['si_phosphate']=par12

g = df1.iloc[:,15:]
df1["WGWQI"] = g.prod(axis=1)
#afficher les valeurs de WGWQI

def QualiteWGWQI(WGWQI):
      # Interprétation des résultats :
        T=''
        if WGWQI <= 100 and WGWQI >= 90:
            T="Excellent "
        elif WGWQI >= 70 and WGWQI <= 89:
            T="Good "
        elif WGWQI >= 50 and WGWQI <= 69 :
            T="Medium "
        elif WGWQI >= 25 and WGWQI <= 49 :
            T= "Bad "
        elif WGWQI >= 0 and WGWQI <= 24:
            T= "Very bad "
        return T

df1["QualiteWGWQI"] = df1["WGWQI"].apply(QualiteWGWQI)
print(df1)
#  afficher la QualiteWGWQI

#questin 7
import numpy as np
df2 = pd.read_excel('WaterQuality.xlsx') #read file excel
col=df2.columns
df2=df2[[col[i]for i in [0,1,2,3,5,6,11,12,13,14]]]
#print(df2[col[0]])
col=df2.columns
#print(col)
df2.head()
SiOthers=np.array([30,3,3,30,0.5,5,594]) 
#print(SiOthers)
wi= np.array([4,1,4,5,5,5,5,5])
#print(wi)
Wi= np.array([a/np.sum(wi) for a in wi])
#print(Wi)
ph =df2[col[2]]
#
qiph= (ph - 8.5)/(6.5-8.5)
qiOthers = (df2[col[3::]]/SiOthers)*100
frames=[qiph,qiOthers]
Qi=pd.concat(frames , axis=1)
SI=1/np.float_power(Qi*Wi,2)
WQI=np.float_power(8/SI.sum(axis=1),0.5) #une autre methode(sqrt)
frames1 = [df2,WQI]
df2=pd.concat(frames1,axis=1)
df2 = df2.rename(columns={df2.columns[-1]: 'OWQI'})
print(df2)#afficher les valeurs de OWQI
Quality = np.zeros((18,1))
Quality = pd.DataFrame(Quality, columns =['Quality'])
frames2 = [df2,Quality]
df2 = pd.concat(frames2 , axis=1)
cols=df2.columns

for i in range (df2[cols[-1]].size):#les conditions
    if (((df2.iloc[i,-2]) >=0) and ((df2.iloc[i,-2]) <=59)):
        #print(df2.iloc[1,-2])
        df2.iloc[i,-1] = "VeryPoor"
    elif (df2.iloc[i,-2] <= 79):
        df2.iloc[i,-1]= "Poor"
    elif (df2.iloc[i,-2] <= 84):
        df2.iloc[i,-1] = "Fair"
    elif (df2.iloc[i,-2] <= 89):
        df2.iloc[i,-1] = "Good"
    elif (df2.iloc[i,-2] <= 100):
        df2.iloc[i,-1] = "ExceLent"
    else:
        df2.iloc[i,-1] = "Outside"
print(df2)#afficher quality

# Question 10

df4 = pd.DataFrame()

df4["Year"]=df.Year
df4["POINTS"]=df.POINTS
df4["WAWQI"]=df.WAWQI
df4["QualiteWAWQI"]=df.QualiteWAWQI
df4["WGWQI"]=df1.WGWQI
df4["QualiteWGWQI"]=df1.QualiteWGWQI
df4["OWQI"]=df2.OWQI
df4["QualiteOWQI"]=df2.Quality


 
print(df)    #afficher year and points        
print(df1)   #afficher WAWQI and QualiteWAWQI
print(df2)   #afficher WGWQI    QualiteWGWQI
print(df4)   #afficher OWQI     QualiteOWQI


# In[ ]:




