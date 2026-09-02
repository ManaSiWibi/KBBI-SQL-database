<script>
  let { label = 'Memuat data…', compact = false } = $props()
</script>

<div class:compact class="loading-state" role="status" aria-live="polite">
  <span class="loading-spinner" aria-hidden="true"></span>
  <div>
    <strong>{label}</strong>
    {#if !compact}<small>Mohon tunggu sebentar.</small>{/if}
  </div>
</div>
