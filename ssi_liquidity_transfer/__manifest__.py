# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Liquidity Transfer",
    "version": "14.0.1.1.0",
    "category": "Accounting",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_master_data_mixin",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_open_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_financial_accounting",
        "ssi_account_account_m2o_configurator_mixin",
        "ssi_account_journal_m2o_configurator_mixin",
        "ssi_res_partner_m2o_configurator_mixin",
        "ssi_m2o_configurator_mixin",
        "ssi_company_currency_mixin",
        "ssi_accounting_entry_mixin",
        "base_automation",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "security/ir_rule_data.xml",
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "data/policy_template_data.xml",
        "data/approval_template_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_automation_data.xml",
        "menu.xml",
        "views/liquidity_transfer_type_views.xml",
        "views/liquidity_transfer_views.xml",
    ],
    "demo": [],
    "images": [],
}
