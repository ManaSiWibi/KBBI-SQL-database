<script>
  import Icon from '../lib/Icon.svelte'
  import PageHero from '../lib/PageHero.svelte'

  const repository = 'https://github.com/dyazincahya/KBBI-SQL-database'
  const datasets = [
    {
      id: 'dictionary', name: 'Kamus Utama', folder: 'edisi-IV', type: 'Definisi kata', records: '115.978',
      formats: ['JSON', 'CSV', 'MySQL', 'PostgreSQL', 'SQLite', 'XML', 'HTML', 'Markdown', 'PHP Array', 'DbUnit'],
    },
    {
      id: 'baku', name: 'Baku & Nonbaku', folder: 'baku-nonbaku', type: 'Relasi ejaan', records: '2.847',
      formats: ['JSON', 'CSV', 'MySQL', 'PostgreSQL', 'SQLite', 'XML', 'HTML', 'Markdown', 'PHP Array', 'DbUnit', 'Text'],
    },
    {
      id: 'sinonim', name: 'Sinonim', folder: 'sinonim', type: 'Relasi makna', records: '4.625',
      formats: ['JSON', 'CSV', 'MySQL', 'PostgreSQL', 'SQLite', 'XML', 'HTML', 'Markdown', 'PHP Array', 'DbUnit', 'Text'],
    },
    {
      id: 'antonim', name: 'Antonim', folder: 'antonim', type: 'Oposisi makna', records: '549',
      formats: ['JSON', 'CSV', 'MySQL', 'PostgreSQL', 'SQLite', 'XML', 'HTML', 'Markdown', 'PHP Array', 'DbUnit', 'Text'],
    },
  ]
  const schemas = [
    { dataset: 'Kamus Utama', root: 'dictionary', fields: ['_id', 'word', 'arti', 'type'], note: 'type 1 = HTML, type 2 = teks biasa' },
    { dataset: 'Baku & Nonbaku', root: 'quiz_baku', fields: ['id', 'word', 'wrong', 'explain', 'clue'], note: 'clue dapat bernilai null' },
    { dataset: 'Sinonim', root: 'dictionary_sinonim', fields: ['id', 'kata_a', 'kata_b', 'jenis', 'penjelasan', 'penggunaan_a', 'penggunaan_b'], note: 'Sinonim dan varian baku/nonbaku' },
    { dataset: 'Antonim', root: 'dictionary_antonim', fields: ['id', 'kata_a', 'kata_b', 'jenis_oposisi', 'bidang', 'tingkat_keyakinan', 'penjelasan', 'penggunaan_a', 'penggunaan_b', 'catatan'], note: 'Oposisi kontekstual, komplementer, relasional, dan reversif' },
  ]
</script>

<PageHero eyebrow="Dokumentasi Developer" title="Data siap digunakan." description="Pelajari koleksi, format file, dan struktur JSON yang tersedia sebelum mengintegrasikannya ke aplikasi Anda." />

<section class="section-wrap developer-page">
  <div class="developer-intro">
    <div><Icon name="layers" size={20} /><p><span>4</span><small>Koleksi data</small></p></div>
    <div><Icon name="database" size={20} /><p><span>123.999</span><small>Total record</small></p></div>
    <div><Icon name="table" size={20} /><p><span>11</span><small>Format tersedia</small></p></div>
    <div><Icon name="file" size={20} /><p><span>JSON</span><small>Format UI explorer</small></p></div>
  </div>

  <section class="api-integration" aria-labelledby="api-integration-title">
    <div class="api-brand" aria-hidden="true">
      <span><Icon name="php" size={44} /></span>
      <i>+</i>
      <span><Icon name="codeigniter" size={38} /></span>
    </div>
    <div class="api-copy">
      <p class="eyebrow"><span></span>Integrasi API</p>
      <h2 id="api-integration-title">API KBBI PHP CodeIgniter 4</h2>
      <p>Jika data lokal belum mencukupi, gunakan layanan ini untuk mengambil data dinamis yang bersumber langsung dari portal resmi KBBI Daring Kemendikdasmen.</p>
      <div class="api-links">
        <a class="primary-button" href="https://github.com/dyazincahya/API-KBBI-PHP-CodeIgniter-4" target="_blank" rel="noreferrer"><Icon name="github" size={16} />Lihat repository <Icon name="external" size={10} /></a>
        <a href="https://kbbi.kemendikdasmen.go.id/" target="_blank" rel="noreferrer">KBBI Daring Kemendikdasmen <Icon name="external" size={10} /></a>
      </div>
    </div>
  </section>

  <section class="developer-section" aria-labelledby="dataset-table-title">
    <header class="developer-heading">
      <div><p class="eyebrow"><span></span>Inventaris data</p><h2 id="dataset-table-title">Koleksi dan format file</h2></div>
      <p>Setiap koleksi tersedia sebagai file statis yang dapat diunduh langsung dari repository.</p>
    </header>
    <div class="table-frame">
      <table class="data-table">
        <thead><tr><th>Koleksi</th><th>Tipe data</th><th>Record</th><th>Format tersedia</th><th><span class="sr-only">Akses</span></th></tr></thead>
        <tbody>
          {#each datasets as dataset}
            <tr>
              <td><strong>{dataset.name}</strong><code>/{dataset.folder}</code></td>
              <td>{dataset.type}</td>
              <td><b>{dataset.records}</b></td>
              <td><div class="format-list">{#each dataset.formats as format}<span class:primary={format === 'JSON'}>{format}</span>{/each}</div></td>
              <td><a href={`${repository}/tree/main/${dataset.folder}`} target="_blank" rel="noreferrer" aria-label={`Buka folder ${dataset.name}`}><Icon name="external" size={14} /></a></td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </section>

  <section class="developer-section" aria-labelledby="schema-table-title">
    <header class="developer-heading">
      <div><p class="eyebrow"><span></span>Referensi JSON</p><h2 id="schema-table-title">Struktur dan tipe field</h2></div>
      <p>Semua file JSON memakai objek root yang membungkus array record.</p>
    </header>
    <div class="table-frame">
      <table class="data-table schema-table">
        <thead><tr><th>Dataset</th><th>Root key</th><th>Field record</th><th>Keterangan</th></tr></thead>
        <tbody>
          {#each schemas as schema}
            <tr><td><strong>{schema.dataset}</strong></td><td><code>{schema.root}</code></td><td><div class="field-list">{#each schema.fields as field}<code>{field}</code>{/each}</div></td><td>{schema.note}</td></tr>
          {/each}
        </tbody>
      </table>
    </div>
  </section>

  <aside class="developer-note">
    <Icon name="info" size={24} />
    <div><strong>Catatan integrasi</strong><p>File kamus utama berukuran besar. Untuk aplikasi web, gunakan pagination, indexing, Web Worker, atau pecah data berdasarkan huruf seperti pipeline pada UI explorer ini.</p></div>
    <a href={`${repository}/tree/main/ui/scripts`} target="_blank" rel="noreferrer"><Icon name="terminal" size={12} />Lihat pipeline data <Icon name="external" size={10} /></a>
  </aside>
</section>
