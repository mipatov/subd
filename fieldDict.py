
fields = {"CODPROG": "код НТП",
            "PROG": "Название программы",
            "F":"Номер проекта",
            "NIR":"Наименование проекта",
            "ISP":"Вуз исполнитель",
            "CODISP":"Код исполнителя",
            "SROK_N":"Год начала",
            "SROK_K":"Год окончания",
            "RUK":"Руководитель проекта",
            "RUK2":"Должность, ученая степень, ученое звание руководителя",
            "GRNTI":"код ГРНТИ",
            "NPROJ":"Кол-во проектов",
            "CODTYPE":"Характер проекта",
            "PFIN":"План. фин. на год",
            "PFIN1":"План. фин. на 1 кв.",
            "PFIN2":"План. фин. на 2 кв.",
            "PFIN3":"План. фин. на 3 кв.",
            "PFIN4":"План. фин. на 4 кв.",
            "FFIN":"Факт. фин. на год",
            "FFIN1":"Факт. фин. на 1 кв.",
            "FFIN2":"Факт. фин. на 2 кв.",
            "FFIN3":"Факт. фин. на 3 кв.",
            "FFIN4":"Факт. фин. на 4 кв."

            }

def GetFullName(name):
    name = name.upper()
    if name in fields.keys():
        return fields[name]
    else: return name

def GetTupleOfFullName(fieldsTuple):
    a = ((GetFullName(el))for el in fieldsTuple)
    return  list(a)
