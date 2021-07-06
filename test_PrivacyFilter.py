import unittest
from PrivacyFilter import PrivacyFilter


def file_to_samples(file, dir="test_samples", delimiter="~"):
    with open("{dir}/{file}".format(dir=dir,file=file)) as f:
        for line in f.readlines():
            line = line.rstrip()
            yield tuple(line.split(delimiter))


class PFTest(unittest.TestCase):
    def setUp(self):
        pass
        self.pfilter = PrivacyFilter()
        self.pfilter.initialize(clean_accents=True, nlp_filter=False)


class TestRegex(PFTest):
    def test_url(self):
        for sample in file_to_samples("url.txt"):
            dirty, clean = sample
            self.assertEqual(self.pfilter.remove_url(dirty), clean)

    def test_email(self):
        for sample in file_to_samples("email.txt"):
            dirty, clean = sample
            self.assertEqual(self.pfilter.remove_email(dirty), clean)

    def test_date(self):
        for sample in file_to_samples("date.txt"):
            dirty, clean = sample
            self.assertEqual(self.pfilter.remove_dates(dirty), clean)

    def test_postal_codes(self):
        for sample in file_to_samples("postal_codes.txt"):
            dirty, clean = sample
            self.assertEqual(self.pfilter.remove_postal_codes(dirty), clean)

    def test_numbers(self):
        for sample in file_to_samples("numbers.txt"):
            dirty, clean = sample
            self.assertEqual(self.pfilter.remove_numbers(dirty), clean)

if __name__ == '__main__':
    unittest.main()
