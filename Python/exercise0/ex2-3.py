import json

family = {
    "dad" : [{"name" : "Jeongmo", "age" : 61, "birthday" : "1960.08.22"}],
    "mom" : [{"name" : "Sooyoung", "age" : 60, "birthday" : "1961.11.16"}],
    "anniversary" : "12 March",
    "child" : [{"name" : "Jeonghwa", "age" : 31, "birthday" : "1990.04.20"},
    {"name" : "Youjo", "age" : 30, "birthday" : "1991.11.09"},
    {"name" : "Soyoung", "age" : 24, "birthday" : "1997.03.11"}
        ]
    }
    
print(json.dumps(family, indent=4, separators=(" ", " : ")))
y = family.get("anniversary")
print(y)
x = family.keys()
print(x)
family["city"] = "Seoul"
print(x)
w = family.values()
print(w)
family["anniversary"] = "March 12"
print(w)

"""
import json
dad = {"name" : "Jeongmo", "age" : 61, "birthday" : "1960.08.22"},
mom = {"name" : "Sooyoung", "age" : 60, "birthday" : "1961.11.16"},
jeonghwa = {"name" : "Jeonghwa", "age" : 31, "birthday" : "1990.04.20"},
youjo = {"name" : "Youjo", "age" : 30, "birthday" : "1991.11.09"},
soyoung = {"name" : "Soyoung", "age" : 24, "birthday" : "1997.03.11"}

family = {
    "Dad" : dad,
    "Mom" : mom,
    "Jeonghwa" : jeonghwa,
    "Youjo" : youjo,
    "Soyoung" : soyoung
    }
    
print(json.dumps(family, indent=4, separators=(" ", " : ")))
"""