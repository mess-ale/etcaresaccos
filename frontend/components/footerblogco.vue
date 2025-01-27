<template>
  <div class="flex items-center max-w-xs">
    <img :src="`http://127.0.0.1:8000${imageSrc}`" alt="Image" class=" w-20 h-20 pr-3 rounded-md object-cover" />
    <nuxt-link :to="`/blog/${blog_id}`" class="hover:font-bold">
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

<style scoped></style>