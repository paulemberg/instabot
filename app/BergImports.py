#!/usr/local/bin/python
# coding: utf-8
# imports
import json
from instapy import InstaPy
from instapy import smart_run

class runner:

    def start(self):
        # login credentials
        data = None
        with open('../config/settings.json', 'r') as myfile:
            data = myfile.read()
            obj = json.loads(data)
            insta_username = obj['instagram']['user']
            insta_password = obj['instagram']['pass']
      
        comments = ['Venha nos conhecer @{}',
              'Adoro seu Perfil! @{}',
              'Nosso feed pode ter algo para você :thumbsup: ',
              'Tem promoção lá no feed :open_mouth:' ,
              'LOL :open_mouth @{}',
              'Produtos importados @{}',
              'Produtos Apple @{}',
              'Notebooks e Mackbooks @{}',
              ':raised_hands: WoW',
              'Da uma olhada no nosso feed @{} :muscle:',
              'Promoção em nosso feed!',
              'lol']
        locations_sao_paulo = [ '567041712/brazil/',
                              '112047398814697/sao-paulo-brazil/']

        tags = ['#apple',
                  '#macbookpro',
                  '#iphone',
                  '#mackbook']
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
            session.like_by_locations(locations_sao_paulo, amount=3)
            session.like_by_tags(tags, amount=3)
            # Joining Engagement Pods
            session.set_do_comment(enabled=True, percentage=10)
            session.set_comments(comments)
            session.join_pods(topic='entertainment', engagement_mode='heavy')

            #follow
            session.follow_by_tags(tags, amount=5)
