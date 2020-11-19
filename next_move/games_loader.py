from typing import TextIO, List
from io import StringIO
import requests
import chess.pgn
import logging

logger = logging.getLogger('GamesLoader')


class GamesLoader:
    def __init__(self):
        self.board: Board = None

    @staticmethod
    def load_from_file(source: str) -> List[chess.pgn.Game]:
        pgn_text: TextIO = None
        try:
            pgn_text = open(source)
        except IOError as e:
            logger.error('Could not open file "%s": %s', source, e)
            return None

        games: List[chess.pgn.Game] = GamesLoader._load_games(pgn_text)
        pgn_text.close()
        return games

    @staticmethod
    def load_from_url(source: str) -> List[chess.pgn.Game]:
        try:
            url_content = requests.get(source)
            pgn_text = StringIO(url_content.text)
        except requests.exceptions.RequestException as e:
            logger.error('Could not open url "%s": %s', source, e)
            return None

        games: List[chess.pgn.Game] = GamesLoader._load_games(pgn_text)
        pgn_text.close()
        return games

    @staticmethod
    def _load_games(loaded_pgn: TextIO) -> List[chess.pgn.Game]:
        games: List[chess.pgn.Game] = []

        while True:
            try:
                loaded_game = chess.pgn.read_game(loaded_pgn)
            except ValueError as e:
                logger.error('Error occured: %s', e)
                break
            if loaded_game is None or len(loaded_game.errors) > 0:
                break
            games.append(loaded_game)

        return games
