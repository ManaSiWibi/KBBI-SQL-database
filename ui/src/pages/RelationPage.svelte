<script>
  import { onMount } from 'svelte'
  import LoadingState from '../lib/LoadingState.svelte'
  import PageHero from '../lib/PageHero.svelte'
  import SearchBar from '../lib/SearchBar.svelte'
  import { getAntonim, getSinonim, normalize } from '../lib/data.js'
  let { kind } = $props()
  let query = $state(''), data = $state([]), loading = $state(true), error = $state(''), filter = $state('semua')
  const isAntonim = $derived(kind === 'antonim')
  let filters = $derived(isAntonim ? ['semua', ...new Set(data.map((item) => item.jenis_oposisi))] : ['semua', ...new Set(data.map((item) => item.jenis))])
  let results = $derived.by(() => {
    const term = normalize(query)
    return data.filter((item) => (!term || normalize(`${item.kata_a} ${item.kata_b} ${item.penjelasan}`).includes(term)) && (filter === 'semua' || (isAntonim ? item.jenis_oposisi : item.jenis) === filter)).slice(0, 100)
  })
  onMount(async () => { try { data = await (kind === 'antonim' ? getAntonim() : getSinonim()) } catch (e) { error = e.message } finally { loading = false } })
  const pretty = (value) => value?.replaceAll('_', ' ')
</script>
<PageHero eyebrow={isAntonim ? 'Oposisi Makna' : 'Padanan Makna'} title={isAntonim ? 'Kamus Antonim' : 'Kamus Sinonim'} description={isAntonim ? 'Jelajahi pasangan lawan kata beserta jenis oposisi, bidang, dan tingkat keyakinannya.' : 'Temukan relasi padanan kata dan variasi bentuk baku maupun tidak baku.'} />
<section class="browser section-wrap">
  <SearchBar bind:value={query} placeholder={`Cari ${kind}…`} count={results.length} {loading} />
  <div class="filter-chips">{#each filters as option}<button class:active={filter === option} onclick={() => filter = option}>{pretty(option)}</button>{/each}</div>
  {#if error}<div class="message error">{error}</div>{:else if loading}<LoadingState label={`Memuat koleksi ${kind}…`} />{:else}<div class="relation-grid">{#each results as item}<article class="relation-card"><div class="relation-words"><strong>{item.kata_a}</strong><span>{isAntonim ? '↔' : '≈'}</span><strong>{item.kata_b}</strong></div><div class="badges"><span>{pretty(isAntonim ? item.jenis_oposisi : item.jenis)}</span>{#if isAntonim}<span>{item.bidang}</span><span>keyakinan {item.tingkat_keyakinan}</span>{/if}</div><p>{item.penjelasan}</p><div class="examples"><p>{item.penggunaan_a}</p><p>{item.penggunaan_b}</p></div>{#if item.catatan}<footer>{item.catatan}</footer>{/if}</article>{/each}</div>{/if}
  {#if data.length > results.length}<p class="limit-note">Menampilkan hingga 100 entri. Gunakan pencarian atau filter untuk mempersempit hasil.</p>{/if}
</section>
