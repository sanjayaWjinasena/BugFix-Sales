# BugFix-Sales — views to hand-port

25 views need hand-porting from Clear-DB. Do NOT 
auto-copy the arch — each has Studio xpath quirks that need 
human review before commit.

| # | Clear-DB view ID | Type | Target model | Name | Inherits |
|---|---|---|---|---|---|
| 1 | 9162 | form | `sale.report` | Default form view for ir.model(600,) | — |
| 2 | 3114 | form | `x_customer_group` | Default form view for x_customer_group | — |
| 3 | 2712 | form | `x_delivery_terms` | Default form view for x_delivery_terms | — |
| 4 | 3120 | form | `x_vendor_group` | Default form view for x_vendor_group | — |
| 5 | 3113 | tree | `x_customer_group` | Default list view for x_customer_group | — |
| 6 | 2711 | tree | `x_delivery_terms` | Default list view for x_delivery_terms | — |
| 7 | 3119 | tree | `x_vendor_group` | Default list view for x_vendor_group | — |
| 8 | 3260 | pivot | `sale.order.line` | Default pivot view for ir.model(599,) | — |
| 9 | 3115 | search | `x_customer_group` | Default search view for x_customer_group | — |
| 10 | 2713 | search | `x_delivery_terms` | Default search view for x_delivery_terms | — |
| 11 | 3121 | search | `x_vendor_group` | Default search view for x_vendor_group | — |
| 12 | 3116 | form | `x_customer_group` | Odoo Studio: Default form view for x_customer_group customization | Default form view for x_customer_group |
| 13 | 2714 | form | `x_delivery_terms` | Odoo Studio: Default form view for x_delivery_terms customization | Default form view for x_delivery_terms |
| 14 | 3122 | form | `x_vendor_group` | Odoo Studio: Default form view for x_vendor_group customization | Default form view for x_vendor_group |
| 15 | 3117 | tree | `x_customer_group` | Odoo Studio: Default list view for x_customer_group customization | Default list view for x_customer_group |
| 16 | 2719 | tree | `x_delivery_terms` | Odoo Studio: Default list view for x_delivery_terms customization | Default list view for x_delivery_terms |
| 17 | 3123 | tree | `x_vendor_group` | Odoo Studio: Default list view for x_vendor_group customization | Default list view for x_vendor_group |
| 18 | 2304 | form | `sale.order` | Odoo Studio: sale.order.form customization | sale.order.form |
| 19 | 3920 | form | `sale.order` | Odoo Studio: sale.order.form customization_button | sale.order.form |
| 20 | 3922 | form | `sale.order` | Odoo Studio: sale.order.form customization_button_2 | sale.order.form |
| 21 | 3259 | tree | `sale.order.line` | Odoo Studio: sale.order.line.tree customization | sale.order.line.tree |
| 22 | 3126 | pivot | `sale.order` | Odoo Studio: sale.order.pivot customization | sale.order.pivot |
| 23 | 7977 | tree | `sale.order` | Odoo Studio: sale.order.tree (orders) customization | sale.order.tree (orders) |
| 24 | 3127 | tree | `sale.order` | Odoo Studio: sale.order.tree customization | sale.order.tree |
| 25 | 4733 | tree | `sale.order` | Odoo Studio: sale.order.tree customization | sale.order.tree |
