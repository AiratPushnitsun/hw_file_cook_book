def create_cook_book():
    with open('cook_book.txt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dishes_name = line.strip()
            ingridient_count = int(f.readline())
            ingridient = []
            for i in range(ingridient_count):
                ing = f.readline().strip()
                ingridient_name, quantity, measure = ing.split(' | ')
                ingridient.append({
                    'ingridient_name': ingridient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            f.readline()
            cook_book[dishes_name] = ingridient
        return cook_book



def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book()
    dict_by_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                ingr["quantity"] *= person_count
                if ingr['ingridient_name'] not in dict_by_dishes:
                    pop_ingr = ingr.pop('ingridient_name')
                    dict_by_dishes[pop_ingr] = ingr
                else:
                    pop_ingr = ingr.pop('ingridient_name')
                    dict_by_dishes[pop_ingr]['quantity'] += ingr['quantity']

    return dict_by_dishes

res = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4)
import pprint
pprint.pprint(res, stream=None, indent=1, width=150, depth=2, compact=False, sort_dicts=False)
