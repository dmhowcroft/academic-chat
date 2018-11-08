#!/usr/bin/python3
import abc
import json
import random
from difflib import SequenceMatcher

publication_lists = [
    [2018, "The ACL Anthology: Current State and Future Directions"],
    [2017, "Generating Contrastive Referring Expressions"],
    [2015, "The Impact of Listener Gaze on Predicting Reference Resolution."],
    [2013, "Predicting the resolution of referring expressions from user behavior"],
    [2014, "Interpreting Natural Language Instructions Using Language, Vision, and Behavior"],
    [2012, "Corpus-based Interpretation of Instructions in Virtual Environments"],
    [2011, "Inferencia de puntos estratégicos en mundos virtuales"],
    [2010, "Ingenieria de requisitos web orientada a aspectos con transformacion de modelos"],]

class Oracle:
    def __init__(self):
        """An oracle.py receives structured queries and replies in natural language"""
        self.general = GeneralOracle()
        self.project = ProjectOracle()
        self.publications = PublicationsOracle()
        self.blog = BlogOracle()

    @abc.abstractmethod
    def supported_operations(self):
        """Returns the strings of the operations supported by this oracle.py"""
        return

    def ask(self, rule):
        """Answers your question, as long as your question sticks to the grammar we have defined earlier.

        :param rule: a list composed of an operation and a list of optional parameters
        :return: a natural language answer to the question for the oracle.py
        """
        if rule[0] in self.general.supported_operations():
            return self.general.ask(rule)
        elif rule[0] in self.project.supported_operations():
            return self.project.ask(rule)
        elif rule[0] in self.publications.supported_operations():
            return self.publications.ask(rule)
        elif rule[0] in self.blog.supported_operations():
            return self.blog.ask(rule)
        else:
            msg={}
            msg['text']='I\'m sorry, I didn\'t understand your question'
            return json.dumps(msg)


class GeneralOracle(Oracle):
    def __init__(self):
        pass

    def supported_operations(self):
        return ['general', 'professional', 'interests']

    def ask(self, rule):
        msg = {'text': 'I don\'t know.'}
        if rule[0] == 'general':
            msg['text'] = random.choice(['Martin graduated from the Faculty of Mathematics, Astronomy, and Physics of the National University of Córdoba, Argentina, with a M.Sc. in computer science. He\'s currently based in Saarbrücken, Germany, working on his PhD in computational linguistics.',
                                         'He sometimes works as his department\'s unofficial graphic designer. He designed posters, conference booklets, websites, and illustrations for multiple conferences and events.',
                                         'His regular hobbies are drawing, music, writing, and some photography.'])
        elif rule[0] == 'professional':
            msg['text'] = random.choice(['He has programmed in several languages (too many), delved into Microcontrollers and Assembly, moved up to Operating Systems, and stuck the landing with some AI and Deep Learning.',
                                         'He is one of the current system administrators for the ACL Anthology.',
                                         'If you only have a passing interest on what he does, then he has articles explaininig his research in simple terms. <a href=\'https://7c0h.com/research.html\'>Check them out!</a>.'])
        elif rule[0] == 'interests':
            msg['text'] = random.choice(['His regular hobbies are drawing, music, writing, and some photography.',
                                         'His favorite OS is Unix. More precisely, Debian. But BSD sounds tempting.',
                                         'He prefers tabs over spaces.',
                                         'He has dinner at 10pm.'])
        return json.dumps(msg)


class ProjectOracle(Oracle):
    def __init__(self):
        pass

    def supported_operations(self):
        return ['proj_title', 'proj_desc', 'proj_repo']

    def ask(self, rule):
        msg = {'text': 'I don\'t know about that yet.'}
        return json.dumps(msg)


class PublicationsOracle(Oracle):
    def __init__(self):
        pass

    def supported_operations(self):
        return ['last_pubs', 'pubs_between', 'pubs_with', 'pubs_venue']

    def ask(self, rule):
        msg = {'text': 'I haven\'t been traind to answer that yet. Try this one: %s' % random.choice(publication_lists)[1]}
        return json.dumps(msg)

