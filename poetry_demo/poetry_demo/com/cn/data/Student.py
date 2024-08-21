class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        print('name = %s, score = %s: %s' % (self.name, self.score, self.get_grade()))


    def get_grade(self):
        if self.score >= 95:
            return 'EXCELLENT'
        elif self.score >= 80:
            return 'GOOD'
        else:
            return 'BAD'