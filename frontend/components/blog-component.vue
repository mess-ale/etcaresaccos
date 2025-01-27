<template>
  <div class="blog-card bg-white shadow-md rounded-lg overflow-hidden">
    <!-- Blog Title -->
    <div class="bg-white xxxs:p-4 md:p-6">
      <nuxt-link :to="`/blog/${blog_id}`">
        <h2 class="text-xl font-bold xxxs:mb-1 md:mb-2 text-secondary hover:text-primary">{{ title }}</h2>
      </nuxt-link>
    </div>

    <!-- Blog Image and Content -->
    <div class="bg-gray-200 p-6">
      <img :src="`http://127.0.0.1:8000${image}`" alt="Blog Image" class="w-full h-auto mb-4">
      <p class="text-primary truncate">{{ content }}</p>
    </div>

    <!-- Author and Read More Section -->
    <div class="bg-white xxxs:p-4 md:p-6 flex justify-between items-center">
      <div>
        <p class="text-primary text-sm">By EtCare</p>
        <p class="text-primary text-sm">{{ publishedAt }}</p>
      </div>
      <div>
        <nuxt-link
          class="etcare-button xxxs:px-2 md:px-4 xxxs:py-1 md:py-2"
          :to="`/blog/${blog_id}`"
        >
          Read More
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: { type: String, required: true },
    summary: { type: String, default: "" },
    image: { type: String, required: true },
    content: { type: String, required: true },
    author: { type: String, required: true },
    publishedAt: { type: String, required: true },
    blog_id: { type: Number, required: true },
  },
};
</script>
