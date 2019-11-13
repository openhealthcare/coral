"""
Episode Category for Coral
"""
from opal.core import episodes


class CoralEpisode(episodes.EpisodeCategory):
    display_name    = 'Episode'
    detail_template = 'detail/episode.html'
