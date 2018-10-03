from soundex import getSoundEx

def test_get_sound_ex():
    assert getSoundEx('Jon') == 'J500'
    assert getSoundEx('John') == 'J500'
    assert getSoundEx('Matt') == 'M300'
    assert getSoundEx('Matthew') == 'M300'
    assert getSoundEx('anna') == 'A500'
    assert getSoundEx('ana') == 'A500'
    assert getSoundEx('erika') == 'E620'
    assert getSoundEx('pam') == 'P500'
