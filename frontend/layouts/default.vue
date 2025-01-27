<template>
    <div class="web-body">
        <header :style="{ backgroundColor: headerBackgroundColor }" class="fixed top-0 left-0 right-0 z-10 text-primary
            body-padding_margin">
            <div class="container">
                <div class="flex items-center justify-between xs:h-20 md:h-24 xxl:h-32">
                    <div class="w-1/4">
                        <nuxt-link to="/"><img
                                class="xxxs:w-24 xxxs:h-10 sm:w-32 sm:h-12 md:w-32 md:h-16 xxl:w-34 xxl:h-20"
                                src="../assets/Etcare_logo1-removebg.png" alt="etcare logo" />
                        </nuxt-link>
                    </div>

                    <div class="w-2/4 hidden lg:inline ">
                        <div class="lg:text-sm flex justify-center items-center xxl:text-lg">
                            <div class="lg:space-x-6 xxl:space-x-8 flex item-center font-bold">
                                <nuxt-link to="/" class="links">HOME</nuxt-link>
                                <div class="flex items-center dropdown-link">
                                    <nuxt-link to="/service" class="links">SERVICE</nuxt-link>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"
                                        class="ml-1">
                                        <path fill="currentColor" d="m5 8l7 8l7-8z"></path>
                                    </svg>
                                    <ul class="dropdown font-bold font-Roboto">
                                        <nuxt-link to="/service/saving">
                                            <li>
                                                Saving
                                            </li>
                                        </nuxt-link>
                                        <nuxt-link to="/service/equb">
                                            <li>
                                                equb
                                            </li>
                                        </nuxt-link>
                                        <nuxt-link to="/service/loan">
                                            <li>
                                                Loan
                                            </li>
                                        </nuxt-link>
                                        <nuxt-link to="/service/training">
                                            <li>
                                                training
                                            </li>
                                        </nuxt-link>
                                    </ul>
                                </div>
                                <nuxt-link to="/about" class="links">ABOUT</nuxt-link>
                                <nuxt-link to="/blog" class="links">BLOG</nuxt-link>
                                <nuxt-link to="/contact" class="links">CONTACT</nuxt-link>
                            </div>
                        </div>
                    </div>

                    <div class="w-2/4 lg:hidden flex justify-center items-center">
                        <button @click="toggleMenu" aria-label="Toggle Menu">
                            <svg v-if="!isMenuOpen" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="M4 18q-.425 0-.712-.288T3 17t.288-.712T4 16h16q.425 0 .713.288T21 17t-.288.713T20 18zm0-5q-.425 0-.712-.288T3 12t.288-.712T4 11h16q.425 0 .713.288T21 12t-.288.713T20 13zm0-5q-.425 0-.712-.288T3 7t.288-.712T4 6h16q.425 0 .713.288T21 7t-.288.713T20 8z">
                                </path>
                            </svg>

                            <svg v-if="isMenuOpen" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                class="font-bold" viewBox="0 0 24 24">
                                <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                    stroke-width="1.5" d="m5 19l7-7m0 0l7-7m-7 7L5 5m7 7l7 7"></path>
                            </svg>
                        </button>
                    </div>

                    <div v-if="isMenuOpen"
                        class="absolute top-16 z-100 left-0 w-full bg-gray-100 lg:hidden shadow-lg z-10">
                        <ul class="space-y-4 items-center py-2 font-bold text-center">
                            <li class="border-b-2">
                                <nuxt-link to="/" @click="closeMenu">HOME</nuxt-link>
                            </li>
                            <li class="border-b-2 flex justify-center items-center">
                                <nuxt-link to="/service" @click="closeMenu">SERVICE</nuxt-link>
                                <svg @click="toggleMenuservice" xmlns="http://www.w3.org/2000/svg" width="1em"
                                    height="1em" viewBox="0 0 24 24" class="ml-1">
                                    <path fill="currentColor" d="m5 8l7 8l7-8z"></path>
                                </svg>
                                <div v-if="openMenuService"
                                    class="absolute top-16 z-100 left-0 w-full bg-gray-300 lg:hidden shadow-lg z-10">
                                    <ul class="space-y-4 py-2 font-bold text-center">
                                        <li @click="closeMenuservice" class="border-b-2">
                                            <nuxt-link to="/service/saving">
                                                Saving
                                            </nuxt-link>
                                        </li>
                                        <li @click="closeMenuservice" class="border-b-2">
                                            <nuxt-link to="/service/equb">
                                                equb
                                            </nuxt-link>
                                        </li>
                                        <li @click="closeMenuservice" class="border-b-2">
                                            <nuxt-link to="/service/loan">
                                                Loan
                                            </nuxt-link>
                                        </li>
                                        <li @click="closeMenuservice">
                                            <nuxt-link to="/service/training">
                                                training
                                            </nuxt-link>
                                        </li>
                                    </ul>
                                </div>

                            </li>
                            <li class="border-b-2">
                                <nuxt-link to="/about" @click="closeMenu">ABOUT</nuxt-link>
                            </li>
                            <li class="border-b-2">
                                <nuxt-link to="/blog" @click="closeMenu">BLOG</nuxt-link>
                            </li>
                            <li class="border-b-2">
                                <nuxt-link to="/contact" @click="closeMenu">CONTACT</nuxt-link>
                            </li>
                        </ul>
                    </div>

                    <div class="w-1/4 flex space-x-4 justify-end">
                        <nuxt-link to="/MembershipForm"
                            class="xxxs:text-xs md:text-sm xxl:text-base flex etcare-button xxxs:pt-1 xxxs:pb-1 xxxs:pl-2 xxxs:pr-2 md:pt-1 md:pb-1 md:pl-4 md:pr-4 xxl:pt-2 xxl:pb-2 xxl:pl-8 xxl:pr-8 space-x-10">
                            JOIN US
                        </nuxt-link>
                    </div>
                </div>
            </div>
        </header>

        <div class="bg-background text-white h-100">
            <slot />
        </div>

        <footer class="bg-primary font-roboto text-white ">
            <div class="body-padding_margin">
                <div class="container">
                    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 pt-10 pb-10">

                        <div class="space-y-3 ">
                            <div class="items-center flex space-x-5">
                                <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                    <path fill="currentColor"
                                        d="M12 20.556q-.235 0-.47-.077t-.432-.25q-1.067-.981-2.164-2.185q-1.096-1.203-1.99-2.493t-1.468-2.633t-.572-2.622q0-3.173 2.066-5.234Q9.037 3 12 3t5.03 2.062q2.066 2.061 2.066 5.234q0 1.279-.572 2.613q-.572 1.333-1.458 2.632q-.885 1.3-1.981 2.494T12.92 20.21q-.191.173-.434.26q-.244.086-.487.086m.004-8.825q.667 0 1.14-.476q.472-.475.472-1.143t-.476-1.14t-1.143-.472t-1.14.476t-.472 1.143t.475 1.14t1.144.472">
                                    </path>
                                </svg>
                                <a href="https://maps.app.goo.gl/Bim8BvzZjeQAjKTU8" class="links" target="_blank">
                                    <h4>Addis Ababa, Ethiopia</h4>
                                </a>
                            </div>

                            <div class="items-center flex space-x-5">
                                <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                    <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                        stroke-width="2">
                                        <path stroke-dasharray="64" stroke-dashoffset="64"
                                            d="M4 5h16c0.55 0 1 0.45 1 1v12c0 0.55 -0.45 1 -1 1h-16c-0.55 0 -1 -0.45 -1 -1v-12c0 -0.55 0.45 -1 1 -1Z">
                                            <animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s"
                                                values="64;0"></animate>
                                        </path>
                                        <path stroke-dasharray="24" stroke-dashoffset="24" d="M3 6.5l9 5.5l9 -5.5">
                                            <animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s"
                                                dur="0.2s" values="24;0"></animate>
                                        </path>
                                    </g>
                                </svg>
                                <a href="mailto:Etcare@gmail.com" class="links">
                                    <h4>Etcare@gmail.com</h4>
                                </a>
                            </div>

                            <div class="items-center flex space-x-5">
                                <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                    <path fill="currentColor"
                                        d="M19.95 21q-3.125 0-6.175-1.362t-5.55-3.863t-3.862-5.55T3 4.05q0-.45.3-.75t.75-.3H8.1q.35 0 .625.238t.325.562l.65 3.5q.05.4-.025.675T9.4 8.45L6.975 10.9q.5.925 1.187 1.787t1.513 1.663q.775.775 1.625 1.438T13.1 17l2.35-2.35q.225-.225.588-.337t.712-.063l3.45.7q.35.1.575.363T21 15.9v4.05q0 .45-.3.75t-.75.3">
                                    </path>
                                </svg>

                                <a href="tel:+251917550560" class="links">
                                    <h4>+251-91-755-0560</h4>
                                </a>
                            </div>

                        </div>


                        <div>
                            <h4 class="mb-4 font-bold font-oswald">COMPANY</h4>
                            <ul class="space-y-2">
                                <li>
                                    <nuxt-link to="/about" class="links">About</nuxt-link>
                                </li>
                                <li>
                                    <nuxt-link to="/service" class="links">Service</nuxt-link>
                                </li>
                                <li>
                                    <nuxt-link to="/blog" class="links">Blog</nuxt-link>
                                </li>
                                <li>
                                    <nuxt-link to="/service/saving" class="links">Saving</nuxt-link>
                                </li>
                                <li>
                                    <nuxt-link to="/service/equb" class="links">Equb</nuxt-link>
                                </li>
                                <li>
                                    <nuxt-link to="/service/loan" class="links">Loan</nuxt-link>
                                </li>
                            </ul>
                        </div>


                        <div class="space-y-3">
                            <h4 class="mb-4 font-bold font-oswald">LATEST NEWS</h4>

                            <footerblogco
                             v-for="(blog, index) in blogPostsLetest" :key="index" :blog_id="blog.blog_id"
                            :description="blog.title" :imageSrc="blog.blog_image" :content="blog.content" author="EtCare"
                            :date="blog.event_date"/>
                            </div>
                        <div>
                            <h5 class="text-justify mb-4 font-bold ">Contact your nearest Etcare SACCO branch to receive
                                your
                                account username and password.</h5>
                            <div class="flex justify-center pt-5">
                                <nuxt-link to="/contact"
                                    class="etcare-button xs:pt-1 xxxs:pb-1 xxxs:pl-5 xxxs:pr-5 md:pt-2 md:pb-2 md:pl-8 md:pr-8 footer-button flex items-center space-x-4">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"
                                        viewBox="0 0 20 20">
                                        <path fill="currentColor"
                                            d="M17 11v3l-3-3H8a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h10a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2zm-3 2v2a2 2 0 0 1-2 2H6l-3 3v-3H2a2 2 0 0 1-2-2V8c0-1.1.9-2 2-2h2v3a4 4 0 0 0 4 4z">
                                        </path>
                                    </svg>
                                    <h1> contact us</h1>
                                </nuxt-link>
                            </div>

                            <div class="flex justify-center">
                                <div class="flex space-x-3 pt-5">
                                    <nuxt-link to="https://web.facebook.com/etcaresacco" target="_blank"><svg
                                            class="socialM" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path fill="currentColor"
                                                d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95c5.05-.5 9-4.76 9-9.95">
                                            </path>
                                        </svg></nuxt-link>
                                    <nuxt-link to="https://www.youtube.com/@etcarebeautyandcosmeticssales"
                                        target="_blank">
                                        <svg class="socialM" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path fill="currentColor"
                                                d="M12.244 4c.534.003 1.87.016 3.29.073l.504.022c1.429.067 2.857.183 3.566.38c.945.266 1.687 1.04 1.938 2.022c.4 1.56.45 4.602.456 5.339l.001.152v.174c-.007.737-.057 3.78-.457 5.339c-.254.985-.997 1.76-1.938 2.022c-.709.197-2.137.313-3.566.38l-.504.023c-1.42.056-2.756.07-3.29.072l-.235.001h-.255c-1.13-.007-5.856-.058-7.36-.476c-.944-.266-1.687-1.04-1.938-2.022c-.4-1.56-.45-4.602-.456-5.339v-.326c.006-.737.056-3.78.456-5.339c.254-.985.997-1.76 1.939-2.021c1.503-.419 6.23-.47 7.36-.476zM9.999 8.5v7l6-3.5z">
                                            </path>
                                        </svg></nuxt-link>
                                    <nuxt-link to="https://vm.tiktok.com/ZMhQxWYC7/" target="_blank"> <svg
                                            class="socialM" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path
                                                d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74a2.89 2.89 0 0 1 2.31-4.64a2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z"
                                                fill="currentColor"></path>
                                        </svg></nuxt-link>

                                    <nuxt-link to="https://t.me/etcaresacco" target="_blank"><svg class="socialM"
                                            xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path
                                                d="M9.78 18.65l.28-4.23l7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3L3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"
                                                fill="currentColor"></path>
                                        </svg></nuxt-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="textcopy">
                <div class="body-padding_margin">
                    <div class="container">
                        <div
                            class="grid grid-cols-1 md:grid-cols-2 gap-4 xxxs:py-4 justify-around w-full items-center text-primary md:py-6 xxl:py-8">
                            <div>
                                <nuxt-link to="/"> <img src="../assets/Etcare_logo1-removebg.png" alt="etcare logo" />
                                </nuxt-link>
                            </div>
                            <div>
                                <h4 class="font-bold md:text-end">© 2024 by EtCare Sacco. All Rights Reserved.</h4>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
