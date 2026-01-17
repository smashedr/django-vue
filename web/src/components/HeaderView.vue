<script setup lang="ts">
import { RouterLink } from 'vue-router'
import router from '../router/index.ts'
import ThemeSwitch from '@/components/ThemeSwitch.vue'
import { SETTINGS } from '@/config/settings.ts'
</script>

<template>
  <nav aria-label="Primary Navigation" class="navbar navbar-expand-sm bg-body-tertiary mb-2">
    <div class="container-fluid">
      <RouterLink to="/" class="px-2">
        <img alt="logo" src="/src/assets/logo.png" width="30" height="30" class="my-auto"
      /></RouterLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <!-- main navigation -->
      <div class="collapse navbar-collapse me-auto" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto">
          <li class="nav-item" v-for="{ meta, path } in router.options.routes" :key="path">
            <RouterLink :to="path" class="nav-link" active-class="active">{{
              meta?.name
            }}</RouterLink>
            <!--<a class="nav-link" :href="link"-->
            <!--  >{{ name }} <i class="fa-solid fa-arrow-up-right-from-square fa-sm"></i-->
            <!--&gt;</a>-->
          </li>
        </ul>
        <ul class="navbar-nav nav-icons d-flex flex-row">
          <li class="nav-item">
            <a
              class="nav-link hvr-grow-lg heart"
              :href="SETTINGS.kofi"
              target="_blank"
              rel="noopener"
            >
              <i class="fa-classic fa-solid fa-heart fa-xl"></i
            ></a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link hvr-grow-lg discord"
              :href="SETTINGS.discord"
              target="_blank"
              rel="noopener"
            >
              <i class="fa-brands fa-discord fa-xl"></i
            ></a>
          </li>
          <li class="nav-item">
            <a class="nav-link hvr-grow-lg" :href="SETTINGS.github" target="_blank" rel="noopener">
              <i class="fa-brands fa-github fa-xl"></i
            ></a>
          </li>
          <ThemeSwitch />
        </ul>
      </div>
    </div>
  </nav>
</template>

<!--<style scoped></style>-->
