"""Break duplicate XML ids that point at the same ir.actions.server record.

Why this exists
---------------
The Studio-numbered XML ids carry the *Clear-DB* database ids of the server
actions they were exported from (``server_action_2336_sls_validate_mobile``).
Those numbers are plain sequence values, so they do not line up with the ids
the same actions get in any other database. When the Studio xmlids were mapped
onto local records, two different BugFix-Sales names ended up bound to one
record:

    BugFix-Sales.action_sls_request_approval_sent_validate -> ir.actions.server(2336)
    BugFix-Sales.action_sls_validate_mobile                -> ir.actions.server(2336)

The two are not the same action and they do not even share a model:
``action_sls_validate_mobile`` is a res.partner action driven by the
``automation_sls_validate_mobile`` rule (data/res_partner_data.xml), while
``action_sls_request_approval_sent_validate`` is a sale.order action
(data/sale_order_data.xml).

With both names on one record the module cannot load. res_partner_data.xml is
loaded first: it rewrites the shared record to res.partner and links the
automation rule to it. sale_order_data.xml is loaded next and rewrites the very
same record to sale.order, which trips base_automation's coherency constraint:

    Model of action SLS - Request Approval Sent - Validate should match
    the one from automated rule SLS - Validate Mobile.

Fix
---
Keep the first binding and drop the later duplicates. The surviving name keeps
the record (and its id, so references to it stay valid); each dropped name has
no record left, so the data file that declares it creates a fresh one on this
same upgrade. Nothing is deleted except the surplus ir_model_data alias -- no
ir.actions.server row is touched.

Scoped to this module's own xmlids, and to ir.actions.server, which is where
the collision happens; a duplicate pointing at a record of some other model is
left alone rather than guessed at.
"""

import logging

_logger = logging.getLogger(__name__)

MODULE = "BugFix-Sales"
MODEL = "ir.actions.server"


def _duplicate_groups(cr):
    """res_id -> ordered list of (ir_model_data.id, xmlid name), duplicates only."""
    cr.execute(
        """
        SELECT res_id, id, name
          FROM ir_model_data
         WHERE module = %s
           AND model = %s
           AND res_id IN (
                 SELECT res_id
                   FROM ir_model_data
                  WHERE module = %s
                    AND model = %s
                  GROUP BY res_id
                 HAVING count(*) > 1
               )
         ORDER BY res_id, id
        """,
        (MODULE, MODEL, MODULE, MODEL),
    )
    groups = {}
    for res_id, data_id, name in cr.fetchall():
        groups.setdefault(res_id, []).append((data_id, name))
    return groups


def migrate(cr, version):
    if not version:
        return

    groups = _duplicate_groups(cr)
    if not groups:
        return

    drop_ids = []
    for res_id, entries in sorted(groups.items()):
        keep_id, keep_name = entries[0]
        dropped = entries[1:]
        drop_ids.extend(data_id for data_id, _name in dropped)
        _logger.info(
            "Duplicate xmlids on %s(%s): keeping %s.%s, dropping %s "
            "(each dropped name is recreated from its own data file)",
            MODEL,
            res_id,
            MODULE,
            keep_name,
            ", ".join(f"{MODULE}.{name}" for _data_id, name in dropped),
        )

    cr.execute("DELETE FROM ir_model_data WHERE id IN %s", (tuple(drop_ids),))
    _logger.info("Dropped %s duplicate ir_model_data alias(es)", len(drop_ids))
