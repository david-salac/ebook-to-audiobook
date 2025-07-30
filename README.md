# Ebook To Audiobook Convertor
A simple Text To Speech (TTS) convertor usable for generating audiobooks.

Author: David Salac

## Usage
1. Install all dependencies in `requirements.txt`.
2. Set environmental variables:
   1. `PATH_TO_BOOK_TXT` <=> PATH TO THE TXT FILE TO BE READ
   2. `PATH_TO_OUTPUT_WAV` <=> PATH TO THE WAV THAT IS GENERATED
3. Run `main.py`.

## Note
The algorithm runs for a while - couple of hours - depending on your computer.

## Common Fixes
The following fixes a classic error with the origin in the `torch` package.
```python
import torch
#  keep the original loader
_orig_load = torch.load
def _safe_load(*args, **kw):
    kw.setdefault("weights_only", False)   # force full un‑pickle
    return _orig_load(*args, **kw)
torch.load = _safe_load
```
