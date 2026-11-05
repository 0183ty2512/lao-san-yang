"""Browser checks for final static formulas, overflow, links and theme persistence."""
from pathlib import Path
import json,re,threading
from urllib.parse import unquote,urlparse
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1];docs=root.parent/'docs'
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(docs)))
threading.Thread(target=server.serve_forever,daemon=True).start()
results=[]
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True)
    page=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
    for day in range(1,51):
        page.goto(f'http://127.0.0.1:{server.server_port}/D{day:02}.html')
        result=page.evaluate(r'''() => ({overflow:document.documentElement.scrollWidth>innerWidth+1,
            math:document.querySelectorAll('mjx-container').length,
            errors:document.querySelectorAll('[data-mjx-error]').length,
            brokenImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src),
            brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(decodeURIComponent(a.hash.slice(1)))).map(a=>a.hash),
            rawTex:/\\(?:frac|partial|begin|end)\b/.test(document.body.innerText),
            scrollable:[...document.querySelectorAll('.math-scroll')].filter(e=>e.scrollWidth>e.clientWidth+1).length})''')
        result['day']=day;results.append(result)
    page.goto(f'http://127.0.0.1:{server.server_port}/D44.html')
    for theme in ['light','dark']:
        if page.locator('html').get_attribute('data-theme')!=theme:page.locator('#theme-toggle').click()
        page.reload();assert page.locator('html').get_attribute('data-theme')==theme
    # Inspect revised formulas in the mock appendix at desktop and phone widths.
    page.set_viewport_size({'width':1280,'height':900})
    page.locator('h1',has_text='模拟试题三 · 参考答案').scroll_into_view_if_needed()
    page.screenshot(path=str(root/'scripts/verification/D44-review.png'))
    page.set_viewport_size({'width':390,'height':844})
    page.locator('.math-scroll').filter(has=page.locator('mjx-container')).last.scroll_into_view_if_needed()
    page.screenshot(path=str(root/'scripts/verification/D44-formula-mobile.png'))
    browser.close()
server.shutdown()
bad=[r for r in results if r['overflow'] or r['errors'] or r['brokenImages'] or r['brokenAnchors'] or r['rawTex']]
output={'pages':results,'themePersistence':True,'failures':bad,'formulaCount':sum(x['math'] for x in results)}
(root/'scripts/verification/browser-check-20261104.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(results),'formulas':output['formulaCount'],'scrollable':sum(x['scrollable'] for x in results),'failures':bad},ensure_ascii=False))
assert not bad
