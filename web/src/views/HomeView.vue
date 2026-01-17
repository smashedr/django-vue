<script setup lang="ts">
import { ref } from 'vue'

const vite_title = import.meta.env.VITE_TITLE
console.log('vite_title:', vite_title)
const vite_description = import.meta.env.VITE_DESCRIPTION
console.log('vite_description:', vite_description)

const responseRef = ref('If only someone (no name) would break something...')

const breakSomething = async () => {
  const data = { action: 'break', data: 'something' }
  try {
    const response = await fetch('/api/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
    console.log('response.status:', response.status)
    responseRef.value = await response.text()
  } catch (e) {
    console.log('error:', e)
    if (e instanceof Error) responseRef.value = e.message
  }
}
</script>

<template>
  <div class="container-fluid">
    <p>VITE_TITLE: {{ vite_title }}</p>
    <p>VITE_DESCRIPTION: {{ vite_description }}</p>
    <button type="button" class="btn btn-primary" @click="breakSomething">Break Something</button>
    <hr />
    <pre v-html="responseRef"></pre>
  </div>
</template>

<!--<style scoped></style>-->
