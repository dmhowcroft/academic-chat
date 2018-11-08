#!/usr/bin/python3
import abc
import random
from difflib import SequenceMatcher


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
            return "I'm sorry, I didn't understand your question"


class GeneralOracle(Oracle):
    def __init__(self):
        pass

    def supported_operations(self):
        return ['general', 'professional', 'interests']

    def ask(self, rule):
        return "I don't know"


class ProjectOracle(Oracle):
    def __init__(self):
        pass

    def supported_operations(self):
        return ['proj_title', 'proj_desc', 'proj_repo']

    def ask(self, rule):
        return "I don't know"


class PublicationsOracle(Oracle):
    def __init__(self):
        pass

    def supported_operations(self):
        return ['last_pubs', 'pubs_between', 'pubs_with', 'pubs_venue']

    def ask(self, rule):
        return "I don't know"


class BlogOracle(Oracle):
    # TODO: There should be a smarter way to query these things that having a hard-coded dictionary
    posts_dict = {
        'nlp_and_taylor_swift.html': 'A more polite Taylor Swift with NLP and word vectors',
        'eyetracking_and_visual_salience.html': 'Eye-tracking and visual salience',
        'sentiments_2_user_groups.html': 'Sentiments are the new Spam - Part 2: user groups',
        'sentiments_are_the_new_spam.html': 'Sentiments are the new Spam - Prologue',
        'calibrate_tablet_genius_mousepen.html': 'Genius MousePen i608 in Debian Linux',
        'recommendation.html': 'The problem with music recommendations',
        'voting.html': 'Voting in Argentina',
        'i_dont_visit_that_website_anymore.html': 'I don\'t visit that website anymore',
        'what_do_you_do_again.html': 'So, what did you say you do?',
        'experiment_report.html': 'Experiment report',
        'im_an_idiot.html': 'I am an idiot (a Windows Phone development story)',
        'save_advertising.html': 'My plan to save online advertising',
        'im_not_that_angry.html': 'I\'m not that angry',
        'screw_your_paid_internet.html': 'Screw your ad-supported internet',
        'neural_network.html': 'A neural network in Javascript',
        'bye_spotify.html': 'It\'s not me, Spotify, it\'s you',
        'guitar_music_and_i.html': 'Guitar music and I',
        'semantic_and_observational.html': 'The Semantic and Observational models',
        'tapiz.html': 'The Tapiz instruction-giving system',
        'give_challenge.html': 'What is the GIVE Challenge?',
        'training_and_testing.html': 'What are training and testing?',
        'diy_tumbler.html': 'DIY Tumbler skins, the math way',
        'tweet_test.html': 'I\'m also trying to have tweets here',
        'random_links_1.html': 'Random links (I)',
        'why_ill_never_be_rich.html': 'Why I\'ll never be rich',
        'testing_code.html': 'Testing code',
        'almost_there.html': 'Almost there!',
        'setting_things_up.html': 'Setting everything up',
        'first_post.html': 'First post!'}
    post_last = 'nlp_and_taylor_swift.html'
    base_url = "https://www.7c0h.com/blog/new/"

    def __init__(self):
        pass

    def supported_operations(self):
        return ['blog_last', 'blog_titles', 'blog_post', 'blog_random']

    def ask(self, rule):
        msg = "I don't know"
        if rule is None:
            return msg
        if rule[0] == 'blog_last':
            msg = random.choice(['The last blog post is <a href="{}">{}</a>.',
                                 'I think the last blog post is <a href="{}">{}</a>.',
                                 'Here is the latest blog post: <a href="{}">{}</a>.',
                                 'You mean the latest blog post? It is <a href="{}">{}</a>.'])
            msg = msg.format(self.base_url + self.post_last, self.posts_dict[self.post_last])
        elif rule[0] == 'blog_titles':
            if rule[1] > 1:
                msg = "These are the latest {} blog posts:<br>".format(rule[1])
                for i in range(rule[1]-1):
                    key = list(self.posts_dict)[i]
                    msg += "<a href='{}'>{}</a>, ".format(self.base_url + "/" + key, self.posts_dict[key])
                key = list(self.posts_dict)[rule[1]-1]
                msg += "and <a href='{}'>{}</a>".format(self.base_url + "/" + key, self.posts_dict[key])
            else:
                msg = self.ask(['blog_last'])
        elif rule[0] == 'blog_random':
            msg = random.choice(['A random blog post is <a href="{}">{}</a>.',
                                 'I think a good blog post is <a href="{}">{}</a>.',
                                 'Here is a completely random blog post: <a href="{}">{}</a>.',
                                 'You mean any blog post? Here\'s one: <a href="{}">{}</a>.'])
            key = list(self.posts_dict)[0]
            msg = msg.format(self.base_url + key, self.posts_dict[key])
        elif rule[0] == 'blog_post':
            ratio = 0
            best = self.post_last
            for key in self.posts_dict:
                new_ratio = SequenceMatcher(None, rule[1], self.posts_dict[key]).ratio()
                if new_ratio > ratio:
                    best = key
                    ratio = new_ratio
            msg = 'The best match I found is this post: <a href="{}">{}</a>.'.format(self.base_url + best,
                                                                                     self.posts_dict[best])
        return msg
