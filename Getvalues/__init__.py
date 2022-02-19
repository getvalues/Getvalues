"""
    get属性：
        作用：查找字典中的某个key值：
        语法：
        '>>> import Getvalues
        '>>> a = {'name': 'zph','phone':{'a':1,'b':[{'a':1},{'b',2}]}}
        '>>> g = Getvalues.get('a', a)
        '>>> g  // [1,1]  出现重复key名时，会按照从上到下的顺序返回多个值
"""

__author__ = "zph"
__version__ = "1.0.0"
__copyright__ = "Copyright (c) Mystery man"


class GetData(object):
    def __init__(self):
        self.Spider_data = []

    def check_list(self, name, data):
        for i in range(len(data)):
            for o in data[i].keys():
                if o == name:
                    self.Spider_data.append(data[i][o])
                elif isinstance(data[i][o], dict):
                    self.Spider_data += GetData().check_get(name, data[i][o])
                elif isinstance(data[i][o], list):
                    self.Spider_data += GetData().check_list(name, data[i][o])
        return self.Spider_data

    def check_get(self, name, data):
        for i in data.keys():
            if i == name:
                self.Spider_data.append(data[i])
            elif isinstance(data[i], dict):
                self.Spider_data += GetData().check_get(name, data[i])
            elif isinstance(data[i], list):
                self.Spider_data += GetData().check_list(name, data[i])
        return self.Spider_data

    def __str__(self):
        return 'Spider_是一个轻松获取字典中某个key的值的包。'


def get(name, data):
    """Easily obtain key values in JSON
    :param name: key
    :param data: json data
    :return: : list data
    :rtype: Getvalues.get
    """
    if isinstance(data, str):
        data = eval(data)
        return GetData().check_get(name, data)
    else:
        return GetData().check_get(name, data)


# if __name__ == '__main__':
    # 这里用于开发者调试，请勿修改。
    # test = {
    #     'name': 'Getvalues',
    #     'age': 1,
    #     'function': [
    #         {'q1': 1},
    #     ]
    # }
    # s = get('q1', test)
    # print(s)
