<script setup lang="ts">
const props = defineProps<{
  href: string
  src: string
}>()
</script>

<template>
  <a :href="props.href" class="text-decoration-none" target="_blank" rel="noopener">
    <picture>
      <source
        :srcset="`${props.src}&theme=dark`"
        media="(prefers-color-scheme: dark), (prefers-color-scheme: no-preference)"
      />
      <source :srcset="`${props.src}&theme=default`" media="(prefers-color-scheme: light)" />
      <img alt="GitHub Stats Dynamic Display" class="img-fluid" :src="props.src" />
    </picture>
  </a>
</template>

<!--<style scoped></style>-->
