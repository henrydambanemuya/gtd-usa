# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 12:35:41 2017
Wrapper functions for GTD Notebook
@author: Henry K. Dambanemuya
"""
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from collections import Counter, OrderedDict

data = pd.read_excel('../GTD/globalterrorismdb_0617dist.xlsx')
years = list(range(2001,2017))
global_data = data.loc[data['iyear'] >= 2001]
us_internal_data = global_data.loc[global_data['country_txt'] == 'United States'].loc[global_data['iyear'] >= 2001]
us_external_data = pd.concat([global_data.loc[global_data['country_txt'] != 'United States'].loc[global_data['natlty1_txt'] == 'United States'],
                              global_data.loc[global_data['country_txt'] != 'United States'].loc[global_data['natlty1_txt'] != 'United States'].loc[global_data['natlty2_txt'] == 'United States'],
                              global_data.loc[global_data['country_txt'] != 'United States'].loc[global_data['natlty1_txt'] != 'United States'].loc[global_data['natlty2_txt'] != 'United States'].loc[global_data['natlty3_txt'] == 'United States']
                              ])
                              
al_qaida, al_qaida_iraq, al_qaida_lebanon, al_qaida_sa, al_qaida_yemen, aqap, aqim, europe, sweden, indian, sympathizer  = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
isi, bangladesh, mei, isil, jerusalem, mosques = {}, {}, {}, {}, {}, {}

def Bar(counter_param, title='', ylabel='', xlabel='', rotation=0):
    print(counter_param)
    labels = list(counter_param.keys())
    values = list(counter_param.values())
    ind = np.arange(0, len(labels), 1)
    fig, ax = plt.subplots(figsize=(18,8))
    ax.set_title(title, fontsize=15, fontweight='bold')
    ax.set_ylabel(ylabel , fontsize=15)
    ax.set_xlabel(xlabel, fontsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    plt.bar(ind, values, align='center')
    ax.set_xticks(ind)
    ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=rotation)
    ax.set_xticklabels(labels[::1])
    plt.show()
    
def Box(values, title='', ylabel='', xlabel=''):
    fig, ax = plt.subplots()
    ax.set_title(title, fontsize=15, fontweight='bold')
    ax.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.set_xlabel(xlabel, fontsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.boxplot(values)
    plt.show()
    
    
def Histogram(values, title='', ylabel='', xlabel=''):
    fig, ax = plt.subplots()
    ax.set_title('', fontsize=15, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=15)
    ax.set_xlabel(xlabel, fontsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.hist(values, bins=100, range=(0,max(values)/6), histtype='bar', align='mid', orientation='vertical')
    plt.show()
    
def pieChart():
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18,6))
    labels1= list(OrderedDict(sorted(Counter(global_data.attacktype1_txt).items(), key=lambda x: x[1], reverse=True)).keys())
    sizes1 = list(OrderedDict(sorted(Counter(global_data.attacktype1_txt).items(), key=lambda x: x[1], reverse=True)).values())
    patches1, texts1 = ax1.pie(sizes1, colors=cm.Set3(np.linspace(0, 1, len(sizes1))), startangle=90)
    ax1.legend(patches1, labels1, loc="right", fontsize=14)
    ax1.set_title('Global', fontsize=15, fontweight='bold')
    labels2= list(OrderedDict(sorted(Counter(us_internal_data.attacktype1_txt).items(), key=lambda x: x[1], reverse=True)).keys())
    sizes2 = list(OrderedDict(sorted(Counter(us_internal_data.attacktype1_txt).items(), key=lambda x: x[1], reverse=True)).values())
    patches2, texts2 = ax2.pie(sizes2, colors=cm.Set3(np.linspace(0, 1, len(sizes2))), startangle=90)
    ax2.legend(patches2, labels2, loc="right", fontsize=14)
    ax2.set_title('Internal', fontsize=15, fontweight='bold')
    labels3= list(OrderedDict(sorted(Counter(us_external_data.attacktype1_txt).items(), key=lambda x: x[1], reverse=True)).keys())
    sizes3 = list(OrderedDict(sorted(Counter(us_external_data.attacktype1_txt).items(), key=lambda x: x[1], reverse=True)).values())
    patches3, texts3 = ax3.pie(sizes3, colors=cm.Set3(np.linspace(0, 1, len(sizes2))), startangle=90)
    ax3.legend(patches2, labels3, loc="right", fontsize=14)
    ax3.set_title('External', fontsize=15, fontweight='bold')
                       
def globalTrends():
    fig, ax = plt.subplots(figsize=(18, 8))
    labels = sorted(Counter(us_external_data.iyear).keys())
    ind = np.arange(0, len(labels), 1)
    ax.set_title('Global Terrorism Trends', fontsize=15, fontweight='bold')
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.set_xlabel('', fontsize=15)
    ax.set_ylabel('Attacks' , fontsize=15)
    ax.set_xticks(np.arange(0, len(labels), 1))
    ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=270)
    ax.set_xticklabels(labels[::1])
    ax.set_yscale('log')
    plt.plot(ind, list(Counter(us_external_data.iyear).values()), label='External', c='g')
    plt.plot(ind, list(Counter(global_data.iyear).values()), label='Global', c='r')
    plt.plot(ind, list(Counter(us_internal_data.iyear).values()), label='Internal')
    plt.legend(loc='best', fontsize=15)
    plt.show()
                       
def alQaidaTrends():
    fig, ax = plt.subplots(figsize=(18, 8))
    labels = years
    ind = np.arange(0, len(labels), 1)
    ax.set_title('Al-Qaida Global Activity', fontsize=15, fontweight='bold')
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.set_xlabel('', fontsize=15)
    ax.set_ylabel('Attacks' , fontsize=15)
    ax.set_xticks(ind)
    ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=270)
    ax.set_xticklabels(labels[::1])
    #ax.set_yscale('log')
    plt.plot(ind, list(al_qaida.values()), label='Al-Qaida', marker='x')
    plt.plot(ind, list(al_qaida_iraq.values()), label='Al-Qaida in Iraq', marker='o')
    plt.plot(ind, list(al_qaida_yemen.values()), label='Al-Qaida in Yemen', marker='v')
    plt.plot(ind, list(al_qaida_lebanon.values()), label='Al-Qaida in Lebanon', marker='s')
    plt.plot(ind, list(al_qaida_sa.values()), label='Al-Qaida in Saudi Arbia', marker='.')
    plt.plot(ind, list(aqim.values()), label='Al-Qaida in the Islamic Maghreb (AQIM)', marker='8')
    plt.plot(ind, list(aqap.values()), label='Al-Qaida in the Arabian Peninsula (AQAP)', marker='^')
    plt.plot(ind, list(europe.values()), label='Secret Organization of al-Qaida in Europe', marker='<')
    plt.plot(ind, list(sweden.values()), label='Al-Qaida Organization for Jihad in Sweden', marker='>')
    plt.plot(ind, list(indian.values()), label='Al-Qaida in the Indian Subcontinent', marker='p')
    plt.plot(ind, list(sympathizer.values()), label='Sympathizers of Al-Qaida Organization', marker='h')
    plt.legend(loc='best', fontsize=15)
    plt.xlim([-1,16])
    plt.show()    
    
def prepareAlQaidaData():
    for year in years:
        try:
            al_qaida[year] = Counter(global_data.loc[global_data['gname'] == 'Al-Qaida'].iyear)[year]
        except:
            al_qaida[year] = 0
        try:         
            al_qaida_iraq[year] = Counter(global_data.loc[global_data['gname'] == 'Al-Qaida in Iraq'].iyear)[year]
        except:
            al_qaida_iraq[year] = 0
        try:
            al_qaida_yemen[year] = Counter(global_data.loc[global_data['gname'] == 'Al-Qaida in Yemen'].iyear)[year]
        except:
            al_qaida_yemen[year] = 0
        try:
            al_qaida_lebanon[year] = Counter(global_data.loc[global_data['gname'] == 'Al-Qaida in Lebanon'].iyear)[year]
        except:
            al_qaida_lebanon[year] = 0
        try:
            al_qaida_sa[year] = Counter(global_data.loc[global_data['gname'] == 'Al-Qaida in Saudi Arabia'].iyear)[year]
        except:
            al_qaida_sa[year] = 0
        try:
            aqap[year] = Counter(global_data.loc[global_data['gname'] == 'Al-Qaida in the Arabian Peninsula (AQAP)'].iyear)[year]
        except:
            aqap[year] = 0
        try:
            aqim[year] = Counter(global_data.loc[global_data['gname'] == 'Al-Qaida in the Islamic Maghreb (AQIM)'].iyear)[year]
        except:
            aqim[year] = 0
        try:
            europe[year] = Counter(global_data.loc[global_data['gname'] == 'Secret Organization of al-Qaida in Europe'].iyear)[year]
        except:
            europe[year] = 0
        try:
            sweden[year] = Counter(global_data.loc[global_data['gname'] == 'Al-Qaida Organization for Jihad in Sweden'].iyear)[year]
        except:
            sweden[year] = 0
        try:
            indian[year] = Counter(global_data.loc[global_data['gname'] == 'Al-Qaida in the Indian Subcontinent'].iyear)[year]
        except:
            indian[year] = 0
        try:
            sympathizer[year] = Counter(global_data.loc[global_data['gname'] == 'Sympathizers of Al-Qaida Organization'].iyear)[year]  
        except:
            sympathizer[year] = 0
            
def isilTrends():
    fig, ax = plt.subplots(figsize=(18, 8))
    labels = years
    ind = np.arange(0, len(labels), 1)
    ax.set_title('Islamic State Global Activity', fontsize=15, fontweight='bold')
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.set_xlabel('', fontsize=15)
    ax.set_ylabel('Attacks' , fontsize=15)
    ax.set_xticks(ind)
    ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=270)
    ax.set_xticklabels(labels[::1])
    #ax.set_yscale('log')
    plt.plot(ind, list(isi.values()), label='Islamic State of Iraq (ISI)', marker='x')
    plt.plot(ind, list(bangladesh.values()), label='Islamic State in Bangladesh', marker='o')
    plt.plot(ind, list(mei.values()), label='Movement of the Islamic State (MEI)', marker='v')
    plt.plot(ind, list(isil.values()), label='Islamic State of Iraq and the Levant (ISIL)', marker='s')
    plt.plot(ind, list(jerusalem.values()), label='Supporters of the Islamic State in Jerusalem', marker='.')
    plt.plot(ind, list(mosques.values()), label='Supporters of the Islamic State in the Land of the Two Holy Mosques', marker='8')
    plt.legend(loc='best', fontsize=15)
    plt.xlim([-1,16])
    plt.show()  
    
def prepareIsilData():
    for year in years:
        try:
            isi[year] = Counter(global_data.loc[global_data['gname'] == 'Islamic State of Iraq (ISI)'].iyear)[year]
        except:
            isi[year] = 0
        try:         
            bangladesh[year] = Counter(global_data.loc[global_data['gname'] == 'Islamic State in Bangladesh'].iyear)[year]
        except:
            bangladesh[year] = 0
        try:
            mei[year] = Counter(global_data.loc[global_data['gname'] == 'Movement of the Islamic State (MEI)'].iyear)[year]
        except:
            mei[year] = 0
        try:
            isil[year] = Counter(global_data.loc[global_data['gname'] == 'Islamic State of Iraq and the Levant (ISIL)'].iyear)[year]
        except:
            isil[year] = 0
        try:
            jerusalem[year] = Counter(global_data.loc[global_data['gname'] == 'Supporters of the Islamic State in Jerusalem'].iyear)[year]
        except:
            jerusalem[year] = 0
        try:
            mosques[year] = Counter(global_data.loc[global_data['gname'] == 'Supporters of the Islamic State in the Land of the Two Holy Mosques'].iyear)[year]
        except:
            mosques[year] = 0
                       
def correlation():
    print('US Internal / Global Attacks: {}'.format(stats.spearmanr(list(Counter(us_internal_data.iyear).values()), list(Counter(global_data.loc[global_data['iyear'] >= 2001].iyear).values()))))
    print('US External / Global Attacks: {}'.format(stats.spearmanr(list(Counter(us_external_data.iyear).values()), list(Counter(global_data.loc[global_data['iyear'] >= 2001].iyear).values()))))
    print('US External / US Internal: {}'.format(stats.spearmanr(list(Counter(us_internal_data.iyear).values()), list(Counter(us_external_data.iyear).values()))))
    
def summaryStatistics():
    print('%s global events observed' %len(global_data))
    print('%s events observed in the United States' %len(us_internal_data))
    print('%s events observed outside the United States' %len(us_external_data))                              