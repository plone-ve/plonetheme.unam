from plonetheme.unam.testing import THEMING_INTEGRATION_TESTING

import unittest2 as unittest


class TestIntegration(unittest.TestCase):

	layer = THEMING_INTEGRATION_TESTING

	def test_availableTheme(self):
		from plone.app.theming.utils import getAvailableThemes
		from plone.app.theming.utils import getTheme

		themes = getAvailableThemes()

		self.assertEqual(len(themes), 2)