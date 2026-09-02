<script>
  import { onMount } from 'svelte'
  import LoadingState from '../lib/LoadingState.svelte'
  import PageHero from '../lib/PageHero.svelte'
  import SearchBar from '../lib/SearchBar.svelte'
  import { getBakuNonbaku, normalize } from '../lib/data.js'

  let query = $state('')
  let data = $state([])
  let loading = $state(true)
  let error = $state('')
  let selected = $state(null)

  let results = $derived.by(() => {
    const term = normalize(query)
    const source = term
      ? data.filter((item) => normalize(`${item.word} ${item.wrong}`).includes(term))
      : data
    return source.slice(0, 80)
  })

  $effect(() => {
    if (!selected) return
    document.body.style.overflow = 'hidden'
    return () => { document.body.style.overflow = '' }
  })

  onMount(async () => {
    try { data = await getBakuNonbaku() }
    catch (cause) { error = cause.message }
    finally { loading = false }
  })

  function closeModal() {
    selected = null
  }

  function handleKeydown(event) {
    if (event.key === 'Escape' && selected) closeModal()
  }

  function closeFromBackdrop(event) {
    if (event.target === event.currentTarget) closeModal()
  }
</script>

<svelte:window onkeydown={handleKeydown} />

<PageHero eyebrow="Ketepatan Berbahasa" title="Kata Baku & Nonbaku" description="Bandingkan bentuk kata yang sesuai kaidah dengan variasi penulisan yang umum dijumpai." />
<section class="browser section-wrap">
  <SearchBar bind:value={query} placeholder="Cari bentuk baku atau nonbaku…" count={results.length} {loading} />
  {#if error}
    <div class="message error">{error}</div>
  {:else if loading}
    <LoadingState label="Memuat koleksi kata baku…" />
  {:else}
    <div class="pair-grid">
      {#each results as item}
        <article class="pair-card">
          <div class="pair-words">
            <div><small>Bentuk baku</small><strong>{item.word}</strong></div>
            <span>≠</span>
            <div><small>Nonbaku</small><s>{item.wrong}</s></div>
          </div>
          <button class="detail-button" type="button" onclick={() => selected = item}>
            Baca penjelasan <span>→</span>
          </button>
        </article>
      {/each}
    </div>
  {/if}
  {#if !query && data.length > results.length}
    <p class="limit-note">Menampilkan 80 entri pertama. Gunakan pencarian untuk hasil yang lebih spesifik.</p>
  {/if}
</section>

{#if selected}
  <div class="modal-backdrop" role="presentation" onclick={closeFromBackdrop}>
    <div class="word-modal" role="dialog" aria-modal="true" aria-labelledby="word-modal-title">
      <div class="word-modal-scroll">
      <header>
        <div>
          <p class="eyebrow"><span></span>Detail kata</p>
          <h2 id="word-modal-title">{selected.word}</h2>
        </div>
        <button class="modal-close" type="button" aria-label="Tutup detail" onclick={closeModal}>×</button>
      </header>
      <div class="modal-pair">
        <div><small>Bentuk baku</small><strong>{selected.word}</strong></div>
        <span>≠</span>
        <div><small>Bentuk nonbaku</small><s>{selected.wrong}</s></div>
      </div>
      <div class="modal-section">
        <small>Penjelasan</small>
        <p>{selected.explain}</p>
      </div>
      {#if selected.clue}
        <div class="modal-section clue-section">
          <small>Petunjuk kata</small>
          <p>{selected.clue}</p>
        </div>
      {/if}
      </div>
    </div>
  </div>
{/if}
