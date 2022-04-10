from unittest import TestCase

from asyncdown import __main__ as adown_main

class TestDateFormats(TestCase):

    def test_call_with_nor_args(self):
        ''' test required stands'''
        with self.assertRaises(SystemExit):
            adown_main.command_line_parser([])

    def test_call_with_verbose(self):
        args = adown_main.command_line_parser(['-v','-u','url/file.zip' ])
        self.assertNotEqual(args.verbose, False )

    def test_verbose_default_false(self):
        args = adown_main.command_line_parser(['-u', 'url/file.zip'])
        self.assertEqual(args.verbose, False )

    def test_call_with_url(self):
        args = adown_main.command_line_parser(['-u', 'url/url1/file.zip'])

        self.assertEqual(args.urls_list, ['url/url1/file.zip',] )

    def test_call_with_url_named(self):
        args = adown_main.command_line_parser(['--urls-list', 'url/url1/file.zip'])

        self.assertEqual(args.urls_list, ['url/url1/file.zip',] )
