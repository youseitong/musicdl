'''initialize'''
import importlib
from .base import BaseMusicClient
from ..utils import BaseModuleBuilder


def _lazyimport(module_path: str, cls_name: str):
    def _factory(**kwargs):
        module = importlib.import_module(module_path, package=__package__)
        cls = getattr(module, cls_name)
        return cls(**kwargs)
    return _factory


'''MusicClientBuilder'''
class MusicClientBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        # Platforms in Greater China
        'QQMusicClient': _lazyimport('.qq', 'QQMusicClient'),                   'KugouMusicClient': _lazyimport('.kugou', 'KugouMusicClient'),              'StreetVoiceMusicClient': _lazyimport('.streetvoice', 'StreetVoiceMusicClient'),   'SodaMusicClient': _lazyimport('.soda', 'SodaMusicClient'),               'FiveSingMusicClient': _lazyimport('.fivesing', 'FiveSingMusicClient'),
        'NeteaseMusicClient': _lazyimport('.netease', 'NeteaseMusicClient'),    'QianqianMusicClient': _lazyimport('.qianqian', 'QianqianMusicClient'),      'MiguMusicClient': _lazyimport('.migu', 'MiguMusicClient'),               'KuwoMusicClient': _lazyimport('.kuwo', 'KuwoMusicClient'),               'BilibiliMusicClient': _lazyimport('.bilibili', 'BilibiliMusicClient'),
        # Global Streaming / Indie
        'YouTubeMusicClient': _lazyimport('.youtube', 'YouTubeMusicClient'),    'JooxMusicClient': _lazyimport('.joox', 'JooxMusicClient'),                 'AppleMusicClient': _lazyimport('.apple', 'AppleMusicClient'),            'JamendoMusicClient': _lazyimport('.jamendo', 'JamendoMusicClient'),      'SoundCloudMusicClient': _lazyimport('.soundcloud', 'SoundCloudMusicClient'),
        'DeezerMusicClient': _lazyimport('.deezer', 'DeezerMusicClient'),       'QobuzMusicClient': _lazyimport('.qobuz', 'QobuzMusicClient'),              'SpotifyMusicClient': _lazyimport('.spotify', 'SpotifyMusicClient'),      'TIDALMusicClient': _lazyimport('.tidal', 'TIDALMusicClient'),
        # Audio / Radio
        'XimalayaMusicClient': _lazyimport('..audiobooks.ximalaya', 'XimalayaMusicClient'),         'LizhiMusicClient': _lazyimport('..audiobooks.lizhi', 'LizhiMusicClient'),    'QingtingMusicClient': _lazyimport('..audiobooks.qingting', 'QingtingMusicClient'),   'LRTSMusicClient': _lazyimport('..audiobooks.lrts', 'LRTSMusicClient'),
        # Aggregators / Multi-Source Gateways
        'MP3JuiceMusicClient': _lazyimport('..common.mp3juice', 'MP3JuiceMusicClient'),             'TuneHubMusicClient': _lazyimport('..common.tunehub', 'TuneHubMusicClient'), 'GDStudioMusicClient': _lazyimport('..common.gdstudio', 'GDStudioMusicClient'),      'MyFreeMP3MusicClient': _lazyimport('..common.myfreemp3', 'MyFreeMP3MusicClient'),   'JBSouMusicClient': _lazyimport('..common.jbsou', 'JBSouMusicClient'),
        # Unofficial Download Sites / Scrapers
        'MituMusicClient': _lazyimport('..thirdpartysites.mitu', 'MituMusicClient'),                 'BuguyyMusicClient': _lazyimport('..thirdpartysites.buguyy', 'BuguyyMusicClient'),  'GequbaoMusicClient': _lazyimport('..thirdpartysites.gequbao', 'GequbaoMusicClient'),    'YinyuedaoMusicClient': _lazyimport('..thirdpartysites.yinyuedao', 'YinyuedaoMusicClient'),  'FLMP3MusicClient': _lazyimport('..thirdpartysites.flmp3', 'FLMP3MusicClient'),
        'FangpiMusicClient': _lazyimport('..thirdpartysites.fangpi', 'FangpiMusicClient'),          'FiveSongMusicClient': _lazyimport('..thirdpartysites.fivesong', 'FiveSongMusicClient'),  'KKWSMusicClient': _lazyimport('..thirdpartysites.kkws', 'KKWSMusicClient'),              'GequhaiMusicClient': _lazyimport('..thirdpartysites.gequhai', 'GequhaiMusicClient'),       'LivePOOMusicClient': _lazyimport('..thirdpartysites.livepoo', 'LivePOOMusicClient'),
        'HTQYYMusicClient': _lazyimport('..thirdpartysites.htqyy', 'HTQYYMusicClient'),             'JCPOOMusicClient': _lazyimport('..thirdpartysites.jcpoo', 'JCPOOMusicClient'),        'TwoT58MusicClient': _lazyimport('..thirdpartysites.twot58', 'TwoT58MusicClient'),          'ZhuolinMusicClient': _lazyimport('..thirdpartysites.zhuolin', 'ZhuolinMusicClient'),
    }


'''BuildMusicClient'''
BuildMusicClient = MusicClientBuilder().build
