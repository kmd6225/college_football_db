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
        return(df[0].iloc[2:len(df[0]),0:len(df[0].columns)])
    except ValueError:
        print('Please enter a boolean for is_offense argument ')


def get_roster(school, year):
    school = str(school)
    year = str(year)
    link = f'https://www.sports-reference.com/cfb/schools/{school}/{year}-roster.html'

    df = pd.read_html(link, match = 'Player', header= 0)[0]
    df = df[df['Player'] != 'Player']
    return(df)




