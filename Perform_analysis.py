#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy

def average_chart(df, local, lan):
    """
        Create 3 plot:
        First compare average Time in ms, between local and lan
        Second create a plot to compare average Time for only LAN
        Third create a plot to compare average Time for only LOCAL
    Args:
        df ([dataframe]): [dataframe created from make_average_chart function]
        local ([bool]): [local is empty or not]
        lan ([bool]): [lan is empty or not]
    """
    df['LAN'] = df['LAN'].fillna(0)
    df['LOCAL'] = df['LOCAL'].fillna(0)
    
    ax1 = df.pivot_table(index="Message Size", columns="Scrittori").plot.bar(figsize = (12, 6))
    plt.savefig("result/plot/avg-compare-lan-local.pdf", format="pdf", bbox_inches="tight")
    
    if not local:
        ax2 = df[['Scrittori', 'Message Size', 'LAN']].pivot_table(index="Message Size", columns="Scrittori", values="LAN").plot.bar(figsize = (12, 6))
        plt.savefig("result/plot/avg-lan.pdf", format="pdf", bbox_inches="tight")
    
    if not lan:
        ax3 = df[['Scrittori', 'Message Size', 'LOCAL']].pivot_table(index="Message Size", columns="Scrittori", values="LOCAL").plot.bar(figsize = (12, 6))
        plt.savefig("result/plot/avg-local.pdf", format="pdf", bbox_inches="tight")

def make_average_chart(df, writer, size):
    """
    Createa a dataframe in which for each writer, message_size and provenance will calculate the average Time in ms

    Args:
        df ([dataframe]): [dataframe created from table creation function]
        writer ([list]): [number of writer read from datafile]
        size ([list]): [number of message_size read from datafile]

    Returns:
        [dataframe]: [dataframe with average Time]
    """
    lan_source = copy.deepcopy(df[df['Provenance'] == 'LAN'])
    local_source = copy.deepcopy(df[df['Provenance'] == 'LOCAL'])

    ris = pd.DataFrame(columns=['Scrittori', 'Message Size', 'LAN', 'LOCAL'])

    for i in range(0, len(size)):
        for j in range(0, len(writer)):
            avg_lan = lan_source[(lan_source['Scrittori'] == writer[j]) & (lan_source['Message Size'] == size[i])]['Time'].mean()
            avg_local = local_source[(local_source['Scrittori'] == writer[j]) & (local_source['Message Size'] == size[i])]['Time'].mean()
            
            list_row_local = [writer[j] , size[i], avg_lan , avg_local]
            ris.loc[len(ris)] = list_row_local
  
    return ris

def r_chart(df, scrittori, size):
    """
    Create the following columns: average, average of average, deviation, Upper bound and Lower bound

    Args:
        df ([dataframe]): [dataframe created from table_creation functino]
        scrittori ([list]): [list of writer found from datafile]
        size ([list]): [list of message size found from datafile]

    Returns:
        [dataframe]: [dataframe with statistical columns]
    """
    basic = ['Scrittori', 'Message Size']
    column_list = []
    for i in range(0, scrittori):
        column_list.append('client' + str(i))

    R = copy.deepcopy(df[(df['Scrittori'] == scrittori) & (df['Message Size'] == size)][basic + column_list])

    R['Xbar'] = R[column_list].mean(axis=1)
    R['R'] = R[column_list].std(axis=1)
    R['Rbar'] = R['Xbar'].mean()
    R['UCL'] = R['Rbar'] + R['R'].mean() * 1.5
    m = R['Rbar'] - R['R'].mean() * 1.5
    R['LCL'] = max(0, m[0])

    return R

