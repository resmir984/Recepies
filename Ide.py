# class Ide:
#     def functionalities(self):
#         funcs=["create_file","rename","delete"]
#         return funcs
# class pycharm(Ide):
#
#     def functionalities(self):
#         funcs=super().functionalities()
#         funcs.append("execute")
#         funcs.append("debug")
#         return funcs
#
#
# py=pycharm()
# print(py.functionalities())


class Ide:
    def functionalities(self):
        funcs=["create_file","rename","delete"]
        return funcs
class pycharm(Ide):

    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("execute")
        funcs.append("debug")
        return funcs

class Vscode(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("vcs")
        funcs.append("formatting")
        return funcs
py=pycharm()
print(py.functionalities())
vsc=Vscode()
print(vsc.functionalities())