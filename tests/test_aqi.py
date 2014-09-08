# -*- coding: utf-8 -*-

import unittest

import aqi


class TestAqi(unittest.TestCase):
    """
    Test the aqi module
    """

    def test_to_iaqi(self):
        """Test IAQI conversion"""
        self.assertEqual(
            aqi.to_iaqi(aqi.POLLUTANT_O3_8H, '0.08753333'),
            129)

    def test_to_aqi(self):
        """Test AQI conversion"""
        self.assertEqual(
            aqi.to_aqi([
                (aqi.POLLUTANT_O3_8H, '0.077'),
                (aqi.POLLUTANT_PM25, '40.9'),
                (aqi.POLLUTANT_CO, '8.4')
            ]),
            104)