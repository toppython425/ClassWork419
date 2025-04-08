# class User:
#     def save(self, validate=True):
#         pass
#
#
# class Product:
#     def save(self):
#         pass
#
#
# def save_all(models):
#     for model in models:
#         model.save()

class User:
    def save(self, **kwargs):
        pass


class Product:
    def save(self, **kwargs):
        pass


def save_all(models):
    for model in models:
        model.save()


if __name__ == '__main__':
    user = User()
    product = Product()
    my_models = [user, product]
    save_all(my_models)