const { $axios } = useNuxtApp();

const headerBackgroundColor = ref('rgba(255, 255, 255, 0.55)');
const isMenuOpen = ref(false);
const openMenuService = ref(false);
const isLoading = ref(false);
const blogPostsLetest = ref([]);

const fetchBlogs = async () => {
    isLoading.value = true;
    try {
        const response = await $axios.get(`/LatestBlogs/`);
        blogPostsLetest.value = response.data;
        console.log("letest blog posts", response.data)
    } catch (error) {
        console.error('Error fetching data:', error);
    } finally {
        isLoading.value = false;
    }
};

const handleScroll = async () => {
    if (window.scrollY > 100) {
        headerBackgroundColor.value = '#fff';
    } else {
        headerBackgroundColor.value = 'rgba(255, 255, 255, 0.55)';
    }
};

const toggleMenu = () => {
    isMenuOpen.value = !isMenuOpen.value;
}

const closeMenu = () => {
    isMenuOpen.value = !isMenuOpen.value;
    openMenuService.value = false;
}
const toggleMenuservice = () => {
    openMenuService.value = !openMenuService.value;
}

const closeMenuservice = () => {
    openMenuService.value = !openMenuService.value;
    isMenuOpen.value = false;
}

onMounted(async () => {
    window.addEventListener('scroll', handleScroll);
    fetchBlogs();
});

