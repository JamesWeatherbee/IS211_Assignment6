#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import conversions


class KnownValues(unittest.TestCase):
    knownvals = ((270.00, 518.00, 543.15),
                 (200.00, 392.00, 473.15),
                 (120.00, 248.00, 393.15),
                 (0.00, 32.00, 273.15),
                 (-273.15, -459.67, 0.00))

    def testCelsiustoKelvin(self):
        for val in self.knownvals:
            c = val[0]
            k = val[2]
            expect = conversions.convertCelsiusToKelvin(c)
            self.assertEqual(expect, k, msg=('{} degrees K '
                                             'is not equal to {}'
                                             ' degrees K.').format(c, k))

    def testCelsiustoFahrenheit(self):
        for val in self.knownvals:
            c = val[0]
            f = val[1]
            expect = conversions.convertCelsiusToFahrenheit(c)
            self.assertEqual(expect, f, msg=('{} degrees F '
                                             'is not equal to {}'
                                             ' degrees F.').format(c, f))

    def testFahrenheitToCelsius(self):
        for val in self.knownvals:
            f = val[1]
            c = val[0]
            expect = conversions.convertFahrenheitToCelsius(f)
            self.assertEqual(expect, c, msg=('{} degrees C '
                                             'is not equal to {}'
                                             ' degrees C.').format(f, c))

    def testFahrenheitToKelvin(self):
        for val in self.knownvals:
            f = val[1]
            k = val[2]
            expect = conversions.convertFahrenheitToKelvin(f)
            self.assertEqual(expect, k, msg=('{} degrees K '
                                             'is not equal to {}'
                                             ' degrees K.').format(f, k))

    def testKelvinToCelsius(self):
        for val in self.knownvals:
            k = val[2]
            c = val[0]
            expect = conversions.convertKelvinToCelsius(k)
            self.assertEqual(expect, c, msg=('{} degrees C '
                                             'is not equal to {}'
                                             ' degrees C.').format(k, c))

    def testKelvinToFahrenheit(self):
        for val in self.knownvals:
            k = val[2]
            f = val[1]
            expect = conversions.convertKelvinToFahrenheit(k)
            self.assertEqual(expect, f, msg=('{} degrees F '
                                             ' is not equal to {}'
                                             ' degrees F.').format(k, f))


if __name__ == '__main__':
    unittest.main()