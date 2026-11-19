/** @odoo-module */
// Sales order / quotation: before saving (Save button, leaving the page, or a
// button that saves first such as Confirm), warn when one or more product
// lines have no Tax. OK saves; Cancel keeps the user on the order unsaved.

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

function linesWithoutTax(record) {
    const lines = record.data.order_line?.records || [];
    return lines.filter(
        (line) =>
            !line.data.display_type &&
            line.data.product_id &&
            !(line.data.tax_id?.records || []).length
    );
}

function productName(value) {
    return Array.isArray(value) ? value[1] : value?.display_name || "";
}

patch(FormController.prototype, {
    async onWillSaveRecord(record, changes) {
        const res = await super.onWillSaveRecord(...arguments);
        if (res === false || record.resModel !== "sale.order" || record !== this.model.root) {
            return res;
        }
        const missing = linesWithoutTax(record);
        if (!missing.length) {
            return res;
        }
        const names = missing.map((line) => "- " + productName(line.data.product_id)).join("\n");
        return new Promise((resolve) => {
            let answered = false;
            const answer = (value) => {
                if (!answered) {
                    answered = true;
                    resolve(value);
                }
            };
            this.model.dialog.add(
                ConfirmationDialog,
                {
                    title: _t("Tax not selected"),
                    body:
                        _t("One or more lines have no Tax selected:") +
                        "\n" + names + "\n\n" +
                        _t("Are you sure you want to save?"),
                    confirmLabel: _t("Ok"),
                    cancelLabel: _t("Cancel"),
                    confirm: () => answer(true),
                    cancel: () => answer(false),
                },
                { onClose: () => answer(false) }
            );
        });
    },
});
