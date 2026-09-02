<script>
  import { onMount } from 'svelte'
  import Icon from '../lib/Icon.svelte'
  import LoadingState from '../lib/LoadingState.svelte'
  import { definitionToText, getAntonim, getBakuNonbaku, getDictionaryIndex, getDictionaryShard, getSinonim, normalize } from '../lib/data.js'

  let { initialType = 'all', setType } = $props()
  const types = [
    { id: 'all', label: 'Semua' },
    { id: 'dictionary', label: 'Kamus' },
    { id: 'baku', label: 'Baku & Nonbaku' },
    { id: 'sinonim', label: 'Sinonim' },
    { id: 'antonim', label: 'Antonim' },
  ]
  let queryInput = $state('')
  let query = $state('')
  let activeType = $state('all')
  let dictionary = $state([])
  let baku = $state([])
  let sinonim = $state([])
  let antonim = $state([])
  let loading = $state(true)
  let searching = $state(false)
  let detailLoading = $state(false)
  let error = $state('')
  let selected = $state(null)

  $effect(() => { activeType = initialType })
  $effect(() => {
    const nextQuery = queryInput
    searching = nextQuery !== query
    const timer = setTimeout(() => {
      query = nextQuery
      searching = false
    }, 250)
    return () => clearTimeout(timer)
  })
  $effect(() => {
    if (!selected) return
    document.body.style.overflow = 'hidden'
    return () => { document.body.style.overflow = '' }
  })

  const matches = (values, term) => normalize(values.join(' ')).includes(term)
  let results = $derived.by(() => {
    const term = normalize(query)
    if (term.length < 2) return []
    const output = []
    if (activeType === 'all' || activeType === 'dictionary') {
      const seen = new Set()
      for (const item of dictionary) {
        const word = normalize(item.word)
        if (word.includes(term) && !seen.has(word)) {
          seen.add(word)
          output.push({ type: 'dictionary', title: item.word, subtitle: 'Entri kamus', source: item })
          if (activeType === 'all' && seen.size >= 16) break
          if (activeType === 'dictionary' && seen.size >= 60) break
        }
      }
    }
    if (activeType === 'all' || activeType === 'baku') {
      const limit = activeType === 'all' ? 12 : 60
      for (const item of baku) {
        if (matches([item.word, item.wrong], term)) output.push({ type: 'baku', title: item.word, counterpart: item.wrong, subtitle: 'Baku & nonbaku', source: item })
        if (output.filter((entry) => entry.type === 'baku').length >= limit) break
      }
    }
    for (const [type, records] of [['sinonim', sinonim], ['antonim', antonim]]) {
      if (activeType !== 'all' && activeType !== type) continue
      const limit = activeType === 'all' ? 12 : 60
      let count = 0
      for (const item of records) {
        if (matches([item.kata_a, item.kata_b, item.penjelasan], term)) {
          output.push({ type, title: item.kata_a, counterpart: item.kata_b, subtitle: type === 'sinonim' ? 'Sinonim' : 'Antonim', source: item })
          count += 1
        }
        if (count >= limit) break
      }
    }
    return output
  })

  onMount(async () => {
    try {
      [dictionary, baku, sinonim, antonim] = await Promise.all([
        getDictionaryIndex(), getBakuNonbaku(), getSinonim(), getAntonim(),
      ])
    } catch (cause) { error = cause.message }
    finally { loading = false }
  })

  function chooseType(type) {
    activeType = type
    setType(type)
  }

  async function openResult(result) {
    detailLoading = true
    try {
      if (result.type === 'dictionary') {
        const records = await getDictionaryShard(result.source.letter)
        selected = { ...result, records: records.filter((record) => normalize(record.word) === normalize(result.title)) }
      } else selected = result
    } catch (cause) { error = cause.message }
    finally { detailLoading = false }
  }

  function closeModal() { selected = null }
  function closeFromBackdrop(event) { if (event.target === event.currentTarget) closeModal() }
  function handleKeydown(event) { if (event.key === 'Escape') closeModal() }
  const typeLabel = (type) => types.find((item) => item.id === type)?.label ?? type
</script>

<svelte:window onkeydown={handleKeydown} />

