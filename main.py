def get_avarage(dataset):
    import json
    import odoo
    from odoo.tools import float_utils
    lnth = len(dataset)
    dataset = list(dict.fromkeys(dataset))
    avg = sum(dataset) / lnth
    result = {'avarage': float_utils.float_round(avg, 1)}
    return json.dumps(result)