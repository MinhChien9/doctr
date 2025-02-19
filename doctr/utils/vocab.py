import logging
import platform
import os
from pathlib import Path

__all__ = ["get_vocab"]


def get_vocab(language: str):
    data = ""
    vocab_path = Path(__file__).parent.parent / "vocabs" / f"{language}.txt"
    if not os.path.exists(vocab_path):
        logging.warning(f"unable to load vocab at path : {vocab_path}")
    else:
        with open(vocab_path, "r", encoding="utf-8") as f:
            data = f.read()

    return data
