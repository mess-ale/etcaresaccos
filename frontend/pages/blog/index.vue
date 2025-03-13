<template>
    <div>
        <div class="pt-32 pb-12 space-y-4">
            <div class="body-padding_margin">
                <div class="container">
                    <h1 class="text-center text-primary font-oswald text-4xl font-bold">Etcare SACCO BLOG</h1>
                    <p class="text-center text-primary font-oswald">
                        Sharing training insights, the latest L&D trends, and tips to improve your training and
                        development here.
                    </p>
                </div>
            </div>
        </div>

        <div v-if="isLoading" class="text-primary text-center font-oswald text-6xl pt-12 pb-12">
            <LoadingPage />
        </div>

        <div v-else class="body-padding_margin mb-10">
            <div class="container">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <blog-component v-for="(blog, index) in blogPosts" :key="index" :blog_id="blog.blog_id"
                        :title="blog.title" :image="blog.blog_image" :content="blog.content" author="EtCare"
                        :publishedAt="blog.event_date" />
                </div>
            </div>
        </div>

        <!-- Pagination Buttons -->
        <div class="flex justify-center space-x-4 my-6">
            <button class="px-4 py-2 bg-primary text-white rounded cursor-pointer" @click="fetchBlogs(currentPage - 1)"
                :disabled="!pagination.previous">
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                    <path fill="currentColor"
                        d="m7.825 12l3.875 3.9q.275.275.288.688t-.288.712q-.275.275-.7.275t-.7-.275l-4.6-4.6q-.15-.15-.213-.325T5.426 12t.063-.375t.212-.325l4.6-4.6q.275-.275.688-.287t.712.287q.275.275.275.7t-.275.7zm6.6 0l3.875 3.9q.275.275.288.688t-.288.712q-.275.275-.7.275t-.7-.275l-4.6-4.6q-.15-.15-.213-.325T12.026 12t.063-.375t.212-.325l4.6-4.6q.275-.275.688-.287t.712.287q.275.275.275.7t-.275.7z">
                    </path>
                </svg>
            </button>
            <button class="px-4 py-2 bg-primary text-white rounded cursour-pointer" @click="fetchBlogs(currentPage + 1)"
                :disabled="!pagination.next">
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                    <path fill="currentColor"
                        d="M9.575 12L5 7.4L6.4 6l6 6l-6 6L5 16.6zm6.6 0L11.6 7.4L13 6l6 6l-6 6l-1.4-1.4z"></path>
                </svg>
            </button>
        </div>
    </div>
</template>

<script setup>
const { $axios } = useNuxtApp();
import { ref, onMounted } from 'vue';

useHead({
  title: 'Blog - Etcare SACCOs Ltd',
});
const blogPosts = ref([]);
const pagination = ref({
    next: null,
    previous: null,
});
const currentPage = ref(1);
const isLoading = ref(false);

const fetchBlogs = async (page = 1) => {
    isLoading.value = true;
    try {
        const response = await $axios.get(`/blogposts/?page=${page}`);
        blogPosts.value = response.data.results;
        pagination.value.next = response.data.next;
        pagination.value.previous = response.data.previous;
        currentPage.value = page;
    } catch (error) {
        console.error('Error fetching data:', error);
    } finally {
        isLoading.value = false;
    }
};

onMounted(() => {
    fetchBlogs();
});
</script>
