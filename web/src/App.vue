<script setup lang="ts">
import HeaderView from '@/components/HeaderView.vue'
import FooterView from '@/components/FooterView.vue'
</script>

<template>
  <header>
    <HeaderView />
  </header>

  <main class="flex-grow-1 px-0 px-sm-3">
    <RouterView />
  </main>

  <footer class="footer mt-auto px-1 flex-shrink-0 bg-body-tertiary">
    <FooterView />
  </footer>
</template>

<!--<style scoped></style>-->
