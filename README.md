# ARCfootball
Hey everybody. This is my first library, helps you to work with football in Python. Yes, it is looking for football matches, transfers and statistics. Easy to use! You are welcome
I hope it will help you to write code)
But how to use it?

Well, that's easy:
if you want to get info about matches, just write -> getting_info_matches(liga)
it returns massive with dictionaries like:
{
  'date' : '01.01',
  'home_team' : 'Russia',
  'guest_team' : 'Spain',
  'score' : '1(4):(3)1'
}
if you want to get info about results, just write -> getting_info_results(liga)
it returns massive with dictionaries like:
{
  'place' : '2',
  'name' : 'RB Leipzig',
  'wins' : '19',
  'loses' : '7',
  'goal_scored' : '60',
  'goal_missed' : '32',
  'number' : '65'
}
if you want to get info about transfers, just write -> getting_info_transfers(liga)
it returns massive with dictionaries like:
{
  'name' : 'Timo Werner forward',
  'pr_club' : 'RB Leipzig',
  'new_club' : 'Chelsea',
  'links' : {
              'name' : 'https://www.sports.ru/tags/151752095/',
              'pr_club' : 'https://www.sports.ru/chelsea/transfers/',
              'new_club' : 'https://www.sports.ru/rb-leipzig/transfers/'
            }
}
So it is quite easy!
