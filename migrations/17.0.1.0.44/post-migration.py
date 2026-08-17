# -*- coding: utf-8 -*-
"""v44 upgrade -- declare two line-level Studio fields required by
Fix-repair v283's port of the Track Lock Status automations.

  * x_studio_re_estimated (Boolean, per-line marker)
  * x_studio_count_1      (Integer, per-line re-estimate instance)

Written by Fix-repair v283 via an onchange handler on sale.order.line.
Read by Fix-repair v283's sale.order write override (which searches the
most recent re-estimated line to compute the header's target
re_estimate_count).

No data migration -- fresh columns default to False / 0 on existing
rows, which is what pre-re-estimation state should look like anyway.
"""


def migrate(cr, version):
    if not version:
        return
    return
