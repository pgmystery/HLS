from dataclasses import dataclass

from HLS.config.playlist import HLSPlaylistConfig
from HLS.config.video_chunks import HLSVideoChunksConfig


@dataclass
class HLSStreamOptions:
    playlist: HLSPlaylistConfig = HLSPlaylistConfig()
    video_chunks: HLSVideoChunksConfig = HLSVideoChunksConfig()
