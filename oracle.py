#!/usr/bin/python3
import abc


class Oracle:
    def __init__(self):
        """An oracle.py receives structured queries and replies in natural language"""
        self.general = GeneralOracle()
        self.project = ProjectOracle()
        self.publications = PublicationsOracle()

    @abc.abstractmethod
    def supported_operations(self):
        """Returns the strings of the operations supported by this oracle.py"""
        return

    def ask(self, rule):
        """Answers your question, as long as your question sticks to the grammar we have defined earlier.

        :param rule: a list composed of an operation and a list of optional parameters
        :return: a natural language answer to the question for the oracle.py
        """
        if rule[0] in self.general.supported_opperations():
            return self.general.ask(rule)
        elif rule[0] in self.project.supported_operations():
            return self.project.ask(rule)
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
    def __init__(self):
        pass

    def supported_operations(self):
        return ['blog_last', 'blog_titles', 'blog_post', 'blog_random']

    def ask(self, rule):
        return "I don't know"
