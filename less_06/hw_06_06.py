# На ресурсе https://json.org/example.html взять пример json "web-app"
# Сохранить в файл. Написать ф-ю, которая принимает массив ключей, по которым будет проходить поиск в данном json-объекте.
# Ф-я должна возвращать список вида:
# [
#     ["key", ["val_1", "val_2"]]
# ].
# Необходимо учесть вложенность объектов и проверку на несуществующий ключ. Если ключа нет - в результир набор он не попадает,
# переход к след ключу.

import json


def get_vals_by_tag(keys):
    result = []
    with open('web-app.json', 'r') as file:
        data = json.load(file)
        cache = {}

        def if_type_is_changed(obj):
            return type(obj) in [dict, list]

        def if_value_in_keys(v):
            return v in keys

        def search(obj):
            for v in obj:
                if if_value_in_keys(v):
                    if cache.get(v) is None:
                        result.append([v, [obj.get(v)]])
                        cache.update({v: len(result) - 1})
                    else:
                        result[cache.get(v)][1].append(obj.get(v))
                else:
                    if if_type_is_changed(v):
                        search(v)
                    elif if_type_is_changed(obj[v]):
                        search(obj[v])

        search(data)
        return result


assert get_vals_by_tag(['servlet-mapping', "AA"]) == [['servlet-mapping', [{
      "cofaxCDS": "/",
      "cofaxEmail": "/cofaxutil/aemail/*",
      "cofaxAdmin": "/admin/*",
      "fileServlet": "/static/*",
      "cofaxTools": "/tools/*"}]]]
