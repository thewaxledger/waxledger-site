import json,sys,subprocess
A=dict(fee=59.99,ship=10,sellFee=.13,haircut=.20,missReal=.85,assumedGem=.35,minSales=25,minMargin=.10)
def score(c):
    if c['raw'] is None or c['psa10'] is None or c['psa9'] is None: return dict(code='NODATA')
    gem=c['pop10']/c['popTotal'] if c.get('pop10') and c.get('popTotal') else A['assumedGem']
    allIn=c['raw']+A['fee']+A['ship']; net10=c['psa10']*(1-A['haircut'])*(1-A['sellFee']); netMiss=c['psa9']*A['missReal']*(1-A['sellFee'])
    ev=gem*net10+(1-gem)*netMiss; profit=ev-allIn; roi=profit/allIn; be=(allIn-netMiss)/(net10-netMiss) if net10!=netMiss else None
    code='GRADE'
    if c['compType']!='Real': code='SKIP'
    elif (c.get('psa10Sales90') or 0)<A['minSales']: code='FAIL liq'
    elif profit<=0: code='FAIL EV'
    elif be is None or gem-be<A['minMargin']: code='MARGINAL'
    return dict(code=code,gem=gem,allIn=allIn,net10=net10,netMiss=netMiss,ev=ev,profit=profit,roi=roi,be=be,down=netMiss-allIn,up=net10-allIn)
entries=json.loads(subprocess.check_output(['python3','build.py'],stderr=subprocess.DEVNULL))
for c in entries:
    s=score(c)
    print(f"{c['id']:52s} raw {str(c['raw']):>8} 9 {str(c['psa9']):>8} 10 {str(c['psa10']):>8} n10 {c['psa10Sales90']:>3} gem {s.get('gem',0)*100:4.0f}% allin {s.get('allIn',0):6.0f} EV {s.get('ev',0):6.0f} profit {s.get('profit',0):+6.0f} be {(s.get('be') or 0)*100:4.0f}% miss {s.get('down',0):+5.0f} hit {s.get('up',0):+5.0f} {s['code']} {c['conf']}")