<section class:has-query={queryInput.length >= 2} class="search-engine-hero">
  <div class="search-engine-copy">
    <p class="eyebrow"><span></span>Dataset sumber terbuka · Bukan sumber resmi</p>
    <h1>Temukan kata,<br /><em>pahami makna.</em></h1>
    <p>Cari arti, bentuk baku, sinonim, dan antonim Bahasa Indonesia dari satu tempat.</p>
  </div>
  <label class="engine-search">
    <Icon name="search" size={23} />
    <span class="sr-only">Cari seluruh koleksi</span>
    <input bind:value={queryInput} placeholder="Ketik kata yang ingin dicari…" autocomplete="off" />
    {#if searching}<i class="mini-spinner" aria-hidden="true"></i>{/if}
    {#if queryInput}<button type="button" aria-label="Hapus pencarian" onclick={() => queryInput = ''}>×</button>{/if}
  </label>
  <div class="engine-filters" aria-label="Filter tipe data">
    {#each types as type}<button class:active={activeType === type.id} onclick={() => chooseType(type.id)}>{type.label}</button>{/each}
  </div>
</section>

<section class="search-results section-wrap" aria-live="polite">
  {#if error}
    <div class="message error">{error}</div>
  {:else if loading}
    <LoadingState label="Menyiapkan seluruh koleksi…" />
  {:else if searching}
    <LoadingState label="Mencari di seluruh koleksi…" compact />
  {:else if query.length < 2}
    <div class="engine-empty"><span>Aa</span><h2>Satu pencarian untuk semua data</h2><p>Ketik sedikitnya dua karakter, lalu pilih tipe data jika ingin hasil yang lebih spesifik.</p></div>
  {:else if !results.length}
    <div class="engine-empty"><span>?</span><h2>Hasil tidak ditemukan</h2><p>Coba kata lain atau pilih filter “Semua”.</p></div>
  {:else}
    <header class="results-heading"><div><p class="eyebrow"><span></span>Hasil pencarian</p><h2>“{query}”</h2></div><strong>{results.length} hasil</strong></header>
    <div class="unified-results">
      {#each results as result}
        <button class="unified-result" onclick={() => openResult(result)}>
          <span class="result-type">{typeLabel(result.type)}</span>
          <div><h3>{result.title}{#if result.counterpart}<span>{result.type === 'baku' || result.type === 'antonim' ? ' ≠ ' : ' ≈ '}{result.counterpart}</span>{/if}</h3><p>{result.subtitle}</p></div>
          <Icon name="arrow" />
        </button>
      {/each}
    </div>
  {/if}
</section>

{#if detailLoading}
  <div class="floating-loader"><i class="loading-spinner"></i><span>Memuat detail…</span></div>
{/if}

{#if selected}
  <div class="modal-backdrop" role="presentation" onclick={closeFromBackdrop}>
    <div class="word-modal" role="dialog" aria-modal="true" aria-labelledby="search-detail-title">
      <div class="word-modal-scroll">
        <header><div><p class="eyebrow"><span></span>{typeLabel(selected.type)}</p><h2 id="search-detail-title">{selected.title}</h2></div><button class="modal-close" aria-label="Tutup detail" onclick={closeModal}>×</button></header>
        {#if selected.type === 'dictionary'}
          <div class="modal-section dictionary-detail">{#each selected.records as record, index}<article><span>{index + 1}</span><p>{definitionToText(record.arti)}</p></article>{/each}</div>
        {:else if selected.type === 'baku'}
          <div class="modal-pair"><div><small>Bentuk baku</small><strong>{selected.source.word}</strong></div><span>≠</span><div><small>Nonbaku</small><s>{selected.source.wrong}</s></div></div>
          <div class="modal-section"><small>Penjelasan</small><p>{selected.source.explain}</p></div>
          {#if selected.source.clue}<div class="modal-section clue-section"><small>Petunjuk kata</small><p>{selected.source.clue}</p></div>{/if}
        {:else}
          <div class="modal-pair"><div><small>Kata pertama</small><strong>{selected.source.kata_a}</strong></div><span>{selected.type === 'antonim' ? '≠' : '≈'}</span><div><small>Kata kedua</small><strong>{selected.source.kata_b}</strong></div></div>
          <div class="modal-section"><small>Penjelasan</small><p>{selected.source.penjelasan}</p></div>
          <div class="modal-section clue-section"><small>Contoh penggunaan</small><p>{selected.source.penggunaan_a}</p><p>{selected.source.penggunaan_b}</p></div>
          {#if selected.source.catatan}<div class="modal-section"><small>Catatan</small><p>{selected.source.catatan}</p></div>{/if}
        {/if}
      </div>
    </div>
  </div>
{/if}
