import re

def step1(new_id):
    return new_id.lower()

def step2(new_id):
    return re.sub('[^a-z0-9\-_.]', '', new_id)

def step3(new_id):
    return re.sub('\.{2,}', '.', new_id)

def step4(new_id):
    new_id = new_id.strip('.')
    return new_id if new_id != '' else 'a'

def step5(new_id):
    return new_id[:15].rstrip('.')

def step6(new_id):
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id

def solution(new_id):
    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    return new_id