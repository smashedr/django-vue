<script setup lang="ts">
import { SETTINGS } from '@/config/settings.ts'
import { aboutBadges, aboutLinks } from '@/config/links.ts'
import GHStatsCard from '@/components/GHStatsCard.vue'
</script>

<template>
  <div class="container-fluid">
    <h1 class="animate__animated animate__zoomIn">
      <i class="fa-regular fa-address-card me-2"></i> About
    </h1>

    <div
      class="d-flex flex-column flex-wrap flex-sm-row align-items-start"
      style="min-height: 24px"
    >
      <a
        v-for="{ alt, href, src } in aboutBadges"
        :key="src"
        :href="href"
        class="me-2 mb-1"
        target="_blank"
        rel="noopener"
      >
        <img :alt="alt" :src="src" height="24"
      /></a>
    </div>

    <hr />

    <figure>
      <blockquote class="blockquote">
        Give a man a fish, and you feed him for a day. Teach a man to fish, and you feed him for a
        lifetime...
      </blockquote>
      <figcaption class="blockquote-footer">
        Lao-Tzu in <cite title="Source Title">Tao Te Ching</cite>
      </figcaption>
    </figure>

    <div class="d-flex flex-column flex-md-row">
      <div class="me-md-3 mb-2 mb-md-0">
        <GHStatsCard
          href="https://github.com/smashedr"
          src="https://github-readme-stats.cssnr.com/?username=smashedr&show_icons=true&hide_rank=true&show=reviews&card_width=350"
        />
      </div>
      <div class="me-md-3">
        <GHStatsCard
          href="https://github.com/smashedr"
          src="https://github-readme-stats.cssnr.com/top-langs/?username=smashedr&layout=donut"
        />
      </div>
    </div>

    <p class="fst-italic">
      Note: These stats only include personal repositories; however, most my work is done in the
      <a :href="SETTINGS.github" target="_blank" rel="noopener">CSSNR Organization</a>.
    </p>

    <div class="d-flex flex-column flex-md-row">
      <div class="me-md-5">
        <h2>Links</h2>
        <ul class="list-unstyled ms-3">
          <li v-for="{ icon, text, href } in aboutLinks" :key="icon">
            <i :class="icon" class="me-2"></i>
            <a :href="href" target="_blank" rel="noopener">{{ text }}</a>
          </li>
        </ul>
      </div>

      <div class="me-md-5">
        <h2>Development</h2>
        <ul>
          <li>Web Extensions</li>
          <li>GitHub Actions</li>
          <li>Docker Containers</li>
          <li>Django Applications</li>
          <li>Mobile Applications</li>
          <li>NPM/Python Packages</li>
        </ul>
      </div>
    </div>

    <h1>Support</h1>
    <p>Please consider making a donation to support this development...</p>
    <a :href="SETTINGS.kofi" target="_blank" rel="noopener">
      <img
        alt="Support on Ko-fi"
        class="img-fluid hvr-grow"
        style="max-height: 64px"
        src="https://cdn.prod.website-files.com/5c14e387dab576fe667689cf/670f5a01c01ea9191809398c_support_me_on_kofi_blue.png"
      />
    </a>

    <p class="lead mt-3">More Information Coming Soon...</p>

    <hr />

    <p>
      This site is built with Jekyll and hosted on GitHub Pages.
      <br />
      View the source code on GitHub:
      <a :href="SETTINGS.github" target="_blank" rel="noopener"> {{ SETTINGS.github }}</a>
    </p>
  </div>
</template>

<!--<style scoped></style>-->
