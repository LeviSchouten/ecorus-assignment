class Office():

    def __init__(self, name):
        self.name = name
        self.people_working = []

    def start_working_for(self, person):
        self.people_working.append(person)

    def finished_working_for(self, person):
        if person in self.people_working:
            self.people_working.remove(person)
