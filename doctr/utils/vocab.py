import logging
import platform
import os

__all__ = ["get_vocab"]


def get_vocab(language: str):

    vocab_path = os.path.join("doctr", "vocabs", f"{language}.txt")
    if not os.path.exists(vocab_path):
        logging.warning(f"unable to load vocab at path : {vocab_path}")

    with open(vocab_path, "r", encoding="utf-8") as f:
        data = f.read()

    return data
