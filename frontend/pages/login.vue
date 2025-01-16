<template>
    <div class="flex items-center justify-center min-h-screen login-back">
        <div class="w-full max-w-md p-8 bg-white rounded-lg shadow-lg space-y-6">
            <h1 class="font-oswald text-center text-2xl font-bold text-blue-900">log in form</h1>
            <form @submit.prevent="handleLogin" class="space-y-4">
                <div>
                    <label class="text-blue-900 font-robot">username*</label>
                    <input type="text" placeholder="Enter your Username..."
                        class="w-full p-3 mt-1 rounded-md border border-blue-200 focus:outline-none focus:border-blue-500"
                        v-model="username" required />
                </div>
                <div>
                    <label class="text-blue-900 font-robot">password*</label>
                    <input type="password" placeholder="Enter your Password..."
                        class="w-full p-3 mt-1 rounded-md border border-blue-200 focus:outline-none focus:border-blue-500"
                        v-model="password" required />
                </div>
                <button type="submit"
                    class="w-full py-3 mt-4 text-white bg-secondary rounded-md hover:bg-red-600 flex justify-center items-center">
                    Log in <span class="ml-2">🔑</span>
                </button>
            </form>
            <div class="flex justify-between text-blue-900 font-semibold">
                <a href="/contact" class="hover:underline">Don’t have an account?</a>
                <a href="/contact" class="hover:underline">Forgot password?</a>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
const { $axios } = useNuxtApp();
import { useRouter } from 'vue-router';
import { useAuthStore } from '~~/stores/auth';

const authStore = useAuthStore();
const router = useRouter();
const username = ref('');
const password = ref('');

const handleLogin = async () => {
    try {
        const response = await $axios.post(
            '/token/',
            {
                username: username.value,
                password: password.value
            }
        );
        try {
            const response = await $axios.get('/userlogin/', null, {
                withCredentials: true,
            });

            console.log(response.data);
        } catch (err) {
            console.log("this is error of etcare", err)
        }

        // useCookie('accessToken').value = response.data.access;  // Store token in cookies
        // useCookie('refreshToken').value = response.data.refresh;
        console.log(response)
        router.push('/');
    } catch (error) {
        console.error('Login failed:', error);
        // Handle login errors
    }
};

definePageMeta({
    layout: false
});
</script>

<style scoped>
.login-back {
    background-image: url("../assets/login.png");
    background-position: center;
    background-size: cover;
}
</style>