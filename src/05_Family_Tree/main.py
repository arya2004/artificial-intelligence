
from collections import defaultdict

# Parents: parents[child] = list of parents
parents = defaultdict(list)

# Add parent facts: parent(child, parent)
parents['umesh'].append('arun')
parents['mahesh'].append('arun')
parents['ashwini'].append('umesh')
parents['swara'].append('ashwini')
parents['aiya'].append('mahesh')
parents['neel'].append('pratibha')
parents['ainav'].append('prakash')

parents['umesh'].append('archana')
parents['mahesh'].append('archana')
parents['ashwini'].append('umesh')
parents['swara'].append('ashwini')
parents['aiya'].append('mahesh')
parents['neel'].append('pratibha')
parents['ainav'].append('prakash')

# Grandparents
parents['arun'].append('ganpat')
parents['archana'].append('ganpat')
parents['ganpat'].append('bhalchandra')
parents['smita'].append('bhalchandra')

# Spouses: spouses[person] = spouse (symmetric)
spouses = {}
spouse_facts = [
    ('umesh', 'ashwini'),
    ('mahesh', 'pratibha'),
    ('prashant', 'pallavi'),
    ('prakash', 'smita'),
    ('arun', 'archana'),
    ('ganpat', 'smita')
]
for a, b in spouse_facts:
    spouses[a] = b
    spouses[b] = a

# Gender facts
males = {
    'arun', 'ganpat', 'umesh', 'mahesh', 'bhalchandra',
    'prashant', 'prakash', 'neel', 'ainav'
}
females = {
    'archana', 'smita', 'pratibha', 'ashwini',
    'swara', 'pallavi', 'aiya'
}

# Define rules as functions
def is_parent(parent, child):
    """parent is parent of child"""
    return parent in parents.get(child, [])

def is_father(father, child):
    """father is father of child"""
    return is_parent(father, child) and father in males

def is_mother(mother, child):
    """mother is mother of child"""
    return is_parent(mother, child) and mother in females

def is_grandfather(gf, child):
    """gf is grandfather of child"""
    for z in parents.get(child, []):
        if is_father(gf, z):
            return True
    return False

def is_grandmother(gm, child):
    """gm is grandmother of child"""
    for z in parents.get(child, []):
        if is_mother(gm, z):
            return True
    return False

def is_sibling(x, y):
    """x and y are siblings (share at least one parent, x != y)"""
    if x == y:
        return False
    for z in parents.get(x, []):
        if z in parents.get(y, []):
            return True
    return False

def is_brother(bro, sib):
    """bro is brother of sib"""
    return is_sibling(bro, sib) and bro in males

def is_sister(sis, sib):
    """sis is sister of sib"""
    return is_sibling(sis, sib) and sis in females

def is_uncle(unc, child):
    """unc is uncle of child"""
    for z in parents.get(child, []):
        if is_brother(unc, z):
            return True
    return False

def is_aunt(aun, child):
    """aun is aunt of child"""
    for z in parents.get(child, []):
        if is_sister(aun, z):
            return True
    return False


