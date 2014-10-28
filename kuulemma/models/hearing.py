# -*- coding: utf-8 -*-
from kuulemma.extensions import db

from .text_item_mixin import TextItemMixin


class Hearing(db.Model, TextItemMixin):
    __versioned__ = {}
    __tablename__ = 'hearing'
