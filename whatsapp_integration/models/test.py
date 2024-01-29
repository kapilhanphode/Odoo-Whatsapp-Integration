from odoo import models, fields, api, _


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    def whatsapp_int(self):
        print('whatsapp integration')
        state = dict(self._fields['state'].selection).get(self.state)
        print('string value',state)
        x = self.env.ref('purchase.report_purchase_quotation').report_action(self)
        msg = 'Hi %s your PO No. is "%s" Your PO is in "%s" State' % (self.partner_id.name, self.name, state)
        whatsapp_api_url = 'https://web.whatsapp.com/send?phone=%s&text=%s' % (self.partner_id.phone,msg)

        return {
            'type': 'ir.actions.act_url',
            'target': 'current',
            'url': whatsapp_api_url,

        }
