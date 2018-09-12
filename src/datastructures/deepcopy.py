import copy

dict1 = {'jon': 'smith', 'jane': 'doe', 'pat': 'green'}
dict2 = {'mammal': 'dog', 'fish': 'trout', 'reptile': 'lizard'}
dict3 = {'tennis': 'racket', 'golf':'club', 'pool':'stick'}
l1 = [dict1, dict2, dict3]
l2 = l1[:]
l3 = copy.deepcopy(l1)
l1[2]['tennis'] = 'ball'

def test_get_sound_ex():
    assert l1[2]['tennis'] == 'ball'
    assert l1[2]['tennis'] == 'racket'
