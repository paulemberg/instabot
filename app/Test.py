# imports
import json
from instapy import InstaPy
from instapy import smart_run

# login credentials
data = None
with open('../config/settings.json', 'r') as myfile:
        data = myfile.read()
obj = json.loads(data)
insta_username = obj['instagram']['user']
insta_password = obj['instagram']['pass']

# comments = ['Nice shot! @{}',
#         'I love your profile! @{}',
#         'Your feed is an inspiration :thumbsup:',
#         'Just incredible :open_mouth:',
#         'What camera did you use @{}?',
#         'Love your posts @{}',
#         'Looks awesome @{}',
#         'Getting inspired by you @{}',
#         ':raised_hands: Yes!',
#         'I can feel your passion @{} :muscle:',
#         'So Great!']


comments = ['Incrível @{}',
        'Adoro seu Perfil! @{}',
        'Seu feed é uma inspiração :thumbsup:',
        'Simplesmente incrível :open_mouth:',
        'LOL :open_mouth @{}',
        'Muito bom seus posts @{}',
        'Sensacional @{}',
        'Inspirando pessoas @{}',
        ':raised_hands: WoW',
        'Poderosa(o) @{} :muscle:',
        'Muito bom!',
        'lol']

locations_sao_paulo = [ '112047398814697/sao-paulo-brazil/',
                        '105211170927706/avenida-paulista/',
                        '1067789380031549/sao-paulo-zona-norte/',
                        '111022996943637/sao-paulo/',
                        '112047398814697',
                        '105211170927706',
                        '1067789380031549',
                        '111022996943637'
                      ]

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # activity
  session.like_by_locations(locations_sao_paulo, amount=10)		
  session.like_by_tags(["empreendedorismo"], amount=10)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=25)
  session.set_comments(comments)
  session.join_pods(topic='general', engagement_mode='light')