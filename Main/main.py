import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from Services.Config.get_input import GetInput


class Main(GetInput):
    def execute_workflow(self):
        self.__my_method()

    def __my_method(self):
        pass


my_code = Main(__file__)
my_code.execute_workflow()
