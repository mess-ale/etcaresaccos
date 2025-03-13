<script setup>
import { onMounted } from 'vue';
import gsap from 'gsap';

onMounted(() => {
  gsap.to('.overlay-svg circle', {
    duration: 25,
    scale: 0.8,
    yoyo: true,
    repeat: -1,
    ease: 'power1.inOut',
    stagger: 0.1
  });
});
</script>

<template>
  <svg
    class="overlay-svg"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 100 100"
    width="100%"
    height="100%"
  >
    <circle cx="-30" cy="10" r="50" fill="url(#grad1)" />
    <circle cx="20" cy="0" r="20" fill="url(#grad2)" />
    <circle cx="140" cy="90" r="50" fill="url(#grad1)" />
    <circle cx="90" cy="100" r="20" fill="url(#grad2)" />
    <defs>
      <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color: #214080; stop-opacity: 1" />
        <stop offset="100%" style="stop-color: #d92a27; stop-opacity: 1" />
      </linearGradient>
      <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color: #214080; stop-opacity: 1" />
        <stop offset="100%" style="stop-color: #d92a27; stop-opacity: 1" />
      </linearGradient>
    </defs>
  </svg>
</template>
