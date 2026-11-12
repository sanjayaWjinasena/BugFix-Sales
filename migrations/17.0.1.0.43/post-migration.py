# -*- coding: utf-8 -*-
"""v43 upgrade — declare x_studio_price_unit_original on
sale.order.line so Fix-repair v279's RUG-repricing override has
somewhere to write the pre-reset price.

Ports the corresponding Studio state='manual' field to state='base';
existing values (Clear-DB) are preserved because the column name is
unchanged.

No data migration; declaration alone flips ownership.
"""


def migrate(cr, version):
    if not version:
        return
    return