onBeforeUnmount(() => {
    window.removeEventListener('scroll', handleScroll);
});
</script>

<style>
@media (min-width: 200px) {
    .body-padding_margin {
        padding: 0 1rem;
    }
}

@media (min-width: 500px) {
    .body-padding_margin {
        padding: 0 2.25rem;
    }
}

@media (min-width: 800px) {
    .body-padding_margin {
        padding: 0 2.5rem;
    }
}

@media (min-width: 1200px) {
    .body-padding_margin {
        padding: 0 3rem;
    }
}

/* global.css */
.container {
    max-width: 1240px;
    /* Adjust this value as per your design */
    margin: 0 auto;
    /* Center the container */
    padding: 0 1rem;
    /* Add some padding for smaller screens */
}

.home-image {
    border-radius: 50%;
    width: 170px;
    height: 170px;
    border: 4px solid theme('colors.secondary');
}

.cancle-img {
    cursor: pointer;
}

.web-body {
    padding: 0;
    margin: 0;
    background-color: theme('colors.background');
}

.links:hover {
    color: theme('colors.secondary');
}

.etcare-button {
    background-color: theme('colors.primary');
    color: theme('colors.white');
    border-radius: 10px 10px 10px 0;
    border: none;
    cursor: pointer;
    transition: color, background-color  0.15s ease-in-out;
}

