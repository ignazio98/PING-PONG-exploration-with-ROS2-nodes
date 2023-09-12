import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
import sys

def average_chart(df):
    """
        Create 3 plot:
        First compare average Time in ms, between local and lan
        Second create a plot to compare average Time for only LAN
        Third create a plot to compare average Time for only LOCAL
    Args:
        df ([dataframe]): [dataframe created from make_average_chart function]
    """
    ax1 = df.pivot("Message Size", "Scrittori").plot.bar(figsize = (12, 6))
    plt.savefig("avg-compare-lan-local.pdf", format="pdf", bbox_inches="tight")
    ax2 = df[['Scrittori', 'Message Size', 'LAN']].pivot("Message Size", "Scrittori").plot.bar(figsize = (12, 6))
    plt.savefig("avg-lan.pdf", format="pdf", bbox_inches="tight")
    ax3 = df[['Scrittori', 'Message Size', 'LOCAL']].pivot("Message Size", "Scrittori").plot.bar(figsize = (12, 6))
    plt.savefig("avg-local.pdf", format="pdf", bbox_inches="tight")

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
    for i in range(0, 4):
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
    axis[j//columns,j%columns].set_title('Writer_' + str(size[j]))

    for ax in axis.flat:
        ax.set(xlabel='Request', ylabel='Time ms')

    plt.savefig("result-" + str(writer[i]) + "-" + provenance + "-writer.pdf", format="pdf", bbox_inches="tight")

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
    axis[j//columns,j%columns].set_title('Writer_' + str(size[j]))

    for ax in axis.flat:
        ax.set(xlabel='Request', ylabel='Time ms')

    plt.savefig("result-" + str(writer[i]) + "-" + provenance + "-message_size.pdf", format="pdf", bbox_inches="tight")

def table_creation(df, writer, size, source):
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

            tmp['Scrittori'] = [i for x in range(0, size)]
            tmp['Message Size'] = [j for x in range(0, size)]

            for k in range(0, i):
                t = data[data['Source'] == source[k]]

                refill = []
                if len(t['Time']) < size:
                    refill = [t['Time'].iloc[1]] * (size - len(t['Time']))

                tmp['client' + str(k)] = np.concatenate((np.array(t['Time']), refill))

            ris = pd.concat([ris, tmp])
    return ris.fillna(0)

def main():
    """
        args 
            1 : LAN/LOCAL
            2 : AVG/R/BOTH
    """    

    if(len(sys.argv) != 3):
        print("Error, number of parameter isn't correct")
        return 1
    
    #save parameter
    provenance = sys.argv[1]
    type = sys.argv[2]

    #open dataset
    df = pd.read_csv('/result/DATI.csv', sep=";", header=0)

    #upload global variable
    source_unique = df['Source'].unique().tolist()
    scrittori_unique = df['Scrittori'].unique().tolist()
    message_unique = df['Message Size'].unique().tolist()

    size = columns = 0
    if(type == "LAN"):
        size = 50
        columns = 4
    else:
        size = 100
        columns = 5

    R = copy.deepcopy(table_creation(df, scrittori_unique, message_unique,  source_unique))
    R = copy.deepcopy(r_chart(R, scrittori_unique, message_unique))

    make_r_chart_by_writer(R, scrittori_unique, message_unique, columns, type)
    make_r_chart_by_size(R, scrittori_unique, message_unique, columns, type)


    avg_dataframe = make_average_chart(R, scrittori_unique, message_unique)
    make_average_chart(avg_dataframe)

    return 

if __name__ == '__main__':
    main()
