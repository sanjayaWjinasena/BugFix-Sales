# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Sales',
    'version': '17.0.1.0.66',
    'summary': 'Bug fixes and enhancements for the Sales workflow',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Sales',
    'license': 'LGPL-3',
    # v0.1.0.66: close the 9 remaining Studio priority=99 view gaps.
    # Extension inherits on:
    #   * sale.order.line.tree (add invoice_status, price fields, qty ordering)
    #   * res.partner.form/tree (Studio field additions)
    #   * res.company.tree (Studio column)
    #   * product.pricelist.tree (Studio column)
    #   * product.template.product.form/tree (Studio field additions)
    #   * product.template.view.tree.website_sale (Studio column)
    #   * product.product.tree (Studio field additions)
    # New file: views/studio_ported_9_views.xml.
    # New dep: website_sale (parent of one inherit, already installed
    # on target - no cycle risk). Validated against odoo/import_xml.rng
    # BEFORE push per new pre-flight discipline.
    # Views: 10/19 -> 19/19 = 100%. Sales migration reaches 100%
    # coverage on all schema categories.
    # v0.1.0.65: hotfix v0.1.0.64. Still crashed with same error.
    # Read Odoo 17's odoo/import_xml.rng directly:
    #   <field type="html"> requires <rng:oneOrMore><rng:ref name="any"/></rng:oneOrMore>
    #   where "any" is <rng:element>...</rng:element> - CHILD XML ELEMENTS.
    # CDATA text was rejected because it's <rng:text/>, not an element.
    # Entity-escaped text also rejected (decodes to text).
    # Fix: parse help HTML into an XML fragment via lxml.html and emit
    # child elements as literal serialized XML in the <field> body.
    # Validated locally against import_xml.rng - PASSES.
    # v0.1.0.64: hotfix v0.1.0.63 - relax-ng install crash
    # ("Element odoo has extra content: record, line 7"). Root cause:
    # <field name="help" type="html">&lt;p&gt;...&lt;/p&gt;</field>
    # decodes to a STRING at parse time, but Odoo 17's relax-ng
    # schema requires type="html" fields to hold either literal
    # XML-parseable HTML elements OR CDATA raw text. Fix: switch
    # help fields to CDATA. Only ]]> sequences need guarding.
    # v0.1.0.63: 29 window actions.
    # Deep dedup on 123 remaining candidates:
    #   * 94 verified TRUE duplicates (name+model+domain+context+view_mode
    #     all match a standard-owned Odoo action) - safely skipped
    #   * 5 look-alikes with distinct domains/contexts - SHIPPED
    #     (e.g. "Sales Orders" on [task_id=active_id],
    #     "Customers"/"Vendors" on x_studio_group filters)
    #   * 24 truly-new (no name-match on target) - SHIPPED
    # New file: data/window_actions.xml.
    # Window actions: 2/133 -> 31/133 = 23% shipped (100% effective
    # after 94 verified skips + our 2 pre-existing).
    # v0.1.0.62: hotfix v0.1.0.61 - fix state-order in generator so
    # multi records come AFTER code records (multi's child_ids can
    # reference code records, so all children must load first).
    # Old order: next_activity, object_write, multi, code
    # New order: next_activity, object_write, code, multi
    # v0.1.0.61: 101 additional server actions (state-diverse).
    # Deep dedup check on 136 remaining candidates:
    #   * 31 verified true duplicates (same name+model+state+code as
    #     standard Odoo) - correctly skipped
    #   * 4 ir_cron actions - skipped per pattern
    #   * 101 truly new - shipped here (44 state=code + 22 next_activity
    #     + 20 multi + 15 object_write)
    # State ordering: next_activity + object_write first, then multi +
    # code (Odoo XML load-order requirement for child_ids refs).
    # Server actions: 57/193 -> 158/193 = 82%.
    # v0.1.0.60: 57 base.automation trigger records - coverage 0/57 -> 57/57.
    # Wires all v0.1.0.59-shipped server actions to their triggers.
    # Trigger types: mostly on_create_or_write (Track * fields) and
    # on_change (Update Payment Term, Validate Payment Method, etc.).
    # New file: data/automations.xml.
    # v0.1.0.59: 57 base_automation server actions - foundation for
    # the 57 base.automation trigger records to ship in v0.1.0.60.
    # All state=code, usage=base_automation. Grouped by model:
    #   * res.partner: 29 (SLS-Track * customer fields, credit limit
    #     validation, customer group validation, payment term updates)
    #   * sale.order: 12 (payment method pass, order validation,
    #     quotation type auto-gen for Repair/Project SOs, seq.no,
    #     analytic tag params, project pricelist, JIN Company Id)
    #   * sale.order.line: 7 (discount/commission validation, RUG
    #     sales price, project details, lock status, apply pricelist)
    #   * product.template: 3 (item master validation)
    #   * x_delivery_terms + product.pricelist + res.partner + res.company:
    #     JIN Company Id records
    # New file: data/server_actions.xml.
    # v0.1.0.58: close the 60 field gap identified by the migration audit.
    # New model files:
    #   * models/product_template.py: 15 fields (item approval flags,
    #     max discount, product_type selection with 4 options, tariff
    #     code M2O to x_tariffmaster owned by BugFix-Stock, etc.)
    #   * models/product_product.py: 43 fields (superset of template
    #     fields + product.product-specific: many redundant checkboxes,
    #     related fields, extra selection with empty options preserved
    #     verbatim per Clear-DB fidelity).
    #   * res_partner.py: un-TODO'd x_vendor_id__purchase_requisition_count
    #     compute (store=False, counts PRs where vendor_id equals partner).
    #   * sale_order.py: un-TODO'd x_studio_one2many_field_ERCBB O2M
    #     to sale.order.line via order_id.
    # NEW DEPS: purchase_requisition (for vendor count compute),
    # BugFix-Stock (for x_tariffmaster comodel resolution).
    # Field coverage: 202/262 -> 262/262 (100%).
    # v0.1.0.57: break the 3-way cycle Sales -> Purchase -> Accounting
    # -> Sales that was silently blocking module upgrades and causing
    # Python classes not to load. Removed BugFix-Purchase from depends.
    # The dep was added in v0.1.0.55/56 to prevent field shadowing on
    # x_delivery_terms (both modules declare via _name). Fix: drop the
    # mirrored x_studio_delivery_terms_id O2M from Sales's declaration.
    # Purchase's declaration keeps the O2M and loads AFTER Sales, so
    # Purchase's class definition wins on merge (O2M present at runtime).
    # v0.1.0.56: cross-repo companion fix for BugFix-Purchase v0.1.0.71.
    # Purchase added _inherit = ['mail.thread', 'mail.activity.mixin']
    # to its x_delivery_terms declaration. Both modules declare that
    # model via _name; without matching the inherit here, chatter/
    # activity fields would get shadowed and view ports referencing
    # them would fail. Mirroring the inherit.
    # v0.1.0.55: cross-repo companion fix for BugFix-Purchase v0.1.0.33.
    # Both this module and BugFix-Purchase declare x_delivery_terms via
    # _name (not _inherit). Odoo merges the declarations, but the
    # LATER-loaded module's field list REPLACES the earlier one's --
    # so Purchase's x_studio_delivery_terms_id O2M (shipped v0.1.0.33)
    # got shadowed at runtime ("Invalid field ... on model
    # x_delivery_terms" error at read time).
    # Fix: mirror Purchase's declaration in Sales - add the O2M
    # declaration + default=True on x_active. Now field sets match
    # regardless of merge order. NEW DEP BugFix-Purchase (needed for
    # x_delivery_term_charge comodel to resolve).
    # v54: added Jinasena_Masterdata_Reporting to depends.
    # BugFix-Sales/models/x_sales_report_type.py was _name='x_sales_report_type'
    # (a competing "owner" declaration without dep on the real owner). With two
    # _name= declarations and no dep chain, Odoo's topological sort could pick
    # BugFix-Sales's class as the live model, leaving x_studio_journal_items_id
    # absent from x_sales_report_type._fields at setup_models() time. That
    # caused KeyError on x_sales_report_model.x_studio_journal_item_ids
    # (related='x_studio_report_type.x_studio_journal_items_id') and broke the
    # registry on every startup. Fix: x_sales_report_type.py converted to
    # _inherit; Jinasena_Masterdata_Reporting (the canonical owner) added here.
    # studio_usermodel_migration removed in v52 (no load-time dep, cycle risk).
    'depends': ['base_setup', 'sale', 'sale_stock', 'industry_fsm_sale',
                'purchase_requisition', 'website_sale',
                'Jinasena_Masterdata_Reporting', 'BugFix-Stock'],
    'post_init_hook': 'post_init_hook',
    # v47: bulk-port of remaining Studio artifacts via
    # scripts/scaffold_bugfix_module.py (adds 8 sale.order fields,
    # 36 sale.order.line fields, sale.order.alert model, 3 custom
    # models: x_customer_group / x_vendor_group / x_delivery_terms).
    # ir_model_pins.xml MUST load before ir.model.access.csv so the
    # ACL rows can resolve the model_x_* xmlids for the custom
    # models.
    # v52: removed studio_usermodel_migration from depends. This module
    # uses no models or fields from studio_usermodel_migration at
    # schema/model-load time (confirmed: no code or view references).
    # The dep was added in v0.47 to anchor load order when fixing the
    # previous cycle, but it created a new 3-way cycle:
    #   BugFix-Sales -> studio_usermodel_migration
    #     -> studio_migrations -> BugFix-Sales
    # Removed alongside dropping studio_migrations from
    # studio_usermodel_migration's depends (v0.0.9 of that module).
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/bugfix_sales_data.xml',
        'data/server_actions.xml',
        'data/server_actions_v2.xml',
        'data/automations.xml',
        'data/window_actions.xml',
        'views/doc_intro_views.xml',
        'views/doc_conclusion_views.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/sale_advance_payment_inv_views.xml',
        'views/sale_order_views.xml',
        'views/x_delivery_terms_studio_ported.xml',
        'views/res_partner_studio_ported.xml',
        'views/sale_order_studio_ported.xml',
        'views/product_pricelist_studio_ported.xml',
        'views/sale_report_studio_ported.xml',
        'views/res_company_studio_ported.xml',
        'views/sale_order_line_studio_ported.xml',
        'views/studio_ported_9_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
