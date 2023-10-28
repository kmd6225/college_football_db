import pandas as pd


def get_gamelog(school,year, is_offense = True):
    school = str(school)
    year = str(year)
    link = f'https://www.sports-reference.com/cfb/schools/{school}/{year}/gamelog/'
 
    try:

        if  is_offense :
            df = pd.read_html(link, match = 'Offensive Game Log',header= 1)
        else:
            df = pd.read_html(link, match = 'Defensive Game Log', header = 1)
        df = df[0].iloc[2:len(df[0]),0:len(df[0].columns)]

        home_ls = []

        for i in df[df.columns[2]].tolist():
            if i == '@':
                home_ls.append('TRUE')
            else:
                home_ls.append('FALSE')
        df[df.columns[2]] = home_ls
        df = df.rename(columns={df.columns[2] : 'is_home'})
        return(df)
    except ValueError:
        print('Please enter a boolean for is_offense argument ')


def get_roster(school, year):
    school = str(school)
    year = str(year)
    link = f'https://www.sports-reference.com/cfb/schools/{school}/{year}-roster.html'

    df = pd.read_html(link, match = 'Player', header= 0)[0]
    df = df[df['Player'] != 'Player']

    school_ls = [school for i in range(len(df))]
    year_ls = [year for i in range(len(df)) ]
    df['school'] = school_ls
    df['season'] = year_ls
    return(df)




