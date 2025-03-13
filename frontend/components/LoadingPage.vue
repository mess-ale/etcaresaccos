<template>
    <div class="w-full flex flex-col items-center justify-center bg-[#EEF4FF]">
      <!-- Spinner -->
      <div class="relative w-20 h-20 mb-8">
        <div class="absolute inset-0 border-4 border-[#214080] rounded-full animate-spin"></div>
        <div class="absolute inset-0 border-4 border-[#D92A27] border-t-transparent rounded-full animate-spin"></div>
      </div>
  
      <!-- Loading Text -->
      <h2 class="text-2xl font-semibold text-[#214080] mb-4 animate-pulse">
        Loading...
      </h2>
  
      <!-- Progress Bar -->
      <div class="w-64 h-2 bg-gray-200 rounded-full overflow-hidden">
        <div 
          class="h-full bg-[#D92A27] transition-all duration-1000 ease-out"
          :style="{ width: progress + '%' }"
        ></div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        progress: 0
      }
    },
    mounted() {
      // Simulate loading progress
      const interval = setInterval(() => {
        this.progress += Math.random() * 15
        if (this.progress >= 100) {
          this.progress = 100
          clearInterval(interval)
        }
      }, 500)
    }
  }
  </script>
  
  <style scoped>
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
  
  .animate-spin {
    animation: spin 1.2s linear infinite;
  }
  </style>