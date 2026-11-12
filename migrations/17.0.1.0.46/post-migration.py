# -*- coding: utf-8 -*-
"""v46 upgrade -- declare 4 Studio fields on product.pricelist.

Ports the Clear-DB Studio schema:
  * x_studio_group_type (Selection: General/Distributor/Dealer)
  * x_studio_order_payment_method (Selection: Cash/Credit)
  * x_studio_project_price_list (Boolean)
  * x_studio_zzzz (Selection: Normal/Low/High/Very High)

Required by seeding_test_data v0.0.6+ so pricelist rows imported
from Clear-DB write cleanly. No data migration -- fresh columns.
"""


def migrate(cr, version):
    if not version:
        return
    return
