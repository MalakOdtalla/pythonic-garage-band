from pythonic_garage_band.pythonic_garage_band import Guitarist, Drummer, Bassist, Band, Musician
import pytest

def test_guitarist_play_solos():
    expected = 'Guitarist is playing solo on the guitar'
    actual = Guitarist('Guitarist', 'guitar').play_solos()
    assert expected == actual

