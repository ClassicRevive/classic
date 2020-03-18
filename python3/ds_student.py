#!/usr/bin/env python3

from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1 = {'CA103': Module('CA103', 'Computer Systems', 5),
       'CA106': Module('CA106', 'Web Design', 5),
       'CA115': Module('CA115', 'Digital Innovation', 5),
       'CA116': Module('CA116', 'Computer Programming I', 10),
       'CA117': Module('CA117', 'Computer Programming II', 10),
       'CA169': Module('CA169', 'Networks and Internet', 5),
       'CA170': Module('CA170', 'Operating Systems', 5),
       'CA172': Module('CA172', 'Problem Solving', 5),
       'MS121': Module('MS121', 'IT Mathematics', 10)}

DS1 = {'CA115': Module('CA120', 'Collaboration and Innovation', 5),
       'MS103': Module('MS103', 'Linear Mathematics I', 5),
       'MS104': Module('MS104', 'Linear Mathematics II', 5),
       'CA115': Module('CA115', 'Digital Innovation', 5),
       'CA116': Module('CA116', 'Computer Programming I', 10),
       'CA117': Module('CA117', 'Computer Programming II', 10),
       'MS129': Module('MS129', 'Calculus I', 5),
       'MS130': Module('MS130', 'Calculus II', 5),
       'MS117': Module('MS117', 'Probability I', 5),
       'CA119': Module('CA119', 'Databases and Data structures', 5)}


class Student(object):
    def __init__(self, idnum, surname, firstname, course):
        self.idnum = idnum
        self.surname = surname
        self.firstname = firstname
        self.tc = 0
        
        if course == "ds1" or course == "DS1":
            self.mods = DS1
        elif course == "CA1" or course == "ca1":
            self.mods = CA1

        self.marks = {code: 0 for code in self.mods.keys()}


        for m in self.mods:
            self.tc += self.mods[m].ects

    def __str__(self):  # table format for student data
        name = '{} : {} {}'.format(self.idnum,
                                   self.firstname,
                                   self.surname)
        uline = '-' * len(name)
        results =  '\n'.join(
            [code + ' : ' + self.mods[code].title + ' : ' + str(
                self.marks[code]) for code in sorted(self.mods.keys())])

        pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            outcome = 'Pass'
        elif self.passed_by_compensation():
            outcome = 'Pass by compensation'
        else:
            outcome = 'Fail'

        return '\n'.join([name, uline, results, pm, outcome])

    def add_mark(self, code, mark):
        # update the mark in the marks dictionary

        self.marks[code] = mark

    def precision_mark(self):
        # add the weighted average of the mark in that module
        # to the avg total
        avg = 0
        for module in self.mods:
            weighted_mark = self.marks[module] * (self.mods[module].ects / self.tc)
            avg += weighted_mark

        return avg

    def passed(self):
        passed = True
        for code, marks in self.marks.items():
            if marks < 40:
                passed = False

        return passed

    def passed_by_compensation(self):
        # calculate how much credits are recieved based on pass or fail
        mincreds = self.tc - ((1 / len(self.marks)) * self.tc)
        credits = 0
        for code, marks in self.marks.items():
            if 39 < marks:
                credits += self.mods[code].ects

        # linear search for any marks below 35
        over35 = True
        for code, marks in self.marks.items():
            if marks < 35:
                over35 = False
                break

        return 44 < self.precision_mark() and mincreds <= credits and over35
