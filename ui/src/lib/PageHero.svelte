<script>
  let { eyebrow = 'Pustaka Bahasa Indonesia', title, description } = $props()
</script>

<section class="page-hero">
  <div class="page-hero-inner">
    <p class="eyebrow"><span></span>{eyebrow}</p>
    <h1>{title}</h1>
    <p>{description}</p>
  </div>
</section>
