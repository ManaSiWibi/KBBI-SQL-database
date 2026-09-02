<script>
  import Icon from './Icon.svelte'
  let { value = $bindable(''), placeholder = 'Cari kata…', count, loading = false, loadingLabel = 'Memuat…' } = $props()
</script>

<div class="toolbar">
  <label class="search-box">
    <Icon name="search" size={19} />
    <span class="sr-only">Pencarian</span>
    <input bind:value {placeholder} autocomplete="off" spellcheck="false" />
    {#if value}<button type="button" aria-label="Hapus pencarian" onclick={() => value = ''}>×</button>{/if}
  </label>
  <span class:loading class="result-count" aria-live="polite">
    {#if loading}<i class="mini-spinner" aria-hidden="true"></i>{loadingLabel}{:else}{count.toLocaleString('id-ID')} hasil{/if}
  </span>
</div>
