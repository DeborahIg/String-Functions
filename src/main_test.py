import main

def test_capitalise_string ():
    assert main.capitalise_string ('eggs') == 'EGGS' 
    assert main.capitalise_string ('bacon') == 'BACON' 
    assert main.capitalise_string ('sausage') == 'SAUSAGE' 
    assert main.capitalise_string ('eggs benedict') == 'EGGS BENEDICT' 
    assert main.capitalise_string ('bangers and 34 mash!!') == 'BANGERS AND 34 MASH!!' 


def test_decapitalise_string ():
    assert main.decapitalise_string ('EGGS') == 'eggs' 
    assert main.decapitalise_string ('BACON') == 'bacon' 
    assert main.decapitalise_string ('SAUSAGE') == 'sausage' 
    assert main.decapitalise_string ('MILK AND YOGHURT') == 'milk and yoghurt' 
    assert main.decapitalise_string ('HASUH98£') == 'hasuh98£' 

def test_cap_string ():
    assert main.cap_first ('eggs') == 'Eggs' 
    assert main.cap_first ('bacon') == 'Bacon' 
    assert main.cap_first ('sausage') == 'Sausage' 
    assert main.cap_first ('my milk') == 'My milk' 
    assert main.cap_first('ha8$') == 'Ha8$'
    assert main.cap_first ('8a') == '8a'

