# src/strategies/__init__.py

from .simple import simple_path
from .martingale import martingale_path
from .dalembert import dalembert_path
from .multiples import multiples_path

__all__ = [
    "simple_path",
    "martingale_path",
    "dalembert_path",
    "multiples_path",
]
