import json, re, sys
sys.path.insert(0, 'output/work')
import merge
ranked = json.load(open('output/work/ranked.json'))
bad = []
for i, it in enumerate(ranked, 1):
    p = it.get('profile_md', '')
    issues = []
    for key in ['Est/Doctors', 'Site (observed', 'Breakdown', 'Independence', 'Decision-maker', 'FinCap', 'Hooks', 'Pitch', 'Sources']:
        if key not in p: issues.append('missing ' + key)
    if not re.search(r'VERIFIED|INFERRED|UNKNOWN', p): issues.append('no evidence tags')
    site = re.search(r'Site \(observed[^:]*\):(.*)', p)
    if site and not re.search(r'["“”\']', site.group(1)): issues.append('no quoted defect in Site line')
    bd = re.search(r'Breakdown:(.*?)\|', p)
    if bd:
        nums = re.findall(r'[A-Za-z]+\s*(\d+)(?:/\d+)?', bd.group(1))
        s = sum(int(n) for n in nums[:9])
        if abs(s - float(it['score'])) > 0.5: issues.append(f'breakdown sum {s} != score {it["score"]}')
    else:
        issues.append('breakdown unparsed')
    dm = re.search(r'Decision-maker:([^\n|•]*)', p)
    if dm and not dm.group(1).strip(): issues.append('empty decision-maker')
    if issues: bad.append((i, it['name'], it['region'], issues))
for b in bad: print(b)
print('profiles with issues:', len(bad), 'of', len(ranked))
print('--- top-50 independence strings containing MEDIUM ---')
for i, it in enumerate(ranked[:50], 1):
    ind = it.get('independence') or ''
    m = re.search(r'Independence:([^\n]*)', it.get('profile_md', ''))
    line = m.group(1) if m else ind
    if 'MEDIUM' in (ind + line).upper():
        print(i, it['name'], '|', ind[:90], '|', line[:120])
