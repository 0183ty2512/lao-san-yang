(() => {
  'use strict';

  const root = document.documentElement;
  const themeKey = 'study-theme';
  const fontKey = 'study-reader-size';
  const sizes = [16, 18, 20, 22, 24];
  const defaultSize = 18;
  const systemDark = window.matchMedia('(prefers-color-scheme: dark)');

  function readSetting(key) {
    try {
      return window.localStorage.getItem(key);
    } catch {
      return null;
    }
  }

  function saveSetting(key, value) {
    try {
      window.localStorage.setItem(key, String(value));
    } catch {
      // The current page's controls also work with storage disabled.
    }
  }

  function readTheme() {
    const saved = readSetting(themeKey);
    return saved === 'dark' || saved === 'light' ? saved : null;
  }

  function readSize() {
    const saved = Number(readSetting(fontKey));
    return sizes.includes(saved) ? saved : defaultSize;
  }

  let chosenTheme = readTheme();
  let size = readSize();
  function applyAppearance() {
    root.dataset.theme = chosenTheme || (systemDark.matches ? 'dark' : 'light');
    root.style.setProperty('--reader-size', size + 'px');
  }
  // Called from the document head, before the first paint.
  applyAppearance();

  function setupPreferences() {
    const themeButton = document.getElementById('theme-toggle');
    const fontButton = document.getElementById('font-toggle');
    const panel = document.getElementById('font-panel');
    const smaller = document.getElementById('font-minus');
    const larger = document.getElementById('font-plus');
    const reset = document.getElementById('font-reset');
    const value = document.getElementById('font-value');

    function updateControls() {
      applyAppearance();
      const dark = root.dataset.theme === 'dark';
      const label = dark ? '切换为明亮模式' : '切换为黑暗模式';
      themeButton.title = label;
      themeButton.setAttribute('aria-label', label);
      themeButton.setAttribute('aria-pressed', String(dark));
      value.textContent = size + ' px';
      smaller.disabled = size === sizes[0];
      larger.disabled = size === sizes[sizes.length - 1];
      fontButton.setAttribute('aria-label', '调节字号，当前 ' + size + ' 像素');
    }

    function changeSize(nextSize) {
      if (!sizes.includes(nextSize)) return;
      size = nextSize;
      saveSetting(fontKey, size);
      updateControls();
    }

    function showPanel(open) {
      panel.hidden = !open;
      fontButton.setAttribute('aria-expanded', String(open));
    }

    updateControls();
    showPanel(false);
    themeButton.addEventListener('click', () => {
      chosenTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      saveSetting(themeKey, chosenTheme);
      updateControls();
    });
    fontButton.addEventListener('click', () => showPanel(panel.hidden));
    smaller.addEventListener('click', () => changeSize(sizes[sizes.indexOf(size) - 1]));
    larger.addEventListener('click', () => changeSize(sizes[sizes.indexOf(size) + 1]));
    reset.addEventListener('click', () => changeSize(defaultSize));
    function dismissOutside(event) {
      if (!panel.hidden && !panel.contains(event.target) && !fontButton.contains(event.target)) {
        showPanel(false);
      }
    }
    document.addEventListener('pointerdown', dismissOutside);
    document.addEventListener('focusin', dismissOutside);
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && !panel.hidden) {
        event.preventDefault();
        showPanel(false);
        fontButton.focus();
      }
    });
    systemDark.addEventListener('change', () => {
      if (!chosenTheme) updateControls();
    });
    function restoreSettings() {
      chosenTheme = readTheme();
      size = readSize();
      updateControls();
    }
    window.addEventListener('storage', (event) => {
      if ([null, themeKey, fontKey].includes(event.key)) restoreSettings();
    });
    window.addEventListener('pageshow', (event) => {
      if (event.persisted) {
        restoreSettings();
        showPanel(false);
      }
    });
  }

  function searchText(text) {
    return text.normalize('NFKC').toLowerCase()
      .replace(/\bd\s*(\d)\b/g, 'd0$1')
      .replace(/\s+/g, ' ').trim();
  }

  function searchIndex(elements) {
    return Array.from(elements, (element) => ({
      element,
      text: searchText(element.textContent + ' ' + (element.dataset.day || '')
        + ' ' + (element.dataset.date || '')),
    }));
  }

  function filterEntries(entries, query) {
    const terms = searchText(query).split(' ').filter(Boolean);
    let visible = 0;
    for (const { element, text } of entries) {
      element.hidden = !terms.every(term => text.includes(term));
      if (!element.hidden) visible++;
    }
    return visible;
  }

  function setupDirectory() {
    const openButton = document.getElementById('toc-toggle');
    const dialog = document.getElementById('toc-dialog');
    const search = document.getElementById('toc-search');
    const empty = document.getElementById('toc-empty');
    const scrollList = dialog.querySelector('.drawer-list');
    const tabs = [...dialog.querySelectorAll('[data-list]')].filter(tab => tab.matches('button'));
    const lists = {};
    for (const name of ['sections', 'days']) {
      const panel = document.getElementById('toc-' + name);
      if (panel) lists[name] = { panel, entries: searchIndex(panel.querySelectorAll('.toc-entry')) };
    }
    const initial = document.body.classList.contains('page-index') || !lists.sections ? 'days' : 'sections';
    let current = initial;
    let anchorAfterClose = null;

    function filter() {
      empty.hidden = filterEntries(lists[current].entries, search.value) > 0;
      scrollList.scrollTop = 0;
    }
    function switchList(name) {
      current = name;
      for (const [key, { panel }] of Object.entries(lists)) panel.hidden = key !== name;
      for (const tab of tabs) {
        const selected = tab.dataset.list === name;
        tab.setAttribute('aria-selected', String(selected));
        tab.tabIndex = selected ? 0 : -1;
      }
      filter();
    }
    for (const [i, tab] of tabs.entries()) {
      tab.addEventListener('click', () => switchList(tab.dataset.list));
      tab.addEventListener('keydown', (event) => {
        const destinations = {
          ArrowLeft: (i + tabs.length - 1) % tabs.length,
          ArrowRight: (i + 1) % tabs.length,
          Home: 0,
          End: tabs.length - 1,
        };
        if (!(event.key in destinations)) return;
        event.preventDefault();
        const nextTab = tabs[destinations[event.key]];
        switchList(nextTab.dataset.list);
        nextTab.focus();
      });
    }
    switchList(initial);
    openButton.setAttribute('aria-expanded', 'false');
    search.addEventListener('input', filter);
    openButton.addEventListener('click', () => {
      if (dialog.open) return;
      search.value = '';
      switchList(initial);
      dialog.showModal();
      openButton.setAttribute('aria-expanded', 'true');
      // Focus the search on desktops without summoning a phone's keyboard on open.
      if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
        search.focus({ preventScroll: true });
      } else {
        document.getElementById('toc-close').focus({ preventScroll: true });
      }
    });
    document.getElementById('toc-close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        event.preventDefault();
        dialog.close();
      }
    });
    function outside(event) {
      const box = dialog.getBoundingClientRect();
      return event.clientX < box.left || event.clientX > box.right
        || event.clientY < box.top || event.clientY > box.bottom;
    }
    let startedOnBackdrop = false;
    dialog.addEventListener('pointerdown', (event) => {
      startedOnBackdrop = event.target === dialog && outside(event);
    });
    dialog.addEventListener('click', (event) => {
      if (startedOnBackdrop && event.target === dialog && outside(event)) {
        dialog.close();
        return;
      }
      const link = event.target.closest('a[href]');
      if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.altKey || event.shiftKey) return;
      const url = new URL(link.href);
      if (url.origin !== location.origin || url.pathname !== location.pathname
        || url.search !== location.search || !url.hash) return;
      const target = document.getElementById(decodeURIComponent(url.hash.slice(1)));
      if (!target) return;
      event.preventDefault();
      anchorAfterClose = { target, hash: url.hash };
      dialog.close();
    });
    dialog.addEventListener('close', () => {
      openButton.setAttribute('aria-expanded', 'false');
      if (!anchorAfterClose) {
        openButton.focus({ preventScroll: true });
        return;
      }
      const { target, hash } = anchorAfterClose;
      anchorAfterClose = null;
      if (location.hash !== hash) location.hash = hash;
      if (!target.hasAttribute('tabindex')) target.tabIndex = -1;
      target.focus({ preventScroll: true });
      target.scrollIntoView({ block: 'start' });
    });
    window.addEventListener('pageshow', (event) => {
      if (event.persisted && dialog.open) dialog.close();
    });
  }

  function setupCatalog() {
    const search = document.getElementById('search');
    if (!search) return;
    const cards = document.querySelectorAll('.grid .card');
    const entries = searchIndex(cards);
    const empty = document.getElementById('catalog-empty');
    const filter = () => { empty.hidden = filterEntries(entries, search.value) > 0; };
    search.addEventListener('input', filter);
    filter();

    const todayLink = document.getElementById('open-today');
    const parts = new Intl.DateTimeFormat('en-US', {
      timeZone: 'Asia/Shanghai', year: 'numeric', month: '2-digit', day: '2-digit',
    }).formatToParts(new Date());
    const value = part => parts.find(item => item.type === part).value;
    const today = value('year') + '-' + value('month') + '-' + value('day');
    const card = [...cards].find(item => item.dataset.date === today);
    if (card && todayLink) {
      todayLink.setAttribute('href', card.getAttribute('href'));
      todayLink.querySelector('[data-action-label]').textContent = '打开今日 ' + card.dataset.day;
    }
  }

  function setupReadingPosition() {
    const key = 'study-reading-position';
    const resume = document.getElementById('resume-reading');
    function updateResume() {
      if (!resume) return;
      resume.hidden = true;
      try {
        const saved = JSON.parse(readSetting(key));
        if (!saved || !/^D(?:0[1-9]|[1-4]\d|50)$/.test(saved.day)
          || typeof saved.anchor !== 'string' || !saved.anchor || saved.anchor.length > 500
          || typeof saved.label !== 'string' || !saved.label || saved.label.length > 500) return;
        resume.href = saved.day + '.html#' + encodeURIComponent(saved.anchor);
        resume.querySelector('[data-resume-day]').textContent = '继续上次阅读 · ' + saved.day;
        resume.querySelector('[data-resume-label]').textContent = saved.label;
        resume.hidden = false;
      } catch {
        // Invalid or unavailable browser storage leaves the shortcut hidden.
      }
    }
    updateResume();
    window.addEventListener('pageshow', updateResume);
    window.addEventListener('storage', event => {
      if (event.key === key || event.key === null) updateResume();
    });

    const day = location.pathname.match(/\/(D(?:0[1-9]|[1-4]\d|50))\.html$/);
    if (!day) return;
    const headings = [...document.querySelectorAll('#toc-sections .toc-entry')].map(link => {
      const target = document.getElementById(decodeURIComponent(link.hash.slice(1)));
      return { target, label: link.querySelector('.entry-label').textContent.trim() };
    }).filter(item => item.target && item.target.closest('.lesson-content'));
    let timer;
    let engaged = false;
    function savePosition() {
      clearTimeout(timer);
      if (!engaged) return;
      const edge = document.querySelector('.site-header').getBoundingClientRect().bottom + 24;
      let current;
      for (const item of headings) {
        if (item.target.getBoundingClientRect().top > edge) break;
        current = item;
      }
      if (!current) return;
      const value = JSON.stringify({ day: day[1], anchor: current.target.id, label: current.label });
      if (value !== readSetting(key)) {
        saveSetting(key, value);
      }
    }
    function scheduleSave() {
      engaged = true;
      clearTimeout(timer);
      timer = setTimeout(savePosition, 180);
    }
    window.addEventListener('scroll', scheduleSave, { passive: true });
    window.addEventListener('hashchange', scheduleSave);
    window.addEventListener('pagehide', savePosition);
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') savePosition();
    });
  }

  function init() {
    setupPreferences();
    setupDirectory();
    setupCatalog();
    setupReadingPosition();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();
