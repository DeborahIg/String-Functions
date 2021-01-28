import main

def test_capitalise_string ():
    assert main.capitalise_string ('eggs') == 'EGGS' 
    assert main.capitalise_string ('bacon') == 'BACON' 
    assert main.capitalise_string ('sausage') == 'SAUSAGE' 
    assert main.capitalise_string ('eggs benedict') == 'EGGS BENEDICT' 
    assert main.capitalise_string ('bangers and 34 mash!!') == 'BANGERS AND 34 MASH!!' 


