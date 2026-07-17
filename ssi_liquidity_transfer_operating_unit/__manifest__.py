# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Liquidity Transfer + Operating Unit",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_liquidity_transfer",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/liquidity_transfer.xml",
        "security/ir_rule/liquidity_transfer.xml",
        "view/liquidity_transfer.xml",
    ],
}