class BlogOracle(Oracle):
    # TODO: There should be a smarter way to query these things that having a hard-coded dictionary

    posts_dict = [
        ('nlp_and_taylor_swift.html', 'A more polite Taylor Swift with NLP and word vectors'),
        ('eyetracking_and_visual_salience.html', 'Eye-tracking and visual salience'),
        ('sentiments_2_user_groups.html','Sentiments are the new Spam - Part 2: user groups'),
        ('sentiments_are_the_new_spam.html', 'Sentiments are the new Spam - Prologue'),
        ('calibrate_tablet_genius_mousepen.html', 'Genius MousePen i608 in Debian Linux'),
        ('recommendation.html', 'The problem with music recommendations'),
        ('voting.html', 'Voting in Argentina'),
        ('i_dont_visit_that_website_anymore.html', 'I don\'t visit that website anymore'),
        ('what_do_you_do_again.html', 'So, what did you say you do?'),
        ('experiment_report.html', 'Experiment report'),
        ('im_an_idiot.html', 'I am an idiot (a Windows Phone development story)'),
        ('save_advertising.html', 'My plan to save online advertising'),
        ('im_not_that_angry.html', 'I\'m not that angry'),
        ('screw_your_paid_internet.html', 'Screw your ad-supported internet'),
        ('neural_network.html', 'A neural network in Javascript'),
        ('bye_spotify.html', 'It\'s not me, Spotify, it\'s you'),
        ('guitar_music_and_i.html', 'Guitar music and I'),
        ('semantic_and_observational.html', 'The Semantic and Observational models'),
        ('tapiz.html', 'The Tapiz instruction-giving system'),
        ('give_challenge.html', 'What is the GIVE Challenge?'),
        ('training_and_testing.html', 'What are training and testing?'),
        ('diy_tumbler.html', 'DIY Tumbler skins, the math way'),
        ('tweet_test.html', 'I\'m also trying to have tweets here'),
        ('random_links_1.html', 'Random links (I)'),
        ('why_ill_never_be_rich.html', 'Why I\'ll never be rich'),
        ('testing_code.html', 'Testing code'),
        ('almost_there.html', 'Almost there!'),
        ('setting_things_up.html', 'Setting everything up'),
        ('first_post.html', 'First post!')]
    base_url = "https://www.7c0h.com/blog/new/"

    def __init__(self):
        pass

    def supported_operations(self):
        return ['blog_last', 'blog_titles', 'blog_post', 'blog_random']

    def ask(self, rule):
        msg = {'text': 'I don\'t know'}
        if rule is None:
            return json.dumps(msg)
        if rule[0] == 'blog_last':
            msg['text'] = random.choice(['The last blog post is:',
                                         'I think the last blog post is:',
                                         'Here is the latest blog post:',
                                         'You mean the latest blog post? It\'s this one:'])
            msg['items'] = [[self.posts_dict[0][1], self.base_url + self.posts_dict[0][0]]]
        elif rule[0] == 'blog_titles':
            if rule[1] > 1:
                all_msgs = []
                msg['text'] = 'These are the latest {} blog posts:'.format(rule[1])
                for i in range(rule[1]):
                    key = self.posts_dict[i][0]
                    all_msgs.append([self.posts_dict[i][1], self.base_url + key])
                msg['items'] = all_msgs
            else:
                return self.ask(['blog_last'])
        elif rule[0] == 'blog_random':
            msg['text'] = random.choice(['A random blog post is:',
                                         'I think a good blog post is:',
                                         'Here is a completely random blog post:',
                                         'You mean any blog post? Here\'s one:'])
            post = random.choice(self.posts_dict)
            msg['items'] = [[post[1], self.base_url + post[0]]]
        elif rule[0] == 'blog_post':
            ratio = 0
            best = 0
            for key in range(len(self.posts_dict)):
                new_ratio = SequenceMatcher(None, rule[1], self.posts_dict[key][1]).ratio()
                if new_ratio > ratio:
                    best = key
                    ratio = new_ratio
            msg['text'] = 'The best match I found is this post:'
            msg['item'] = [[self.posts_dict[best][1], self.base_url + self.posts_dict[best][0]]]
        return json.dumps(msg)
