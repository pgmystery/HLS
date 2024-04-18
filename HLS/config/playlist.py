from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class HLSPlaylistConfig:
    save_path: Optional[Path] = None
