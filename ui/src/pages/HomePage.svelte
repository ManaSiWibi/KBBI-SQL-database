<script>
  import { onMount } from 'svelte'
  import Icon from '../lib/Icon.svelte'
  import { formatNumber, getManifest } from '../lib/data.js'
  let { navigate } = $props()
  let manifest = $state(null)

  const collections = [
    { route: 'dictionary', icon: 'book', title: 'Kamus Utama', text: 'Temukan arti dan ragam entri dari KBBI Edisi IV.', key: 'dictionary' },
    { route: 'baku-nonbaku', icon: 'check', title: 'Baku & Nonbaku', text: 'Periksa bentuk kata yang sesuai kaidah Bahasa Indonesia.', key: 'bakuNonbaku' },
    { route: 'sinonim', icon: 'link', title: 'Sinonim', text: 'Jelajahi padanan dan hubungan antarkata.', key: 'sinonim' },
    { route: 'antonim', icon: 'swap', title: 'Antonim', text: 'Pahami lawan kata dan jenis oposisi maknanya.', key: 'antonim' },
  ]
  const sources = [
    { name: 'Ican Bachors · KBBI.sql', url: 'https://github.com/bachors/KBBI.sql' },
    { name: 'kbbi-v6-full-csv', url: 'https://github.com/aryakdaniswara/kbbi-v6-full-csv' },
    { name: 'kbbi-v6-categories', url: 'https://github.com/aryakdaniswara/kbbi-v6-categories' },
    { name: 'kbbi-v6-wordlist', url: 'https://github.com/aryakdaniswara/kbbi-v6-wordlist' },
    { name: 'kbbi-dataset-kbbi-v', url: 'https://github.com/aryakdaniswara/kbbi-dataset-kbbi-v' },
    { name: 'raf555 · KBBI-api', url: 'https://github.com/raf555/kbbi-api' },
  ]

  onMount(async () => manifest = await getManifest())
</script>

<section class="home-hero">
  <div class="home-copy">
    <p class="eyebrow"><span></span>Dataset sumber terbuka · Bukan sumber resmi</p>
    <h1>Kata membuka<br /><em>cakrawala.</em></h1>
    <p>Jelajahi arti, bentuk baku, sinonim, dan antonim dari koleksi open-source yang ringan dan mudah ditelusuri. Explorer ini bukan layanan resmi KBBI.</p>
    <div class="hero-actions">
      <button class="primary-button" onclick={() => navigate('dictionary')}>Mulai mencari <Icon name="arrow" /></button>
      <a href="https://github.com/dyazincahya/KBBI-SQL-database" target="_blank" rel="noreferrer">Lihat repositori ↗</a>
    </div>
  </div>
  <div class="word-art" aria-hidden="true">
    <span class="letter letter-k">K</span><span class="letter letter-b">B</span><span class="letter letter-i">I</span>
    <p><strong>ka·ta</strong> <i>n</i> unsur bahasa yang diucapkan atau dituliskan.</p>
  </div>
</section>

<section class="stats" aria-label="Statistik dataset">
  {#each collections as item}
    <div><strong>{manifest ? formatNumber(manifest.count[item.key]) : '—'}</strong><span>{item.title}</span></div>
  {/each}
</section>

<section class="section-wrap home-collections">
  <header class="section-heading"><p class="eyebrow"><span></span>Koleksi Data</p><h2>Jelajahi bahasa dari berbagai sisi</h2></header>
  <div class="collection-grid">
    {#each collections as item, index}
      <button class:featured={index === 0} class="collection-card" onclick={() => navigate(item.route)}>
        <span class="icon-badge"><Icon name={item.icon} size={24} /></span>
        <div><small>0{index + 1}</small><h3>{item.title}</h3><p>{item.text}</p><b>{manifest ? formatNumber(manifest.count[item.key]) : '…'} entri</b></div>
        <Icon name="arrow" />
      </button>
    {/each}
  </div>
</section>

<section class="section-wrap sources-section" aria-labelledby="sources-title">
  <div class="sources-intro">
    <p class="eyebrow"><span></span>Sumber data</p>
    <h2 id="sources-title">Dikurasi dari ekosistem data terbuka.</h2>
    <p>Repositori ini menggabungkan sejumlah sumber data Bahasa Indonesia yang tersedia di internet, khususnya GitHub. Sebagian koleksi relasi kata diperkaya menggunakan kecerdasan buatan.</p>
  </div>
  <div class="source-list">
    {#each sources as source, index}
      <a href={source.url} target="_blank" rel="noreferrer"><span>{String(index + 1).padStart(2, '0')}</span><strong>{source.name}</strong><b>↗</b></a>
    {/each}
    <div class="ai-source"><span>AI</span><p><strong>Data hasil pengayaan AI</strong><small>Baku & Nonbaku, Sinonim, serta Antonim dibuat menggunakan GPT-5.6 Sol.</small></p></div>
  </div>
</section>

<section class="section-wrap data-notice" aria-labelledby="data-ownership-title">
  <div class="notice-heading">
    <p class="eyebrow"><span></span>Kredit & penggunaan data</p>
    <h2 id="data-ownership-title">Sumber terbuka, hak data tetap dihormati.</h2>
  </div>
  <div class="notice-content">
    <p>Seluruh data kamus dimiliki oleh <strong>Badan Pengembangan dan Pembinaan Bahasa, Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi Republik Indonesia</strong>.</p>
    <p>Penggunaan komersial dilarang dan tunduk pada Undang-Undang Republik Indonesia Nomor 28 Tahun 2014 tentang Hak Cipta.</p>
    <small>Ikon kamus pada dokumentasi disediakan oleh <a href="https://www.flaticon.com/free-icon/dictionary_7214200?related_id=7214200" target="_blank" rel="noreferrer">Flaticon ↗</a></small>
  </div>
</section>
