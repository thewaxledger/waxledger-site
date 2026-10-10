"""Build public/index.html from src/index.src.html (adds <head> meta, favicons, OG tags, Beta label).
Run: python3 tools/build.py
"""
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(ROOT,'src/index.src.html')).read()
META='''
<link rel="canonical" href="https://thewaxledger.com/">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0F1B2D">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Wax Ledger">
<meta property="og:title" content="Wax Ledger">
<meta property="og:description" content="Your one-stop sports card hub. Sold comps, a raw-to-gem calculator on real sales, a pre-grading tool that runs in your browser, and the release calendar.">
<meta property="og:url" content="https://thewaxledger.com/">
<meta property="og:image" content="https://thewaxledger.com/og-image.png">
<meta property="og:image:width" content="2400">
<meta property="og:image:height" content="1260">
<meta property="og:image:alt" content="Wax Ledger logo with the tagline Your one-stop sports card hub">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@thewaxledger">
<meta name="twitter:title" content="Wax Ledger">
<meta name="twitter:description" content="Your one-stop sports card hub. Sold comps, a raw-to-gem calculator on real sales, a pre-grading tool that runs in your browser, and the release calendar.">
<meta name="twitter:image" content="https://thewaxledger.com/og-image.png">'''
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Wax Ledger: sold comps, a raw-to-gem calculator on real sales, a pre-grading tool that runs in your browser, and the sports card release calendar.">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
'''
i=s.index('<title>'); j=s.index('</title>')+8
out=head+s[i:j]+META+'\n</head>\n<body>\n'+s[:i]+s[j:]+'\n</body>\n</html>\n'
import re
out=re.sub(r'Preview build · (\w+ \d+, 2026)', r'Beta · \1', out).replace('<b>Preview build</b>','<b>Beta</b>')
open(os.path.join(ROOT,'public/index.html'),'w').write(out); print('built public/index.html',len(out))
# static, indexable pages from the same data
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages
m=re.search(r'Beta · (\w+ \d+, 2026)', out)
print('static pages (cards, reviews, urls):', pages.build('Beta · '+m.group(1) if m else 'Beta'))