.etcare-button:hover {
    background-color: theme('colors.background');
    color: theme('colors.secondary');
}

.footer-button {
    font-size: 0.8rem;
    border-radius: 1px;
    background-color: theme('colors.secondary');
    color: theme('colors.background');

}

.textcopy {
    background-color: theme('colors.background');
}

.footerpadding {
    padding: 0 4rem;
    height: 440px;
}

.socialM {
    transition: transform .3s ease-in-out;
}

.socialM:hover {
    transform: translateY(-15%);
    color: theme('colors.secondary');
}

.dropdown {
    position: absolute;
    background-color: white;
    /* Replace with theme('colors.white') */
    width: 25%;
    border-top: solid 1px #ccc;
    /* Replace with theme('colors.secondary') */
    top: 60%;
    visibility: hidden;
    opacity: 0;
    transition: opacity 1s, visibility 1s;
}

.dropdown-link:hover .dropdown {
    visibility: visible;
    opacity: 1;
}

.dropdown li:hover {
    color: theme('colors.secondary');
}

.dropdown li {
    padding: 0.5rem 1rem;
    position: relative;
    border-bottom: solid 1px theme('colors.secondary');
    overflow: hidden;
}

.dropdown li::before {
    content: '';
    background-image: linear-gradient(to right, transparent, theme('colors.primary'));
    width: 0;
    position: absolute;
    bottom: 0;
    height: 100%;
    left: 0;
    transition: width 0.65s ease;
}

.dropdown li:hover::before {
    width: 100%;
}
</style>