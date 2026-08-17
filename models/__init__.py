from . import doc_intro
from . import doc_conclusion
from . import minimum_sales_margin_seed
from . import res_company            # must precede res_config_settings — settings' related fields resolve against it
from . import res_config_settings
from . import res_partner            # must precede sale_order — related fields on SO resolve against res.partner Studio fields
from . import sale_advance_payment_inv
from . import sale_order
from . import sale_order_line
from . import account_payment
