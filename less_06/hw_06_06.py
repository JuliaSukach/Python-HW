# На ресурсе https://json.org/example.html взять пример json "web-app"
# Сохранить в файл. Написать ф-ю, которая принимает массив ключей, по которым будет проходить поиск в данном json-объекте.
# Ф-я должна возвращать список вида:
# [
#     ["key", ["val_1", "val_2"]]
# ].
# Необходимо учесть вложенность объектов и проверку на несуществующий ключ. Если ключа нет - в результир набор он не попадает,
# переход к след ключу.

import json

with open('web-app.json', 'r') as file:
    json_data = json.load(file)

result = []
cache = {}


def get_vals_by_tag(keys, data):
    def make_record_to_result(value, obj):
        if cache.get(value) is None:
            result.append([value, [obj]])
            cache.update({value: len(result) - 1})
        else:
            result[cache.get(value)][1].append(obj)

    def get_val(k, d):
        if not isinstance(d, dict) and not isinstance(d, list):
            return

        if isinstance(d, dict) or isinstance(d, list):
            if k in d:
                make_record_to_result(k, d[k])
                return

        for val in d.values() if isinstance(d, dict) else d:
            get_val(k, val)

    for key in keys:
        get_val(key, data)

    return result

assert get_vals_by_tag(['servlet-mapping', 'aa'], json_data) == [['servlet-mapping', [{
    "cofaxCDS": "/",
    "cofaxEmail": "/cofaxutil/aemail/*",
    "cofaxAdmin": "/admin/*",
    "fileServlet": "/static/*",
    "cofaxTools": "/tools/*"}]]]
