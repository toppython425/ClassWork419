# class Group(object):
#
#     def __init__(self, members: list):
#         self.members = members
#
#     def __len__(self):
#         return int(len(self.members) / 2)
#
#
# group = Group(['Иван', 'Мария', 'Peter'])
# print(len(group))


class Group(object):

    def __init__(self, members: list):
        self.members = members

    def __len__(self):
        return len(self.members)


group = Group(['Иван', 'Мария', 'Peter'])
print(len(group))
