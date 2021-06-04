import requests
from bs4 import BeautifulSoup

class ARCfootball():
    HEADERS = {
               'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
            }


    def output_transfers(transfers):
        for transfer in transfers:
            print(transfer['name'] + ' : ' + transfer['links']['player'])
            print(transfer['pr_club'] + ' -> ' + transfer['new_club'])
            print(transfer['pr_club'] + ' : ' + transfer['links']['pr_club'])
            print(transfer['new_club'] + ' : ' + transfer['links']['new_club'])
            print('')


    def getting_info_result(liga):
        URL = 'https://www.sports.ru/' + str(liga) + '/table/'
        response = requests.get(URL, headers=HEADERS)
        clubs = []
        soup = BeautifulSoup(response.content, 'lxml')
        articles = soup.find('div', class_='stat mB6')
        items = articles.find_all('tr')

        for item in items:
            params = item.find_all('td')
            place = params[0].text
            name = params[1].text
            wins = params[3].text
            loses = params[5].text
            goal_scored = params[6].text
            goal_missed = params[7].text
            number = params[8].text
            if name != 'Команда':
                clubs.append({
                    'place' : place,
                    'name' : name,
                    'wins' : wins,
                    'loses' : loses,
                    'goal_scored' : goal_scored,
                    'goal_missed' : goal_missed,
                    'number' : number
                })
        return clubs


    def main_result(choice):
        if choice == 1:
            liga = 'la-liga'
        if choice == 2:
            liga = 'rfpl'
        if choice == 3:
            liga = 'fnl'
        if choice == 4:
            liga = 'epl'
        if choice == 5:
            liga = 'seria-a'
        if choice == 6:
            liga = 'bundesliga'
        output_result(getting_info_result(liga))


    def main_matches(choice):
        if choice == 1:
            liga = 'la-liga'
        if choice == 2:
            liga = 'rfpl'
        if choice == 3:
            liga = 'fnl'
        if choice == 4:
            liga = 'epl'
        if choice == 5:
            liga = 'seria-a'
        if choice == 6:
            liga = 'bundesliga'
        output_matches(getting_info_matches(liga))


    def getting_info_matches(liga):
        URL = 'https://www.sports.ru/' + str(liga) + '/calendar/'
        response = requests.get(URL, headers=HEADERS)
        matches = []
        soup = BeautifulSoup(response.content, 'lxml')
        articles = soup.find_all('table', class_='stat-table')
        for article in articles:
            items = article.find_all('tr')

            for item in items:
                date = item.find('td', class_='name-td alLeft').text
                home_team = item.find('td', class_='owner-td').text
                guest_team = item.find('td', class_='guests-td').text
                score = item.find('td', class_='score-td').text

                matches.append({
                    'date' : str(date),
                    'home_team' : home_team,
                    'guest_team' : guest_team,
                    'score' : score,

                })
        return matches


    def output_matches(matches):
        print('Какой клуб тебя интересует?')
        user_club = input()
        user_matches = []
        for match in matches:
            if match['home_team'] == user_club or match['guest_team'] == user_club:
                user_matches.append(match)
        for user_match in user_matches:

            print(user_match['date'])
            print(user_match['home_team'] + ' ' + user_match['score'] + ' ' + user_match['guest_team'])


    def liga_input():
        print('Какая лига тебя интересует?')
        print('1. Лалига')
        print('2. РПЛ')
        print('3. ФНЛ')
        print('4. АПЛ')
        print('5. Серия - А')
        print('6. Бундеслига')
        return int(input('->'))


    def output_result(clubs):
        for club in clubs:
            name = club['name']
            number = club['number']
            print(f'{name} : {number} очков')


    def getting_info_transfers(liga):
        URL = 'https://www.sports.ru/' + liga + '/transfers/'
        response = requests.get(URL, headers=HEADERS)
        transfers = []
        soup = BeautifulSoup(response.content, 'lxml')
        articles = soup.find('tbody', class_='transfers-table__body')
        items = articles.find_all('tr', class_='transfers-table__row')
        for item in items:
            name = item.find('td', class_='transfers-table__body-span transfers-table__name').text
            clubs = item.find_all('a')
            pr_club = clubs[1].text
            new_club = clubs[2].text
            links = {
                'player' : clubs[0].get('href'),
                'pr_club' : clubs[1].get('href'),
                'new_club' : clubs[2].get('href')
            }
            transfers.append({
                'name' : name,
                'pr_club' : pr_club,
                'new_club' : new_club,
                'links' : links
            })
        return transfers


    def main_tranfers(choice):
        if choice == 1:
            liga = 'la-liga'
        if choice == 2:
            liga = 'rfpl'
        if choice == 3:
            liga = 'fnl'
        if choice == 4:
            liga = 'epl'
        if choice == 5:
            liga = 'seria-a'
        if choice == 6:
            liga = 'bundesliga'
        output_transfers(getting_info_transfers(liga))
