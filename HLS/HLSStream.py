from pathlib import Path
from typing import Optional

from HLS.config import HLSStreamOptions


class HLSStream:
    def __init__(self, config: Optional[HLSStreamOptions] = None):
        self.config = config
        self.hls_stream: Optional[HLSStreamInstance] = None

    def __enter__(self):
        self.hls_stream = HLSStreamInstance(config=self.config)

    def __exit__(self, _, __, ___):
        if self.hls_stream is not None:
            self.hls_stream.close()


class HLSStreamInstance:
    def __init__(self, config: Optional[HLSStreamOptions] = None):
        self.config = config

        if config is None:
            self.config = HLSStreamOptions()

    def close(self):
        pass

    def feed_video(self, src: Path):
        pass

    def feed_image(self, src: Path):
        pass
