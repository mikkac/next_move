import unittest

import sys
sys.path.insert(0, '..')
from next_move.games_loader import GamesLoader


class GamesLoaderTest(unittest.TestCase):
    def test_load_from_file_success(self):
        pgn_path = 'pgn_file_01.txt'
        expected_number_of_games = 249
        obtained_number_of_games = len(GamesLoader.load_from_file(pgn_path))
        self.assertEqual(obtained_number_of_games, expected_number_of_games)

    def test_load_from_file_failure_empty_file(self):
        pgn_path = 'empty_file.txt'
        expected_number_of_games = 0
        obtained_number_of_games = len(GamesLoader.load_from_file(pgn_path))
        self.assertEqual(obtained_number_of_games, expected_number_of_games)

    def test_load_from_file_failure_nonexistent_file(self):
        pgn_path = 'does_not_exist'
        expected_games = None
        obtained_games = GamesLoader.load_from_file(pgn_path)
        self.assertEqual(obtained_games, expected_games)

    def load_from_url_success(self):
        self.assertTrue('FOO'.isupper())


if __name__ == '__main__':
    unittest.main()
