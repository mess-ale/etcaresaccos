<template>
    <div class="flex items-center max-w-xs">
      <img :src="imageSrc" alt="Image" class="w-20 h-20 pr-3 object-cover" />
      <div>
        <p class="text-sm">{{ description }}</p>
        <p class="text-sm font-bold mt-1">{{ date }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue'
  
  // Define props for the component
  const props = defineProps({
    imageSrc: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    },
    date: {
      type: String,
      required: true
    }
  })
  </script>
  
  <style scoped>
  </style>
  