def make_r_chart_by_writer(df, writer, size, columns, provenance):
    """
    Create a chart composet by 2 * columns subplot.
    In which for each subplot will be show average time in ms, for each writer.
    This fuction will save the plot into pdf file

    Args:
        df ([dataframe]): [description]
        writer ([type]): [description]
        size ([type]): [description]
        columns ([type]): [description]
        provenance ([type]): [description]
    """

    fig, axis = plt.subplots(nrows=2,ncols=columns)
    fig.set_size_inches(60, 30)
    symbol = ["o", "v", "^", "*", "+", "x", "P", "D", "s"]

    for j in range(0, len(size)):
        median = 0
        for i in range(0, len(writer)):
            data = r_chart(df, writer[i], size[j])
            axis[j//columns,j%columns].plot(data['Xbar'], marker=symbol[i], label = 'Writer' + str(writer[i]))
            median = min(median, data['Rbar'][0])

        axis[j//columns,j%columns].plot(data['UCL'], color='b', label = 'UCL')
        axis[j//columns,j%columns].plot(data['LCL'], color='k', label = 'LCL')
        axis[j//columns,j%columns].plot(median, color='r', label = 'Median')

        axis[j//columns,j%columns].legend()
        axis[j//columns,j%columns].grid()
        axis[j//columns,j%columns].set_title('Size_' + str(size[j]))

    for ax in axis.flat:
        ax.set(xlabel='Request', ylabel='Time ms')
        
    plt.savefig(f"result/plot/result-{provenance}-writer.pdf", format="pdf", bbox_inches="tight")

def make_r_chart_by_size(df, writer, size, columns, provenance):
    """
    Create a chart composet by 2 * columns subplot.
    In which for each subplot will be show average time in ms, for each message size.
    This fuction will save the plot into pdf file

    Args:
        df ([dataframe]): [description]
        writer ([type]): [description]
        size ([type]): [description]
        columns ([type]): [description]
        provenance ([type]): [description]
    """

    fig, axis = plt.subplots(nrows=2,ncols=columns)
    fig.set_size_inches(60, 30)
    symbol = ["o", "v", "^", "*", "+", "x", "P", "D", "s"]

    for j in range(0, len(writer)):
        median = 0
        for i in range(0, len(size)):
            data = r_chart(df, writer[j], size[i])
            axis[j//columns,j%columns].plot(data['Xbar'], marker=symbol[i], label = 'Writer' + str(writer[j]))
            median = min(median, data['Rbar'][0])

        axis[j//columns,j%columns].plot(data['UCL'], color='b', label = 'UCL')
        axis[j//columns,j%columns].plot(data['LCL'], color='k', label = 'LCL')
        axis[j//columns,j%columns].plot(median, color='r', label = 'Median')

        axis[j//columns,j%columns].legend()
        axis[j//columns,j%columns].grid()
        axis[j//columns,j%columns].set_title('Writer' + str(writer[j]))

    for ax in axis.flat:
        ax.set(xlabel='Request', ylabel='Time ms')

    plt.savefig(f"result/plot/result-{provenance}-message-size.pdf", format="pdf", bbox_inches="tight")

def table_creation(df, writer, size, source, n_element):
    """
    Create a dataframe with a dynamic number of column, due to value of scrittori_unique 

    Args:
        df ([dataframe]): [dataframe read from file]
        size ([int]): [number of row for each client]

    Returns:
        [dataframe]: [dataframe modified]
    """
    ris = pd.DataFrame()

    for i in writer:
        for j in size:
            data = df[(df['Scrittori'] == i) & (df['Message Size'] == j)]
            tmp = pd.DataFrame()

            tmp['Scrittori'] = [i for x in range(0, n_element)]
            tmp['Message Size'] = [j for x in range(0, n_element)]

            for k in range(0, i):
                t = data[data['Source'] == source[k]]

                refill = []
                if len(t['Time']) < n_element and len(t['Time']) > 0:
                    refill = [t['Time'].iloc[0]] * (n_element - len(t['Time']))
                elif len(t['Time']) == 0:
                    refill = [0] * (n_element - len(t['Time']))
                elif len(t['Time']) > n_element:
                    t['Time'] = t['Time'].iloc[0:n_element]

                tmp['client' + str(k)] = np.concatenate((np.array(t['Time']), refill))

            ris = pd.concat([ris, tmp])
    return ris.fillna(0)
    
def check_structure(df, columns):
    """
    Split the data inside the DATI.csv file into multiple columns 

    Args:
        df ([dataframe]): [dataframe read from file]
        column ([int]): [number of column of df]

    Returns:
        [dataframe]: [dataframe splited]
    """
    header = ['Source', 'Scrittori', 'Message Size', 'Time', 'Provenance']
    ris_ = pd.DataFrame()
    if columns == 1:
        #I have only 1 column, i need to split
        ris_ = df.iloc[:, 0].str.split('-', expand=True)
        ris_.columns = header
    
    ris_[['Scrittori', 'Message Size','Time']] = ris_[['Scrittori', 'Message Size','Time']].astype('int64')
    return ris_

def main():
    #open dataset
    lan = "LAN"
    local = "LOCAL"
    df = pd.read_csv('result/DATI.csv', sep=";", header=0)
    
    df = check_structure(df, df.shape[1])
    dfall = copy.deepcopy(df)
    dflan = copy.deepcopy(df[df['Provenance'] == lan])
    dflocal = copy.deepcopy(df[df['Provenance'] == local])

    #upload global variable
    source_unique = dfall['Source'].unique().tolist()
    scrittori_unique = dfall['Scrittori'].unique().tolist()
    message_unique_lan = dflan['Message Size'].unique().tolist()
    message_unique_local = dflocal['Message Size'].unique().tolist()

    #average chart
    avg_dataframe = make_average_chart(dfall, scrittori_unique, message_unique_local)
    average_chart(avg_dataframe, dflocal.empty, dflan.empty)
    
    if not dflan.empty:
    	# R chart for LAN settings
        #LAN Settings
        size = 50
        columns = 4
        Rlan = copy.deepcopy(table_creation(dflan, scrittori_unique, message_unique_lan, source_unique, size))
        make_r_chart_by_writer(Rlan, scrittori_unique, message_unique_lan, columns, lan)
        make_r_chart_by_size(Rlan, scrittori_unique, message_unique_lan, 2, lan)

    if not dflocal.empty:
    	# R chart for LOCAL settings
    	#LOCAL
        size = 100
        columns = 5

        Rlocal = copy.deepcopy(table_creation(dflocal, scrittori_unique, message_unique_local, source_unique, size))
        make_r_chart_by_writer(Rlocal, scrittori_unique, message_unique_local, columns, local)
        make_r_chart_by_size(Rlocal, scrittori_unique, message_unique_local, 2, local)
 
    return 

if __name__ == '__main__':
    main()