<template>
  <div class="flex items-center max-w-xs">
    <img :src="`http://127.0.0.1:8000${imageSrc}`" alt="Image" class=" w-20 h-20 pr-3 rounded-md object-cover" />
    <nuxt-link :to="`/blog/${blog_id}`" class="foter-class">
      <div>
        <p class="text-sm">{{ description }}</p>
        <p class="text-sm font-bold mt-1">{{ date }}</p>
      </div>
    </nuxt-link>

  </div>
</template>

<script>
export default {
  props: {
    description: { type: String, required: true },
    summary: { type: String, default: "" },
    imageSrc: { type: String, required: true },
    content: { type: String, required: true },
    author: { type: String, required: true },
    date: { type: String, required: true },
    blog_id: { type: Number, required: true },
  },
};
</script>

<style scoped>
.foter-class {
  transition: all 0.35s ease-in-out; 
}

.foter-class:hover {
  font-weight: bold;
  transform: scale(1.05); 
  text-shadow: 0 0 5px rgba(0, 0, 0, 0.2); 
}

.foter-class:not(:hover) { 
    transform: scale(1.0); 
    text-shadow: none; 
}
</style>