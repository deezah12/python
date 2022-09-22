users = [
    {'name': 'hadiza',
     'age': 21,
     'gender': 'female',
     'user_name': 'deezah',
     'is_verified': True,
     'tweets': [{'content': 'Po for president', 'likes': 450, 'retweets': 233},
                {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2}]
     },

    {'name': 'Ibrahim',
     'age': 21,
     'gender': 'Male',
     'user_name': 'ibro',
     'is_verified': False,
     'tweets': [{'content': 'Programming is fun', 'likes': 34, 'retweets': 12}],

     },
    {'name': 'James',
     'age': 21,
     'gender': 'Male',
     'user_name': 'amez',
     'is_verified': True,
     'tweets': [{'content': 'love is life', 'likes': 450, 'retweets': 233},
                {'content': 'only Racheal i know', 'likes': 97, 'retweets': 21}]
     },
    {'name': 'Racheal',
     'age': 21,
     'gender': 'female',
     'user_name': 'betty',
     'is_verified': False,
     'tweets': [{'content': '.', 'likes': 1450, 'retweets': 1330},
                {'content': 'Thinking about Amez', 'likes': 4, 'retweets': 2},
                {'content': 'Amezing grace', 'likes': 2000, 'retweets': 1580}, ]
     },
    {'name': 'Elijah',
     'age': 17,
     'gender': 'Male',
     'user_name': 'el_d_si',
     'is_verified': False,
     'tweets': [{'content': '#Osun decides', 'likes': 12, 'retweets': 8},
                {'content': 'imole de', 'likes': 97, 'retweets': 21}]
     },
    {'name': 'Dorris',
     'age': 16,
     'gender': 'female',
     'user_name': 'anything',
     'is_verified': False,
     'tweets': [{'content': 'i love Chimamanda ', 'likes': 450, 'retweets': 233},
                {'content': 'Feminism is the goal', 'likes': 97, 'retweets': 21}]
     },
    {'name': 'Jacob',
     'age': 37,
     'gender': 'Male',
     'user_name': '',
     'is_verified': True,
     'tweets': [{'content': 'reflection is my goal', 'likes': 450, 'retweets': 233},
                {'content': 'how to get more likes on on twitter', 'likes': 97, 'retweets': 21}]
     },
    {'name': 'Derek',
     'age': 29,
     'gender': 'Male',
     'user_name': 'standby_gen',
     'is_verified': True,
     'tweets': [{'content': 'love is life', 'likes': 450, 'retweets': 233},
                {'content': 'only Racheal i know', 'likes': 97, 'retweets': 21}]
     },
    {'name': 'Mubarak',
     'age': 47,
     'gender': 'Male',
     'user_name': 'Whistle',
     'is_verified': True,
     'tweets': []
     }
]

no_of_users = len(users)
usernames = {user['user_name'] for user in users}
female_users = [user['name'] for user in users if user['gender'] == 'female']
in_active_users = [user for user in users if len(user['tweets']) == 0]
name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]
check_if_verified = [user for user in users if user['is_verified'] == True]
avg_age_of_users = round(sum(user['age'] for user in users) / len(users))
print(avg_age_of_users)