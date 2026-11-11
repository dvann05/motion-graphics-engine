from .tech_intro import build_tech_intro
from .promo_card import build_promo_card

AVAILABLE_SCENES = {
    "tech_intro": build_tech_intro,
    "promo_card": build_promo_card,
}

__all__ = ["build_tech_intro", "build_promo_card", "AVAILABLE_SCENES"]
