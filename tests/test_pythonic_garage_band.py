from pythonic_garage_band.pythonic_garage_band import  Musician, Band,Guitarist, Bassist, Drummer
import pytest


# Band Member Names


def test_name_musician():
  actual = Musician('John')
  assert 'John' == actual.name

def test_name_bass():
  actual = Bassist('Paul')
  assert 'Paul' == actual.name

def test_name_guitar():
  actual = Guitarist('George')
  assert 'George' == actual.name

def test_name_drummer():
  actual = Drummer('Ringo')
  assert 'Ringo' == actual.name


# Get Instrument Tests


def test_musician_instrument():
  actual = Musician('Name')
  assert 'Nothing' == actual.get_instrument()

def test_get_guitar():
  actual = Guitarist('Slash')
  assert 'Guitar' == actual.get_instrument()

def test_get_bass():
  actual = Bassist('Who Plays Bass Again?')
  assert 'Bass' == actual.get_instrument()

def test_get_drums():
  actual = Drummer('Insert Name')
  assert 'Drums' == actual.get_instrument()


# Test Solos


def test_guitar_solo():
  actual = Guitarist('An Actual Ukulele')
  assert 'Guitar Sounds' == actual.play_solo()

def test_bass_solo():
  actual = Bassist('A Really Big Ukulele')
  assert 'Bass Sounds' == actual.play_solo()

def test_drum_solo():
  actual = Drummer('Silence')
  assert 'LOUD NOISES' == actual.play_solo()

def test_all_band_solos():
  actual = Band('Test Band', [Guitarist('Wham'), Drummer('Bam'), Bassist('Shang-a-lang')])
  assert 'Guitar Sounds LOUD NOISES Bass Sounds ' == actual.play_solos()

band_one = """
Catfish and the Bottlemen
Van McCann,Guitar
Jon Barr,Drums
Benji Blakeway,Bass
Bob Hall,Guitar
"""
band_two = """
Louis the Child
Robby,Bass
Freddy,Bass
"""

#  Output Tests

def test_str_output():
  test_band = Band.create_from_data(band_one)
  expected = """The Band's Name is: Catfish and the Bottlemen
The Members are:
Van McCann on Guitar
Jon Barr on Drums
Benji Blakeway on Bass
Bob Hall on Guitar
"""
  assert expected == test_band.__str__()

def test_diff_str_output():
  test_band = Band.create_from_data(band_two)
  expected = """The Band's Name is: Louis the Child
The Members are:
Robby on Bass
Freddy on Bass
"""
  assert expected == test_band.__str__()

def test_all_bands_list():
  Band.create_from_data(band_one)
  Band.create_from_data(band_two)
  expected = """The Band's Name is: Catfish and the Bottlemen
The Members are:
Van McCann on Guitar
Jon Barr on Drums
Benji Blakeway on Bass
Bob Hall on Guitar
The Band's Name is: Louis the Child
The Members are:
Robby on Bass
Freddy on Bass
"""
  assert expected == Band.to_list()
