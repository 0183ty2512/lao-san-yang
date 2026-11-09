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
    context=browser.new_context(viewport={'width':390,'height':844},device_scale_factor=1)
    page=context.new_page()
    javascript_errors=[]
    page.on('pageerror',lambda error:javascript_errors.append(str(error)))
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
    base=f'http://127.0.0.1:{server.server_port}'
    page.goto(base+'/D08.html')
    page.locator('#font-toggle').click()
    for _ in range(3):page.locator('#font-plus').click()
    assert page.locator('#font-value').inner_text()=='24 px'
    assert page.locator('#font-plus').is_disabled()
    page.reload()
    assert page.locator('.lesson-content').evaluate('(e)=>getComputedStyle(e).fontSize')=='24px'
    for width in [320,390,768,1280]:
        page.set_viewport_size({'width':width,'height':844})
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),width
    page.set_viewport_size({'width':390,'height':844})
    page.locator('#toc-toggle').click()
    assert page.locator('#toc-dialog').evaluate('(e)=>e.open')
    page.locator('#toc-search').fill('2022-二-2')
    first=page.locator('#toc-sections .toc-entry:visible').first
    target=first.get_attribute('href')
    first.click()
    page.wait_for_function('!document.getElementById("toc-dialog").open')
    assert page.evaluate('decodeURIComponent(location.hash)')==target
    assert page.evaluate('document.activeElement.id')==target[1:]
    assert page.locator(target).bounding_box()['y']>=page.locator('.site-header').bounding_box()['height']
    page.locator('#toc-toggle').click()
    page.locator('#toc-search').fill('~无匹配项目~')
    assert page.locator('#toc-empty').is_visible()
    page.keyboard.press('Escape')
    page.wait_for_function('document.activeElement.id==="toc-toggle"')
    page.locator('#toc-toggle').click()
    page.locator('.drawer-list').evaluate('(e)=>{e.scrollTop=e.scrollHeight}')
    page.locator('#toc-days-tab').click()
    assert page.locator('.drawer-list').evaluate('(e)=>e.scrollTop')==0
    page.locator('#toc-search').fill('D11')
    page.locator('#toc-days .toc-entry:visible').click()
    page.wait_for_url('**/D11.html')
    assert page.locator('.lesson-content').evaluate('(e)=>getComputedStyle(e).fontSize')=='24px'
    page.locator('#font-toggle').click()
    page.locator('#font-reset').click()
    page.keyboard.press('Escape')
    # At phone width the directory has a real scrolling list and clear question labels.
    page.goto(base+'/D08.html')
    page.locator('#toc-toggle').click()
    page.screenshot(path=str(root/'scripts/verification/reader-directory.png'))
    assert page.locator('.drawer-list').evaluate('(e)=>e.scrollHeight>e.clientHeight')
    page.keyboard.press('Escape')
    page.locator('#theme-toggle').click()
    page.goto(base+'/index.html')
    page.set_viewport_size({'width':1280,'height':900})
    page.screenshot(path=str(root/'scripts/verification/reader-index.png'))
    page.locator('#search').fill('2026-11-08')
    assert page.locator('.card:visible').count()==1
    assert page.locator('.card:visible').get_attribute('href')=='D11.html'
    page.locator('.card:visible').click()
    page.set_viewport_size({'width':390,'height':844})
    page.screenshot(path=str(root/'scripts/verification/reader-lesson.png'))
    page.locator('#font-toggle').focus()
    page.keyboard.press('Enter')
    page.keyboard.press('Tab')
    assert page.evaluate('document.activeElement.id')=='font-minus'
    page.keyboard.press('Escape')
    page.goto(base+'/D44.html')
    # Inspect revised formulas in the mock appendix at desktop and phone widths.
    page.set_viewport_size({'width':1280,'height':900})
    page.locator('h1',has_text='模拟试题三 · 参考答案').scroll_into_view_if_needed()
    page.screenshot(path=str(root/'scripts/verification/D44-review.png'))
    page.set_viewport_size({'width':390,'height':844})
    page.locator('.math-scroll').filter(has=page.locator('mjx-container')).last.scroll_into_view_if_needed()
    page.screenshot(path=str(root/'scripts/verification/D44-formula-mobile.png'))
    # A real question jump survives another day's top and returns from the index.
    page.goto(base+'/index.html')
    page.evaluate("localStorage.removeItem('study-reading-position')")
    page.reload()
    assert page.locator('#resume-reading').is_hidden()
    page.evaluate("localStorage.setItem('study-reading-position', '{broken')")
    page.reload()
    assert page.locator('#resume-reading').is_hidden()
    page.goto(base+'/D08.html')
    page.locator(target).evaluate('(e)=>e.scrollIntoView({block:"start"})')
    page.wait_for_function('''anchor => {
        try {return JSON.parse(localStorage.getItem('study-reading-position')).anchor === anchor}
        catch {return false}
    }''',arg=target[1:])
    saved=page.evaluate("localStorage.getItem('study-reading-position')")
    # Returning to the same question after reading another tab updates the bookmark.
    other=page.context.new_page()
    other.goto(base+'/D11.html')
    other.locator('.lesson-content h2').first.evaluate('(e)=>e.scrollIntoView({block:"start"})')
    other.wait_for_function("JSON.parse(localStorage.getItem('study-reading-position')).day === 'D11'")
    other.close()
    page.evaluate('window.scrollBy(0,12)')
    page.wait_for_function("saved => localStorage.getItem('study-reading-position') === saved",arg=saved)
    page.goto(base+'/D11.html')
    page.locator('.brand').click()
    assert page.evaluate("localStorage.getItem('study-reading-position')")==saved
    assert page.locator('#resume-reading').is_visible()
    assert 'D08' in page.locator('#resume-reading').inner_text()
    for width in [320,1280]:
        page.set_viewport_size({'width':width,'height':900})
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
        page.screenshot(path=str(root/f'scripts/verification/reader-resume-{width}.png'))
    page.locator('#resume-reading').click()
    page.wait_for_url('**/D08.html#*')
    assert page.evaluate('decodeURIComponent(location.hash)')==target
    box=page.locator(target).bounding_box()
    assert page.locator('.site-header').bounding_box()['height']<=box['y']<page.viewport_size['height']
    browser.close()
server.shutdown()
bad=[r for r in results if r['overflow'] or r['errors'] or r['brokenImages'] or r['brokenAnchors'] or r['rawTex']]
assert not javascript_errors,javascript_errors
output={'pages':results,'themePersistence':True,'failures':bad,'formulaCount':sum(x['math'] for x in results)}
(root/'scripts/verification/browser-check-reader.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(results),'formulas':output['formulaCount'],'scrollable':sum(x['scrollable'] for x in results),'failures':bad},ensure_ascii=False))
assert not bad
