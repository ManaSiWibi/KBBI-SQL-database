<script>
  import { onMount } from 'svelte'
  import Icon from './lib/Icon.svelte'
  import HomePage from './pages/HomePage.svelte'
  import SearchPage from './pages/SearchPage.svelte'
  import AboutPage from './pages/AboutPage.svelte'

  const searchTypes = ['all', 'dictionary', 'baku', 'sinonim', 'antonim']
  const legacyTypes = { dictionary: 'dictionary', 'baku-nonbaku': 'baku', sinonim: 'sinonim', antonim: 'antonim' }
  const descriptions = {
    all: 'Cari arti, kata baku dan nonbaku, sinonim, serta antonim dari satu halaman pencarian.',
    dictionary: 'Cari arti dari lebih dari 115 ribu entri dataset open-source KBBI Edisi IV.',
    baku: 'Cari bentuk kata baku dan nonbaku Bahasa Indonesia.',
    sinonim: 'Temukan padanan dan relasi antarkata Bahasa Indonesia.',
    antonim: 'Temukan lawan kata dan jenis oposisi makna Bahasa Indonesia.',
  }
  let route = $state('home')
  let activeType = $state('all')

  function readRoute() {
    const path = location.hash.replace(/^#\/?/, '').split('?')[0] || 'home'
    const params = new URLSearchParams(location.hash.split('?')[1] ?? '')
    if (path === 'home') route = 'home'
    else if (path === 'about') route = 'about'
    else route = 'search'
    activeType = legacyTypes[path] ?? params.get('type') ?? 'all'
    if (!searchTypes.includes(activeType)) activeType = 'all'

    const metadata = route === 'home'
      ? ['KBBI Data Explorer', 'Jelajahi dataset Bahasa Indonesia sumber terbuka dan akses pencarian global untuk kamus, kata baku, sinonim, serta antonim.']
      : route === 'about'
        ? ['Tentang Dataset | KBBI Explorer', 'Informasi sumber, format, dan penggunaan dataset KBBI SQL Database.']
        : ['Pencarian Global | KBBI Data Explorer', descriptions[activeType]]
    document.title = metadata[0]
    document.querySelector('meta[name="description"]')?.setAttribute('content', metadata[1])
    window.scrollTo({ top: 0, behavior: 'instant' })
  }

  function navigate(destination) {
    if (destination === 'home' || destination === 'about' || destination === 'search') {
      location.hash = `/${destination}`
      return
    }
    const type = legacyTypes[destination] ?? destination
    location.hash = `/search?type=${type}`
  }

  function setType(type) {
    location.hash = type === 'all' ? '/search' : `/search?type=${type}`
  }

  onMount(() => {
    readRoute()
    window.addEventListener('hashchange', readRoute)
    return () => window.removeEventListener('hashchange', readRoute)
  })
</script>

<header class="site-header">
  <a class="brand" href="#/home" aria-label="KBBI Data Explorer beranda"><span>K</span><div><strong>KBBI</strong><small>Data Explorer</small></div></a>
  <nav class="desktop-nav" aria-label="Navigasi utama">
    <a class:active={route === 'home'} href="#/home">Beranda</a>
    <a class:active={route === 'search'} href="#/search">Pencarian</a>
    <a class:active={route === 'about'} href="#/about">Tentang</a>
  </nav>
  <a class="github-button" href="https://github.com/dyazincahya/KBBI-SQL-database" target="_blank" rel="noreferrer" aria-label="Buka repositori GitHub"><Icon name="github" /></a>
</header>

<main>
  {#if route === 'home'}<HomePage {navigate} />
  {:else if route === 'about'}<AboutPage />
  {:else}<SearchPage initialType={activeType} {setType} />{/if}
</main>

<footer class="site-footer"><div class="brand footer-brand"><span>K</span><div><strong>KBBI</strong><small>Data Explorer</small></div></div><p>Dataset Bahasa Indonesia sumber terbuka. Bukan layanan resmi KBBI.</p><a href="https://github.com/dyazincahya/KBBI-SQL-database" target="_blank" rel="noreferrer">GitHub ↗</a></footer>

<nav class="mobile-nav main-mobile-nav" aria-label="Navigasi seluler">
  <a class:active={route === 'home'} href="#/home"><Icon name="home" size={19} /><span>Beranda</span></a>
  <a class:active={route === 'search'} href="#/search"><Icon name="search" size={19} /><span>Pencarian</span></a>
  <a class:active={route === 'about'} href="#/about"><Icon name="info" size={19} /><span>Tentang</span></a>
</nav>
