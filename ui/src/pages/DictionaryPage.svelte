<script>
  import { onMount } from 'svelte'
  import LoadingState from '../lib/LoadingState.svelte'
  import PageHero from '../lib/PageHero.svelte'
  import SearchBar from '../lib/SearchBar.svelte'
  import { definitionToText, getDictionaryIndex, getDictionaryShard, normalize } from '../lib/data.js'

  let queryInput = $state('')
  let query = $state('')
  let index = $state([])
  let selected = $state(null)
  let selectedWord = $state('')
  let loading = $state(true)
  let searching = $state(false)
  let detailLoading = $state(false)
  let error = $state('')

  $effect(() => {
    const nextQuery = queryInput
    searching = nextQuery !== query
    const timer = setTimeout(() => {
      query = nextQuery
      searching = false
    }, 250)
    return () => clearTimeout(timer)
  })

  let results = $derived.by(() => {
    const term = normalize(query)
    if (term.length < 2) return []
    const uniqueWords = new Map()
    for (const item of index) {
      const word = normalize(item.word)
      if (word.includes(term) && !uniqueWords.has(word)) uniqueWords.set(word, item)
    }
    return [...uniqueWords.values()]
      .sort((a, b) => Number(!normalize(a.word).startsWith(term)) - Number(!normalize(b.word).startsWith(term)) || a.word.localeCompare(b.word, 'id'))
      .slice(0, 60)
  })

  onMount(async () => {
    try { index = await getDictionaryIndex() }
    catch (cause) { error = cause.message }
    finally { loading = false }
  })

  async function openEntry(item) {
    selectedWord = normalize(item.word)
    detailLoading = true
    try {
      const shard = await getDictionaryShard(item.letter)
      selected = shard.filter((record) => normalize(record.word) === normalize(item.word))
    } catch (cause) { error = cause.message }
    finally { detailLoading = false }
  }
</script>

<PageHero eyebrow="Dataset sumber terbuka · Bukan sumber resmi" title="Kamus Besar Bahasa Indonesia" description="Telusuri lebih dari seratus ribu entri koleksi open-source KBBI Edisi IV. Halaman ini bukan layanan resmi KBBI." />
<section class="browser section-wrap">
  <SearchBar bind:value={queryInput} placeholder="Cari kata, misalnya: bahasa" count={results.length} loading={loading || searching} loadingLabel={loading ? 'Memuat kamus…' : 'Mencari…'} />
  {#if error}<div class="message error">{error}</div>
  {:else if loading}<LoadingState label="Menyiapkan indeks kamus…" />
  {:else if searching}<LoadingState label="Mencari kata dalam kamus…" compact />
  {:else if !queryInput || queryInput.length < 2}<div class="search-prompt"><span>ab</span><h2>Apa kata yang ingin Anda temukan?</h2><p>Masukkan sedikitnya dua karakter. Hasil terbaik akan ditampilkan lebih dahulu.</p></div>
  {:else if !results.length && !loading}<div class="message">Kata tidak ditemukan.</div>
  {:else}
    <div class="dictionary-layout">
      <div class="word-list" aria-label="Hasil pencarian" aria-busy={searching}>
        {#if searching}<div class="list-loading"><i class="mini-spinner" aria-hidden="true"></i>Memperbarui hasil…</div>{/if}
        {#each results as item}<button class:active={selectedWord === normalize(item.word)} onclick={() => openEntry(item)}><strong>{item.word}</strong><small>Lihat semua definisi</small><span>→</span></button>{/each}
      </div>
      <aside class="definition-panel">
        {#if detailLoading}<LoadingState label="Memuat definisi…" compact />
        {:else if selected}
          <p class="definition-label">Entri kamus</p><h2>{selected[0].word}</h2>
          {#each selected as entry, index}<article><span>{index + 1}</span><p>{definitionToText(entry.arti)}</p></article>{/each}
        {:else}<div class="empty-detail"><span>Aa</span><p>Pilih salah satu kata untuk membaca artinya.</p></div>{/if}
      </aside>
    </div>
  {/if}
</section>
